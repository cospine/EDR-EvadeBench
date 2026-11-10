#!/usr/bin/env python3
"""Stage 4b (Effectiveness Evaluation) -- PSD and BDD metrics.

Implements the two metrics defined in Section III-D of the paper.

**Prevention Stage Distribution (PSD)** -- paper Eq. (1)

    PSD_p = < P_p(L1), P_p(L2), P_p(L3), P_p(L4), P_p(L5) >

where each element is the proportion of product *p*'s outcomes assigned to
that level. PSD is computed **per product**.

**Bypass Depth Distribution (BDD)** -- paper Eq. (2)

    BDD_g = < Q_g(L1), Q_g(L2), Q_g(L3), Q_g(L4), Q_g(L5) >

where each element is the proportion of outcomes for group *g* assigned to
that level, normalised by the total number of outcomes for *g*. A group may be
a DET category (Layer 1 stage or Layer 2 strategy) or an individual technique.

Both are also computable separately by environment or payload family.

Data sources
------------
The script uses whichever of these exist, and says clearly what it could not
compute:

* a case-level outcome matrix (the paper's original results or ``score.py`` output)
      -> full PSD (all five levels) and full BDD.
* ``results/technique_level.csv``  (per technique, L1..L5 counts)
      -> full BDD by technique, Layer 1 stage, Layer 2 strategy and overall.
* ``results/by_product.csv`` / ``results/by_payload.csv``  (L5 counts only)
      -> the L5 component of PSD, and L5 by payload family.

Usage
-----
    python framework/metrics.py                 # auto-detect inputs, write results/metrics/
    python framework/metrics.py --source outcomes
    python framework/metrics.py --source technique-level
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    LAYER1_MEMBERS, LAYER1_ORDER, LAYER2_MEMBERS, LAYER2_ORDER, LEVELS, LEVEL_NAMES,
    PAYLOAD_ORDER, PRODUCT_ORDER, RESULTS_DIR, TECHNIQUES, TECHNIQUE_ORDER,
    counts_by_level, distribution, read_csv, write_csv,
)

METRICS_DIR = RESULTS_DIR / "metrics"


def _pct(x: float) -> str:
    return f"{x * 100:.1f}%"


def load_outcomes(path: Path) -> list[dict]:
    """Read a scored-outcome CSV, drop baseline rows, fill layer1/layer2.

    Layer membership is resolved from the schema by technique id rather than
    taken from the file, so any outcome file carrying a technique id works --
    including one produced by ``score.py``, which does not emit layer columns.
    Baseline rows are excluded: the paper computes PSD and BDD over
    non-baseline outcomes.
    """
    out = []
    for row in read_csv(path):
        if str(row.get("is_baseline", "")).strip().lower() in ("true", "1", "yes"):
            continue
        spec = TECHNIQUES.get(str(row.get("technique_id", "")).strip())
        if spec:
            row = dict(row)
            row["layer1"] = row.get("layer1") or spec["layer1"]
            row["layer2"] = row.get("layer2") or spec["layer2"]
        out.append(row)
    return out


def psd_from_outcomes(rows: list[dict]) -> list[dict]:
    """PSD per product from case-level scored outcomes (paper Eq. 1)."""
    out = []
    for product in PRODUCT_ORDER:
        subset = [r for r in rows if r["product"] == product]
        counts = counts_by_level(subset)
        dist = distribution(counts)
        out.append({
            "product": product,
            "n": len(subset),
            **{lvl: round(dist[lvl], 6) for lvl in LEVELS},
        })
    return out


def prevention_by_stage(rows: list[dict]) -> list[dict]:
    """Prevention rate per product per Layer 1 stage (paper Figure 6).

    Measured as the proportion of outcomes the product prevented from reaching
    L5 (Operational Success), i.e. ``1 - L5 rate``.
    """
    out = []
    for product in PRODUCT_ORDER:
        for stage in LAYER1_ORDER:
            subset = [r for r in rows if r["product"] == product and r["layer1"] == stage]
            if not subset:
                continue
            n = len(subset)
            k = sum(1 for r in subset if r["level"] == "L5")
            out.append({
                "product": product,
                "stage": stage,
                "n": n,
                "l5_count": k,
                "prevention_rate": round(1 - k / n, 6),
            })
    return out


def l5_by_layer2_payload(rows: list[dict]) -> list[dict]:
    """L5 rates per Layer 2 strategy and payload family (paper Table III)."""
    out = []
    for strategy in LAYER2_ORDER:
        members = set(LAYER2_MEMBERS[strategy])
        for payload in PAYLOAD_ORDER:
            subset = [r for r in rows
                      if r["technique_id"] in members and r["payload_family"] == payload]
            n = sum(int(r["n"]) for r in subset)
            k = sum(int(r["n_l5"]) for r in subset)
            out.append({
                "layer2": strategy,
                "payload_family": payload,
                "n": n,
                "L5_count": k,
                "L5": round(k / n, 6) if n else 0.0,
            })
    return out


def l5_by_layer2_payload_from_outcomes(rows: list[dict]) -> list[dict]:
    """Table III rows computed directly from case-level outcomes."""
    out = []
    for strategy in LAYER2_ORDER:
        for payload in PAYLOAD_ORDER:
            subset = [r for r in rows
                      if r["layer2"] == strategy and r["payload_family"] == payload]
            n = len(subset)
            k = sum(1 for r in subset if r["level"] == "L5")
            out.append({
                "layer2": strategy,
                "payload_family": payload,
                "n": n,
                "L5_count": k,
                "L5": round(k / n, 6) if n else 0.0,
            })
    return out


def l5_overall_by_payload_from_outcomes(rows: list[dict]) -> list[dict]:
    out = []
    for payload in PAYLOAD_ORDER:
        subset = [r for r in rows if r["payload_family"] == payload]
        n = len(subset)
        k = sum(1 for r in subset if r["level"] == "L5")
        out.append({"payload_family": payload, "n": n, "L5_count": k,
                    "L5": round(k / n, 6) if n else 0.0})
    return out


def bdd_from_outcomes(rows: list[dict], key: str) -> list[dict]:
    """BDD over arbitrary groups from case-level scored outcomes (paper Eq. 2)."""
    groups = sorted({r[key] for r in rows})
    out = []
    for g in groups:
        subset = [r for r in rows if r[key] == g]
        counts = counts_by_level(subset)
        dist = distribution(counts)
        out.append({"group": g, "n": len(subset), **{lvl: round(dist[lvl], 6) for lvl in LEVELS}})
    return out


def bdd_from_technique_level(rows: list[dict], members: list[str] | None = None) -> list[dict]:
    """BDD from per-technique L1..L5 counts.

    ``members=None`` yields one row per technique; otherwise the counts of the
    listed techniques are summed before normalising (a DET category).
    """
    out = []
    if members is None:
        for row in rows:
            counts = {lvl: int(row[lvl]) for lvl in LEVELS}
            dist = distribution(counts)
            out.append({
                "group": row["technique_id"],
                "n": sum(counts.values()),
                **{lvl: round(dist[lvl], 6) for lvl in LEVELS},
            })
        return out

    total = {lvl: 0 for lvl in LEVELS}
    n = 0
    for row in rows:
        if row["technique_id"] in members:
            for lvl in LEVELS:
                total[lvl] += int(row[lvl])
            n += sum(int(row[lvl]) for lvl in LEVELS)
    dist = distribution(total)
    return [{"group": "(all)", "n": n, **{lvl: round(dist[lvl], 6) for lvl in LEVELS}}]


def merge_groups(rows: list[dict]) -> dict[str, int]:
    total = {lvl: 0 for lvl in LEVELS}
    for row in rows:
        for lvl in LEVELS:
            total[lvl] += int(row[lvl])
    return total


def write_bdd(path: Path, group_col: str, groups: list[tuple[str, dict]]) -> None:
    out = []
    for name, counts in groups:
        n = sum(counts.values())
        dist = distribution(counts)
        out.append({group_col: name, "n": n, **{lvl: round(dist[lvl], 6) for lvl in LEVELS}})
    write_csv(path, [group_col, "n", *LEVELS], out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Compute PSD and BDD (paper Section III-D).")
    ap.add_argument("--source", choices=["auto", "outcomes", "technique-level"], default="auto")
    ap.add_argument("--outcomes", type=Path, default=RESULTS_DIR / "outcomes_scored.csv",
                    help="case-level outcome CSV (default: released paper results)")
    ap.add_argument("--outdir", type=Path, default=METRICS_DIR)
    args = ap.parse_args()

    outcomes_path = args.outcomes
    tech_path = RESULTS_DIR / "technique_level.csv"
    by_product_path = RESULTS_DIR / "by_product.csv"
    by_payload_path = RESULTS_DIR / "by_payload.csv"

    have_outcomes = outcomes_path.exists() and args.source in ("auto", "outcomes")
    have_tech = tech_path.exists() and args.source in ("auto", "technique-level")

    if not have_outcomes and not have_tech:
        print("[!] no input data found.")
        print(f"    expected either {outcomes_path} (case-level) or {tech_path} (technique-level)")
        print("[i] an evaluator running their own experiment should produce case-level data with:")
        print("      python framework/cases.py     --out results/cases.csv")
        print("      python framework/score.py template --out results/evidence.local.csv")
        print("      python framework/score.py run --in results/evidence.local.csv")
        return 2

    args.outdir.mkdir(parents=True, exist_ok=True)
    notes = []

    # ---------------- BDD ----------------
    if have_outcomes:
        rows = load_outcomes(outcomes_path)
        write_csv(args.outdir / "bdd_technique.csv",
                  ["group", "n", *LEVELS], bdd_from_outcomes(rows, "technique_id"))
        write_csv(args.outdir / "bdd_layer1.csv",
                  ["group", "n", *LEVELS], bdd_from_outcomes(rows, "layer1"))
        write_csv(args.outdir / "bdd_layer2.csv",
                  ["group", "n", *LEVELS], bdd_from_outcomes(rows, "layer2"))
        write_csv(args.outdir / "bdd_payload.csv",
                  ["group", "n", *LEVELS], bdd_from_outcomes(rows, "payload_family"))
        write_csv(args.outdir / "bdd_environment.csv",
                  ["group", "n", *LEVELS], bdd_from_outcomes(rows, "environment"))
        write_bdd(args.outdir / "bdd_overall.csv", "group",
                  [("Overall", counts_by_level(rows))])
        print(f"[+] BDD written from case-level outcomes ({len(rows)} cases)")
    else:
        tech_rows = read_csv(tech_path)
        write_csv(args.outdir / "bdd_technique.csv",
                  ["group", "n", *LEVELS], bdd_from_technique_level(tech_rows))
        groups = []
        for stage in LAYER1_ORDER:
            groups.append((stage, merge_groups(
                [r for r in tech_rows if r["technique_id"] in LAYER1_MEMBERS[stage]])))
        write_bdd(args.outdir / "bdd_layer1.csv", "group", groups)
        groups = []
        for strat in LAYER2_ORDER:
            groups.append((strat, merge_groups(
                [r for r in tech_rows if r["technique_id"] in LAYER2_MEMBERS[strat]])))
        write_bdd(args.outdir / "bdd_layer2.csv", "group", groups)
        write_bdd(args.outdir / "bdd_overall.csv", "group",
                  [("Overall", merge_groups(tech_rows))])
        print(f"[+] BDD written from technique-level counts ({len(tech_rows)} techniques)")

    # ---------------- PSD ----------------
    if have_outcomes:
        rows = load_outcomes(outcomes_path)
        psd = psd_from_outcomes(rows)
        write_csv(args.outdir / "psd_by_product.csv", ["product", "n", *LEVELS], psd)
        print("[+] PSD written (all five levels) from case-level outcomes")
        write_csv(args.outdir / "prevention_by_stage.csv",
                  ["product", "stage", "n", "l5_count", "prevention_rate"],
                  prevention_by_stage(rows))
        print("[+] prevention rate by Layer 1 stage written (Figure 6)")
    else:
        if by_product_path.exists():
            rows = read_csv(by_product_path)
            out = []
            for product in PRODUCT_ORDER:
                subset = [r for r in rows if r["product"] == product]
                n = sum(int(r["n"]) for r in subset)
                k = sum(int(r["n_l5"]) for r in subset)
                out.append({"product": product, "n": n, "L5_count": k,
                            "L5": round(k / n, 6) if n else 0.0})
            write_csv(args.outdir / "psd_by_product_l5_only.csv",
                      ["product", "n", "L5_count", "L5"], out)
            print("[+] PSD written in L5-only form (per-product L1-L4 counts are not available)")
            notes.append("PSD is L5-only: the released per-product data records only L5 counts. "
                         "Full PSD requires case-level outcomes.")
        else:
            notes.append("PSD not computed: neither case-level outcomes nor per-product data present.")

    # ---------------- L5 by payload ----------------
    if have_outcomes:
        outcome_rows = load_outcomes(outcomes_path)
        table3 = l5_by_layer2_payload_from_outcomes(outcome_rows)
        write_csv(args.outdir / "l5_by_layer2_payload.csv",
                  ["layer2", "payload_family", "n", "L5_count", "L5"], table3)
        print("[+] Layer 2 L5 by payload family written (paper Table III)")
        out = l5_overall_by_payload_from_outcomes(outcome_rows)
        write_csv(args.outdir / "l5_overall_by_payload.csv",
                  ["payload_family", "n", "L5_count", "L5"], out)
        print("[+] overall L5 by payload family written")
    elif by_payload_path.exists():
        rows = read_csv(by_payload_path)
        table3 = l5_by_layer2_payload(rows)
        write_csv(args.outdir / "l5_by_layer2_payload.csv",
                  ["layer2", "payload_family", "n", "L5_count", "L5"], table3)
        print("[+] Layer 2 L5 by payload family written (paper Table III)")

        out = []
        for payload in PAYLOAD_ORDER:
            subset = [r for r in rows if r["payload_family"] == payload]
            n = sum(int(r["n"]) for r in subset)
            k = sum(int(r["n_l5"]) for r in subset)
            out.append({"payload_family": payload, "n": n, "L5_count": k,
                        "L5": round(k / n, 6) if n else 0.0})
        write_csv(args.outdir / "l5_overall_by_payload.csv",
                  ["payload_family", "n", "L5_count", "L5"], out)
        print("[+] overall L5 by payload family written")

    if notes:
        print()
        for note in notes:
            print(f"[i] {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
