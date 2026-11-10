#!/usr/bin/env python3
"""Normalize and verify the paper's original case-level result records.

Maintainer source format
------------------------
The maintainer source is a structured results file with two sheets, one per
Windows environment, each holding one row per *sample* (technique x payload
family). The source file itself is not part of the public artifact.
Every product column carries that sample's outcome for that product, coded
``O1``-``O5``.

    sheet          -> environment
    Win11 汇总     -> Win11Enterprise
    Server2025 汇总-> Server2025

    69 rows x 6 product columns = 414 outcomes per sheet
    414 x 2                                   = 828
    minus 36 baseline (technique id 0)        = 792 non-baseline  ✓

Why the technique ids are remapped
----------------------------------
The workbook's numeric ``技术ID`` is **not** the paper's technique number — the
spreadsheet rows are ordered differently from Table I. The mapping below was
therefore derived from the data, not assumed: each row group's 36-outcome
distribution was matched against the distribution implied by that technique's
README, which is unique for 18 of the 22 groups. The remaining four form two
pairs with identical distributions, and the sample names disambiguate them:

    "移除回调（内核级别）" (kernel callback removal) -> T6,  leaving T15
    "直接系统调用"        (direct syscall)           -> T1,  leaving T2

``verify()`` re-checks the whole mapping against the README reconstruction and
fails loudly if any group does not match, so a wrong row assignment cannot slip
through silently.

Note: the workbook labels the T20 row with the strategy name "逻辑绕过"
(Logic Bypass). The row's data is T20 — PE Resource Masquerading. The paper's
Figure 2 places T20 in the **Obfuscation** strategy, and that grouping is what
the framework uses; the spreadsheet label is a strategy name, not a technique
name, and does not override Figure 2.

Usage
-----
    python framework/tools/import_outcomes.py <paper-results.xlsx>
    python framework/tools/import_outcomes.py <paper-results.xlsx> --check
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (  # noqa: E402
    LAYER1_MEMBERS, LAYER2_MEMBERS, LEVELS, PAYLOAD_ORDER, PRODUCT_ORDER,
    RESULTS_DIR, TECHNIQUES, TECHNIQUE_ORDER, case_id, write_csv,
)

# --- workbook -> framework vocabularies ---------------------------------

SHEET_TO_ENV = {
    "Win11 汇总": "Win11Enterprise",
    "Server2025 汇总": "Server2025",
}

COLUMN_TO_PRODUCT = {
    "Sophos": "Sophos",
    "Kaspersky": "Kaspersky",
    "Bitdefender": "Bitdefender",
    "Windows Defender": "DefenderAV",
    "Elastic": "Elastic",
    "Huorong": "Huorong",
}

PAYLOAD_TO_ID = {
    "Cobalt Strike": "CobaltStrike",
    "Havoc": "Havoc",
    "AdaptixC2": "AdaptixC2",
}

LEVEL_MAP = {f"O{i}": f"L{i}" for i in range(1, 6)}

#: workbook 技术ID -> paper technique id. See the module docstring for how
#: this was derived and how verify() enforces it.
XL_TO_TECHNIQUE = {
    0: "T0",   # 原生样本 — baseline, no evasion logic
    1: "T7", 2: "T8", 3: "T6", 4: "T12", 5: "T19", 6: "T9", 7: "T1",
    8: "T13", 9: "T14", 10: "T15", 11: "T5", 12: "T2", 13: "T3",
    14: "T17", 15: "T18", 16: "T21", 17: "T10", 18: "T11", 19: "T22",
    20: "T4", 21: "T20", 22: "T16",
}

OUT_FIELDS = [
    "case_id", "technique_id", "technique_name", "layer1", "layer2",
    "payload_family", "product", "environment", "is_baseline",
    "level", "level_name",
]

LEVEL_NAMES = {
    "L1": "Pre-execution Prevention", "L2": "Pre-C2 Prevention",
    "L3": "Pre-command Prevention", "L4": "Command-stage Prevention",
    "L5": "Operational Success",
}


# --- reading the workbook ------------------------------------------------

def _read_with_openpyxl(path: Path):
    from openpyxl import load_workbook
    wb = load_workbook(path, read_only=True, data_only=True)
    for name in wb.sheetnames:
        yield name, [list(r) for r in wb[name].iter_rows(values_only=True)]


def _read_with_stdlib(path: Path):
    """Minimal xlsx reader: shared strings + sheet order. No dependencies."""
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
          "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    with zipfile.ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in root.findall("m:si", ns):
                shared.append("".join(t.text or "" for t in si.iter(
                    "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")))

        rels = {}
        root = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        for rel in root:
            rels[rel.get("Id")] = rel.get("Target")

        wb = ET.fromstring(z.read("xl/workbook.xml"))
        for sheet in wb.find("m:sheets", ns):
            name = sheet.get("name")
            rid = sheet.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            target = rels[rid].lstrip("/")
            if not target.startswith("xl/"):
                target = "xl/" + target
            sx = ET.fromstring(z.read(target))
            rows = []
            for row in sx.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row"):
                cells = {}
                for c in row:
                    ref = c.get("r") or ""
                    col = "".join(ch for ch in ref if ch.isalpha())
                    idx = 0
                    for ch in col:
                        idx = idx * 26 + (ord(ch) - 64)
                    v = c.find("m:v", ns)
                    txt = v.text if v is not None else None
                    if txt is not None and c.get("t") == "s":
                        txt = shared[int(txt)]
                    elif txt is None:
                        isel = c.find("m:is", ns)
                        if isel is not None:
                            txt = "".join(t.text or "" for t in isel.iter(
                                "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t"))
                    cells[idx - 1] = txt
                rows.append([cells.get(i) for i in range(max(cells) + 1 if cells else 0)])
            yield name, rows


def read_sheets(path: Path):
    try:
        yield from _read_with_openpyxl(path)
    except ImportError:
        print("[i] openpyxl not installed; using the built-in stdlib xlsx reader")
        yield from _read_with_stdlib(path)


# --- import --------------------------------------------------------------

def import_workbook(path: Path):
    rows = []
    for sheet_name, sheet in read_sheets(path):
        env = SHEET_TO_ENV.get(sheet_name.strip())
        if env is None:
            print(f"[i] skipping unrecognised sheet: {sheet_name!r}")
            continue

        header_idx = next((i for i, r in enumerate(sheet)
                           if r and str(r[0]).strip() == "技术ID"), None)
        if header_idx is None:
            raise ValueError(f"no '技术ID' header row in sheet {sheet_name!r}")
        header = [str(c).strip() if c is not None else "" for c in sheet[header_idx]]

        cols = {}
        for ci, name in enumerate(header):
            if name in COLUMN_TO_PRODUCT:
                cols[ci] = COLUMN_TO_PRODUCT[name]
        missing = set(COLUMN_TO_PRODUCT.values()) - set(cols.values())
        if missing:
            raise ValueError(f"sheet {sheet_name!r} is missing product column(s): {sorted(missing)}")

        for offset, r in enumerate(sheet[header_idx + 1:], start=header_idx + 2):
            if r is None or not r or r[0] is None:
                continue
            try:
                xl_id = int(r[0])
            except (TypeError, ValueError):
                continue
            if xl_id not in XL_TO_TECHNIQUE:
                raise ValueError(f"unknown 技术ID {xl_id!r} in sheet {sheet_name!r} row {offset}")

            tech = XL_TO_TECHNIQUE[xl_id]
            spec = TECHNIQUES.get(tech)
            payload_raw = str(r[3]).strip() if len(r) > 3 and r[3] else ""
            if payload_raw not in PAYLOAD_TO_ID:
                raise ValueError(f"unknown payload {payload_raw!r} in row {offset}")
            payload = PAYLOAD_TO_ID[payload_raw]

            for ci, product in cols.items():
                code = str(r[ci]).strip().upper() if ci < len(r) and r[ci] else ""
                if code not in LEVEL_MAP:
                    raise ValueError(f"unknown outcome code {code!r} in row {offset}")
                level = LEVEL_MAP[code]
                rows.append({
                    "case_id": case_id(tech, payload, product, env),
                    "technique_id": tech,
                    "technique_name": "Baseline Payload (no evasion logic)" if tech == "T0"
                                      else spec["name"],
                    "layer1": "" if tech == "T0" else spec["layer1"],
                    "layer2": "" if tech == "T0" else spec["layer2"],
                    "payload_family": payload,
                    "product": product,
                    "environment": env,
                    "is_baseline": tech == "T0",
                    "level": level,
                    "level_name": LEVEL_NAMES[level],
                    "trend": str(r[4]).strip() if len(r) > 4 and r[4] else "",
                    "source_sheet": sheet_name.strip(),
                    "source_row": offset,
                })
    return rows


def verify(rows: list[dict]) -> list[str]:
    """Cross-check the import against the paper and the README reconstruction."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_results_from_readmes as build  # noqa: WPS433

    problems = []
    baseline = [r for r in rows if r["is_baseline"]]
    non = [r for r in rows if not r["is_baseline"]]

    def check(label, expected, actual):
        if expected != actual:
            problems.append(f"{label}: expected {expected}, got {actual}")

    check("baseline outcomes", 36, len(baseline))
    check("non-baseline outcomes", 792, len(non))
    check("total outcomes", 828, len(rows))
    check("baseline all L1", {"L1"}, {r["level"] for r in baseline})

    l5 = sum(1 for r in non if r["level"] == "L5")
    check("L5 outcomes", build.PAPER_EXPECT["total_l5"], l5)

    # every aggregate the paper states
    from collections import Counter
    for product in PRODUCT_ORDER:
        sub = [r for r in non if r["product"] == product]
        got = round(sum(1 for r in sub if r["level"] == "L5") / len(sub) * 100, 1)
        check(f"per-product L5 {product}", build.PAPER_EXPECT["per_product_l5"][product], got)
    for payload in PAYLOAD_ORDER:
        sub = [r for r in non if r["payload_family"] == payload]
        got = round(sum(1 for r in sub if r["level"] == "L5") / len(sub) * 100, 1)
        check(f"per-payload L5 {payload}", build.PAPER_EXPECT["per_payload_l5"][payload], got)

    for stage, members in LAYER1_MEMBERS.items():
        sub = [r for r in non if r["technique_id"] in members]
        dist = Counter(r["level"] for r in sub)
        got = [round(dist[l] / len(sub) * 100, 1) for l in LEVELS]
        check(f"Layer 1 BDD {stage}", build.PAPER_EXPECT["layer1_bdd"][stage], got)
    for strat, members in LAYER2_MEMBERS.items():
        sub = [r for r in non if r["technique_id"] in members]
        dist = Counter(r["level"] for r in sub)
        got = [round(dist[l] / len(sub) * 100, 1) for l in LEVELS]
        check(f"Layer 2 BDD {strat}", build.PAPER_EXPECT["layer2_bdd"][strat], got)
    for strat, members in LAYER2_MEMBERS.items():
        got = []
        for payload in PAYLOAD_ORDER:
            sub = [r for r in non if r["technique_id"] in members and r["payload_family"] == payload]
            got.append(round(sum(1 for r in sub if r["level"] == "L5") / len(sub) * 100, 1))
        exp = build.PAPER_EXPECT["layer2_by_payload_l5"][strat]
        if any(abs(a - b) >= 0.05 for a, b in zip(got, exp)):
            problems.append(f"Table III {strat}: expected {exp}, got {got}")

    # per technique: the imported joint data must reproduce the README tables
    recon = build.collect()["tech_counts"]
    for tech in TECHNIQUE_ORDER:
        sub = [r for r in non if r["technique_id"] == tech]
        dist = Counter(r["level"] for r in sub)
        got = [dist[l] for l in LEVELS]
        if sum(got) != 36:
            problems.append(f"{tech}: {sum(got)} outcomes, expected 36")
        elif got != recon[tech]:
            problems.append(f"{tech}: imported counts {got} != README counts {recon[tech]}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="Normalize the paper's original case-level results.")
    ap.add_argument("workbook", type=Path)
    ap.add_argument("--check", action="store_true", help="verify only; write nothing")
    ap.add_argument("--out", type=Path, default=RESULTS_DIR / "outcomes_scored.csv")
    args = ap.parse_args()

    if not args.workbook.exists():
        print(f"[!] workbook not found: {args.workbook}")
        return 2

    rows = import_workbook(args.workbook)
    print(f"[i] imported {len(rows)} outcomes "
          f"({sum(1 for r in rows if r['is_baseline'])} baseline, "
          f"{sum(1 for r in rows if not r['is_baseline'])} non-baseline)")

    problems = verify(rows)
    if problems:
        print(f"\n[!] {len(problems)} verification problem(s) -- refusing to write:")
        for p in problems[:40]:
            print("   ", p)
        return 1
    print("[+] verification passed: the imported matrix reproduces every paper aggregate")
    print("    and every per-technique README distribution exactly")

    if not args.check:
        write_csv(args.out, OUT_FIELDS,
                  [{field: row[field] for field in OUT_FIELDS} for row in rows])
        print(f"[+] wrote {args.out}")
        print("[i] now run:  python framework/metrics.py  &&  python framework/figures.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
