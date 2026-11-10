#!/usr/bin/env python3
"""Build ``results/`` from the outcome tables in the 22 technique READMEs.

Why this exists
---------------
The technique READMEs report, for each technique, a Bypass Depth Distribution
over 36 outcomes, an L5 rate per product (n=6) and an L5 rate per payload
family (n=12). Those percentages are exact multiples of 1/36, 1/6 and 1/12
rounded to 0.1%, so the underlying **integer counts are recoverable without
loss**. This script performs that inversion, validates it, and emits the
resulting data as CSV so that the rest of the framework -- and any reader --
can verify the paper's aggregates rather than take them on trust.

What it can and cannot reconstruct
----------------------------------
* Reconstructed: per-technique L1-L5 counts (n=36); per-technique L5 counts by
  product (n=6) and by payload family (n=12). From these, every Layer 1 and
  Layer 2 aggregate, the overall L5 rate, and Table III of the paper follow.
* NOT reconstructed: the joint 6x3x2 assignment per technique. The marginals
  above do not determine the 36 individual cells, so the full 792-row outcome
  matrix cannot be derived here. That requires the authors' case-level records.

Resolved: the Layer 2 mapping of T20 and T21
--------------------------------------------
The first run of this checker reported two failures -- the Layer 2 BDD for
**Obfuscation** and for **Logic Bypass**. Both are now resolved, and the paper
fully determined the answer: Figure 2 of the paper places **PE Resource
Masquerading (T20) in the Obfuscation column** and **API-level Behavioral
Obfuscation (T21) in the Logic Bypass column**, whereas the root README and
this framework's schema had the two swapped.

With the mapping corrected, the per-technique tables reproduce the paper's
Figure 5 exactly:

    Obfuscation   = T17, T18, T19, T20  ->  54/57/9/0/24  of 144 = 37.5/39.6/6.2/0.0/16.7
    Logic Bypass  = T21, T22            ->  12/34/8/0/18  of  72 = 16.7/47.2/11.1/0.0/25.0

This is recorded in CHANGELOG.md rather than left as a silent edit, because a
reader comparing this artifact against the submitted paper may have the older
mapping.

Usage
-----
    python framework/tools/build_results_from_readmes.py
    python framework/tools/build_results_from_readmes.py --check    # verify only
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import (  # noqa: E402
    LAYER1_MEMBERS, LAYER2_MEMBERS, LEVELS, PAYLOAD_ORDER, PRODUCT_ORDER,
    REPO_ROOT, RESULTS_DIR, TECHNIQUES, TECHNIQUE_ORDER, distribution, write_csv,
)

# ---------------------------------------------------------------- parsing

def _pcts(line: str) -> list[float]:
    return [float(x) for x in re.findall(r"([0-9]+(?:\.[0-9]+)?)%", line)]


def _row_after(lines: list[str], heading: str) -> list[float] | None:
    for i, line in enumerate(lines):
        if heading in line:
            for j in range(i + 1, min(i + 8, len(lines))):
                cand = lines[j].strip()
                if cand.startswith("|") and "%" in cand and ":---" not in cand:
                    return _pcts(cand)
    return None


def parse_readme(path: Path) -> tuple[list[float], list[float], list[float]]:
    lines = path.read_text(encoding="utf-8").split("\n")
    bdd = _row_after(lines, "**Bypass Depth Distribution")
    pay = _row_after(lines, "**Payload sensitivity")
    prod = _row_after(lines, "**Per-product L5 rate")
    if not (bdd and pay and prod):
        raise ValueError(f"could not parse result tables from {path}")
    if len(bdd) != 5 or len(pay) != 3 or len(prod) != 6:
        raise ValueError(f"unexpected table width in {path}: {len(bdd)}/{len(pay)}/{len(prod)}")
    return bdd, pay, prod


def to_counts(pcts: list[float], n: int) -> list[int]:
    """Invert a percentage back to integer counts and check it is exact."""
    counts = [round(x / 100.0 * n) for x in pcts]
    for pct, cnt in zip(pcts, counts):
        if abs(cnt / n * 100.0 - pct) > 0.06:
            raise ValueError(f"percentage {pct}% is not consistent with n={n} (got {cnt})")
    return counts


# ---------------------------------------------------------------- expected

#: Aggregates stated in the paper, used to cross-check the reconstruction.
PAPER_EXPECT = {
    "total_outcomes": 792,
    "total_l5": 182,
    "overall_l5_rate": 23.0,
    "per_product_l5": {"Sophos": 0.0, "Kaspersky": 16.7, "Bitdefender": 0.0,
                       "Elastic": 9.1, "Huorong": 57.6, "DefenderAV": 54.5},
    "per_payload_l5": {"CobaltStrike": 8.7, "Havoc": 32.6, "AdaptixC2": 27.7},
    # paper Table IV (Layer 1 BDD), percent
    "layer1_bdd": {
        "Collection":   [25.0, 34.4, 12.2, 2.4, 26.0],
        "Transmission": [16.7, 33.3, 0.0, 16.7, 33.3],
        "Detection":    [28.6, 41.5, 9.2, 0.4, 20.3],
    },
    # paper Figure 5 (Layer 2 BDD), percent
    "layer2_bdd": {
        "EDR Sensor Disruption": [20.0, 41.7, 12.8, 3.9, 21.7],
        "EDR Agent Disruption":  [33.3, 22.2, 11.1, 0.0, 33.3],
        "Telemetry Blocking":    [16.7, 33.3, 0.0, 16.7, 33.3],
        "Memory Concealment":    [27.0, 40.9, 10.3, 0.8, 21.0],
        "Obfuscation":           [37.5, 39.6, 6.2, 0.0, 16.7],
        "Logic Bypass":          [16.7, 47.2, 11.1, 0.0, 25.0],
    },
    # paper Table III (Layer 2 L5 rate by payload family), percent
    "layer2_by_payload_l5": {
        "EDR Sensor Disruption": [3.3, 36.7, 25.0],
        "EDR Agent Disruption":  [33.3, 33.3, 33.3],
        "Telemetry Blocking":    [33.3, 33.3, 33.3],
        "Memory Concealment":    [6.0, 28.6, 28.6],
        "Obfuscation":           [0.0, 29.2, 20.8],
        "Logic Bypass":          [0.0, 41.7, 33.3],
    },
}

#: Check areas that are knowingly not reconciled. Empty: every cross-check now
#: passes. The mechanism is kept so that a future discrepancy can be pinned
#: deliberately (and reported) rather than silently tolerated -- and so that
#: an *undocumented* mismatch always fails the run.
KNOWN_DISCREPANCIES: dict[str, tuple[list[float], list[float]]] = {}


# ---------------------------------------------------------------- core

def collect() -> dict:
    """Parse the 22 READMEs and run every cross-check against the paper."""
    tech_counts: dict[str, list[int]] = {}
    tech_by_product: dict[str, list[int]] = {}
    tech_by_payload: dict[str, list[int]] = {}

    for t in TECHNIQUE_ORDER:
        folder = next((p for p in REPO_ROOT.glob(f"{t}_*") if p.is_dir()), None)
        if folder is None:
            raise FileNotFoundError(f"no folder for {t}")
        bdd, pay, prod = parse_readme(folder / "README.md")
        tech_counts[t] = to_counts(bdd, 36)
        tech_by_payload[t] = to_counts(pay, 12)
        tech_by_product[t] = to_counts(prod, 6)

    checks: list[tuple[str, str, str, bool]] = []
    problems: list[str] = []

    def record(area: str, expected, actual, ok: bool) -> None:
        checks.append((area, str(expected), str(actual), ok))
        if not ok:
            problems.append(f"{area}: expected {expected}, got {actual}")

    # ---- level 1: internal consistency ---------------------------------
    for t in TECHNIQUE_ORDER:
        c = tech_counts[t]
        if sum(c) != 36:
            record(f"{t} BDD total", 36, sum(c), False)
        for label, arr in (("payload", tech_by_payload[t]), ("product", tech_by_product[t])):
            if sum(arr) != c[4]:
                record(f"{t} {label} L5 total", c[4], sum(arr), False)

    # ---- level 2: overall totals ---------------------------------------
    total_outcomes = sum(sum(v) for v in tech_counts.values())
    total_l5 = sum(v[4] for v in tech_counts.values())
    record("total non-baseline outcomes", PAPER_EXPECT["total_outcomes"], total_outcomes,
           total_outcomes == PAPER_EXPECT["total_outcomes"])
    record("total L5 outcomes", PAPER_EXPECT["total_l5"], total_l5,
           total_l5 == PAPER_EXPECT["total_l5"])
    record("overall L5 rate (%)", PAPER_EXPECT["overall_l5_rate"],
           round(total_l5 / total_outcomes * 100, 1),
           round(total_l5 / total_outcomes * 100, 1) == PAPER_EXPECT["overall_l5_rate"])

    # ---- level 2: per-product and per-payload L5 -----------------------
    pidx = {p: i for i, p in enumerate(PRODUCT_ORDER)}
    for product in PRODUCT_ORDER:
        k = sum(tech_by_product[t][pidx[product]] for t in TECHNIQUE_ORDER)
        got = round(k / (len(TECHNIQUE_ORDER) * 6) * 100, 1)
        record(f"per-product L5 rate {product}", PAPER_EXPECT["per_product_l5"][product], got,
               got == PAPER_EXPECT["per_product_l5"][product])

    yidx = {p: i for i, p in enumerate(PAYLOAD_ORDER)}
    for payload in PAYLOAD_ORDER:
        k = sum(tech_by_payload[t][yidx[payload]] for t in TECHNIQUE_ORDER)
        got = round(k / (len(TECHNIQUE_ORDER) * 12) * 100, 1)
        record(f"per-payload L5 rate {payload}", PAPER_EXPECT["per_payload_l5"][payload], got,
               got == PAPER_EXPECT["per_payload_l5"][payload])

    def group_counts(members: list[str]) -> list[int]:
        return [sum(tech_counts[t][i] for t in members) for i in range(5)]

    # ---- level 3: paper Table IV (Layer 1 BDD) -------------------------
    for stage, members in LAYER1_MEMBERS.items():
        counts = group_counts(members)
        dist = distribution(dict(zip(LEVELS, counts)))
        got = [round(dist[l] * 100, 1) for l in LEVELS]
        record(f"Layer 1 BDD {stage}", PAPER_EXPECT["layer1_bdd"][stage], got,
               got == PAPER_EXPECT["layer1_bdd"][stage])

    # ---- level 3: paper Figure 5 (Layer 2 BDD) -------------------------
    for strat, members in LAYER2_MEMBERS.items():
        counts = group_counts(members)
        dist = distribution(dict(zip(LEVELS, counts)))
        got = [round(dist[l] * 100, 1) for l in LEVELS]
        record(f"Layer 2 BDD {strat}", PAPER_EXPECT["layer2_bdd"][strat], got,
               got == PAPER_EXPECT["layer2_bdd"][strat])

    # ---- level 3: paper Table III (Layer 2 L5 by payload) --------------
    for strat, members in LAYER2_MEMBERS.items():
        got = []
        for i in range(3):
            n = len(members) * 12
            k = sum(tech_by_payload[t][i] for t in members)
            got.append(round(k / n * 100, 1))
        exp = PAPER_EXPECT["layer2_by_payload_l5"][strat]
        record(f"Table III L5-by-payload {strat}", exp, got,
               all(abs(a - b) < 0.05 for a, b in zip(got, exp)))

    return {
        "tech_counts": tech_counts,
        "by_product": tech_by_product,
        "by_payload": tech_by_payload,
        "checks": checks,
        "problems": problems,
        "total_outcomes": total_outcomes,
        "total_l5": total_l5,
    }


def write_results(result: dict) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    tech_counts = result["tech_counts"]

    rows = []
    for t in TECHNIQUE_ORDER:
        spec = TECHNIQUES[t]
        c = tech_counts[t]
        rows.append({
            "technique_id": t, "technique_name": spec["name"],
            "layer1": spec["layer1"], "layer2": spec["layer2"],
            "n": sum(c), **{lvl: c[i] for i, lvl in enumerate(LEVELS)},
            "l5_rate": round(c[4] / sum(c), 4),
        })
    write_csv(RESULTS_DIR / "technique_level.csv",
              ["technique_id", "technique_name", "layer1", "layer2", "n",
               *LEVELS, "l5_rate"], rows)

    rows = [{"technique_id": t, "product": product, "n": 6,
             "n_l5": result["by_product"][t][i]}
            for t in TECHNIQUE_ORDER for i, product in enumerate(PRODUCT_ORDER)]
    write_csv(RESULTS_DIR / "by_product.csv", ["technique_id", "product", "n", "n_l5"], rows)

    rows = [{"technique_id": t, "payload_family": payload, "n": 12,
             "n_l5": result["by_payload"][t][i]}
            for t in TECHNIQUE_ORDER for i, payload in enumerate(PAYLOAD_ORDER)]
    write_csv(RESULTS_DIR / "by_payload.csv",
              ["technique_id", "payload_family", "n", "n_l5"], rows)

    print(f"[+] wrote results/technique_level.csv ({len(TECHNIQUE_ORDER)} techniques)")
    print(f"[+] wrote results/by_product.csv ({len(TECHNIQUE_ORDER) * 6} rows)")
    print(f"[+] wrote results/by_payload.csv ({len(TECHNIQUE_ORDER) * 3} rows)")


def write_report(result: dict) -> None:
    checks = result["checks"]
    ok = sum(1 for _, _, _, good in checks if good)
    lines = [
        "# Consistency Report",
        "",
        "Generated by `framework/tools/build_results_from_readmes.py`.",
        "",
        "This report checks that the outcome tables in the 22 technique READMEs,",
        "converted from percentages back to integer counts, reproduce every",
        "aggregate stated in the companion paper.",
        "",
        "## Summary",
        "",
        f"- Cross-checks run: **{len(checks)}**",
        f"- Passed: **{ok}**",
        f"- Failed: **{len(checks) - ok}**",
        "",
        "## Reconstructed totals",
        "",
        "| Quantity | Reconstructed | Paper |",
        "| :--- | ---: | ---: |",
        f"| Non-baseline outcomes | {result['total_outcomes']} | 792 |",
        f"| L5 outcomes | {result['total_l5']} | 182 |",
        f"| Overall L5 rate | {result['total_l5'] / result['total_outcomes'] * 100:.1f}% | 23.0% |",
        "",
        "## Checks",
        "",
        "| Area | Expected | Reconstructed | Result |",
        "| :--- | :--- | :--- | :---: |",
    ]
    for area, exp, act, good in checks:
        lines.append(f"| {area} | {exp} | {act} | {'PASS' if good else '**FAIL**'} |")

    failing = [c for c in checks if not c[3]]
    lines += [
        "",
        "## Open discrepancies",
        "",
    ]
    if failing:
        lines += [
            f"{len(failing)} check(s) do not reconcile. These are recorded here rather than",
            "silently adjusted, because resolving them requires the authors' case-level",
            "records (see `results/README.md`).",
            "",
        ]
        for area, exp, act, _ in failing:
            lines += [
                f"**{area}**",
                "",
                f"- paper: `{exp}`",
                f"- reconstructed from the technique READMEs: `{act}`",
                "",
            ]
        lines += [
            "The L5 and L4 values agree; only the L1/L2/L3 split diverges. The paper's",
            "Figure 5 and its running text are consistent with each other, so the",
            "divergence is between the paper and the per-technique README tables.",
            "",
        ]
    else:
        lines += ["None. Every check reconciles.", ""]

    lines += [
        "## Relationship to the case-level matrix",
        "",
        "This report reconstructs per-technique **marginals** from the READMEs: the",
        "level distribution (n=36), the per-product L5 counts (n=6) and the",
        "per-payload L5 counts (n=12). Those marginals do not determine the 36",
        "individual cells of each technique, so this route alone cannot produce the",
        "joint matrix.",
        "",
        "The paper's original joint result matrix is shipped separately as",
        "`results/outcomes_scored.csv`. With it present, `metrics.py` computes",
        "the full PSD (all five per-product levels) and the Figure 6 prevention",
        "rates. The original Figures 4, 5 and 6 are shipped as PDF files; `figures.py`",
        "can optionally render data-equivalent SVG versions under `figures/generated/`.",
        "",
        "The two routes cross-check each other: the joint matrix's per-technique",
        "distributions must equal the ones reconstructed here.",
        "",
        "## Reproducing this report",
        "",
        "```bash",
        "python framework/tools/build_results_from_readmes.py",
        "python framework/metrics.py",
        "python framework/figures.py",
        "python framework/tests/test_metrics.py",
        "```",
        "",
    ]
    (RESULTS_DIR / "consistency_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] wrote {RESULTS_DIR / 'consistency_report.md'}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Reconstruct results/ from the technique READMEs.")
    ap.add_argument("--check", action="store_true", help="verify only; write nothing")
    args = ap.parse_args()

    result = collect()
    failing = {area: (exp, act) for area, exp, act, ok in result["checks"] if not ok}
    ok = len(result["checks"]) - len(failing)
    print(f"[i] cross-checks against the paper: {ok}/{len(result['checks'])} passed")

    if not args.check:
        write_results(result)
        write_report(result)

    if not failing:
        print("[+] reconstruction is fully consistent with every stated paper aggregate")
        return 0

    known = {area: (str(exp), str(act)) for area, (exp, act) in KNOWN_DISCREPANCIES.items()}
    new = {a: v for a, v in failing.items() if a not in known}
    pinned_moved = {a: v for a, v in failing.items() if a in known and known[a] != v}

    for area, (exp, act) in failing.items():
        print(f"[!] {area}: paper {exp}  vs  reconstructed {act}")

    if new or pinned_moved:
        print("\n[!] FAIL: undocumented mismatch(es) -- investigate before publishing")
        return 1

    print(f"\n[i] the {len(failing)} failure(s) above are the documented open discrepancies")
    print("    (see results/README.md and results/consistency_report.md).")
    print("    All other aggregates reconcile exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
