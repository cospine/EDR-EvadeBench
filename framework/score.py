#!/usr/bin/env python3
"""Stage 4a (Effectiveness Evaluation) -- assign one of the five outcome levels.

The paper (Section III-C, "Outcome Assessment") assigns each execution one of
five mutually exclusive levels by **correlating three evidence sources**:

  1. endpoint process and network state,
  2. C2 server logs,
  3. product alerts or local protection logs.

Because that correlation is a judgement over heterogeneous evidence, this
script does not attempt to "detect" outcomes. It takes the evidence fields a
reviewer has already recorded in a structured form and applies the paper's
decision procedure deterministically, so that two evaluators given the same
evidence reach the same label. Cases whose evidence is internally
inconsistent are refused rather than scored, and are reported for manual
review.

Input:  one row per case, with the evidence columns below.
Output: the same rows plus ``level``, ``score_status`` and ``score_reason``.

Usage
-----
    python framework/score.py template --out evidence.csv     # blank rows for all 792 cases
    python framework/score.py run --in evidence.csv --out results/outcomes_scored.local.csv
    python framework/score.py explain                         # print the decision procedure
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS_DIR, enumerate_cases, read_csv, write_csv  # noqa: E402

EVIDENCE_FIELDS = [
    "case_id", "technique_id", "payload_family", "product", "environment",
    # --- evidence recorded by the reviewer, from the three sources ---
    "process_created",
    "process_terminated_by_product",
    "c2_beacon_observed",
    "c2_beacon_latency_s",
    "commands_sent",
    "commands_completed",
    "session_alive_at_end",
    "product_alert_observed",
    "evidence_refs",
    "notes",
]

OUTPUT_FIELDS = EVIDENCE_FIELDS + ["level", "level_name", "score_status", "score_reason"]

LEVEL_NAMES = {
    "L1": "Pre-execution Prevention",
    "L2": "Pre-C2 Prevention",
    "L3": "Pre-command Prevention",
    "L4": "Command-stage Prevention",
    "L5": "Operational Success",
}

_TRUTHY = {"true", "1", "yes", "y", "t"}
_FALSY = {"false", "0", "no", "n", "f", ""}


def _flag(row: dict, key: str):
    """Parse a tri-state boolean: True, False, or None when not recorded."""
    raw = (row.get(key) or "").strip().lower()
    if raw in _TRUTHY:
        return True
    if raw in _FALSY:
        return False if raw != "" else None
    return None


def _int(row: dict, key: str):
    raw = (row.get(key) or "").strip()
    if raw == "":
        return None
    try:
        return int(float(raw))
    except ValueError:
        return None


def score_row(row: dict) -> tuple[str | None, str, str]:
    """Apply the paper's decision procedure. Returns (level, status, reason)."""
    created = _flag(row, "process_created")
    terminated = _flag(row, "process_terminated_by_product")
    beacon = _flag(row, "c2_beacon_observed")
    sent = _int(row, "commands_sent")
    completed = _int(row, "commands_completed")
    alive = _flag(row, "session_alive_at_end")

    # --- L1 vs L2 cannot be separated without knowing whether a process ran ---
    if created is None:
        return None, "ambiguous", "process_created not recorded: L1 and L2 cannot be separated"

    if created is False:
        return "L1", "determined", "no process created (blocked pre-execution)"

    # A process ran. Did a beacon appear?
    if beacon is None:
        return None, "ambiguous", "c2_beacon_observed not recorded"
    if beacon is False:
        if terminated is True:
            return "L2", "determined", "process ran and was terminated before any C2 connection"
        if terminated is False or alive is True:
            return (None, "ambiguous",
                    "no C2 connection and no product termination: this indicates a payload or "
                    "validation defect, not prevention -- return the sample for revision")
        return None, "ambiguous", "no C2 connection but termination by product not recorded"

    # Beacon established. Was any command issued?
    if sent is None:
        return None, "ambiguous", "commands_sent not recorded"
    if sent == 0:
        if alive is True:
            return (None, "ambiguous",
                    "beacon established, no commands issued, session still alive: the evaluator "
                    "did not exercise the session, so L3 vs L5 cannot be decided")
        if terminated is True or alive is False:
            return "L3", "determined", "session terminated before any command was sent"
        return None, "ambiguous", "no commands sent but session state not recorded"

    if completed is None:
        return None, "ambiguous", "commands_completed not recorded"
    if sent < 0 or completed < 0:
        return None, "ambiguous", "command counts cannot be negative"
    if completed > sent:
        return None, "ambiguous", "commands_completed cannot exceed commands_sent"
    if completed < sent or alive is False:
        return "L4", "determined", "commands issued but did not all complete, or session ended"
    if alive is None:
        return None, "ambiguous", "session_alive_at_end not recorded: L4 and L5 cannot be separated"
    return "L5", "determined", "all commands completed and the session survived the observation window"


def cmd_explain(args) -> int:
    print(__doc__)
    print("Decision procedure applied by score_row():\n")
    print("  process_created == False                  -> L1")
    print("  process ran, terminated, no beacon        -> L2")
    print("  beacon up, terminated before any command  -> L3")
    print("  commands sent but incomplete / session dead-> L4")
    print("  all commands completed, session alive     -> L5")
    print("\n  Anything else is refused as ambiguous and returned for manual review,")
    print("  including the important case of 'no C2 connection and no product")
    print("  termination', which indicates a sample defect rather than prevention.")
    return 0


def cmd_template(args) -> int:
    rows = enumerate_cases()
    blank = [{k: "" for k in EVIDENCE_FIELDS} | {
        "case_id": r["case_id"], "technique_id": r["technique_id"],
        "payload_family": r["payload_family"], "product": r["product"],
        "environment": r["environment"],
    } for r in rows]
    out = args.out or (RESULTS_DIR / "evidence.template.csv")
    write_csv(out, EVIDENCE_FIELDS, blank)
    print(f"[+] wrote {len(blank)} blank evidence rows to {out}")
    return 0


def cmd_run(args) -> int:
    src = args.input or (RESULTS_DIR / "evidence.csv")
    if not src.exists():
        print(f"[!] no evidence file at {src}")
        print("[i] create a template with:  python framework/score.py template --out evidence.csv")
        return 2
    rows = read_csv(src)
    out_rows, tally, ambiguous = [], {}, []
    for row in rows:
        level, status, reason = score_row(row)
        enriched = dict(row)
        enriched["level"] = level or ""
        enriched["level_name"] = LEVEL_NAMES.get(level, "")
        enriched["score_status"] = status
        enriched["score_reason"] = reason
        out_rows.append(enriched)
        if level:
            tally[level] = tally.get(level, 0) + 1
        else:
            ambiguous.append(enriched)

    out = args.out or (RESULTS_DIR / "outcomes_scored.local.csv")
    write_csv(out, OUTPUT_FIELDS, out_rows)

    print(f"[+] scored {len(out_rows)} cases -> {out}")
    for lvl in ["L1", "L2", "L3", "L4", "L5"]:
        n = tally.get(lvl, 0)
        pct = (n / len(out_rows) * 100) if out_rows else 0.0
        print(f"    {lvl} {LEVEL_NAMES[lvl]:<26} {n:4}  {pct:5.1f}%")
    if ambiguous:
        print(f"\n[!] {len(ambiguous)} case(s) refused as ambiguous and requiring manual review:")
        for row in ambiguous[:20]:
            print(f"    {row['case_id']}: {row['score_reason']}")
        if len(ambiguous) > 20:
            print(f"    ... and {len(ambiguous) - 20} more")
        return 1
    print("\n[+] all cases scored deterministically")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Assign L1-L5 to evaluated cases.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_t = sub.add_parser("template", help="write a blank evidence CSV")
    p_t.add_argument("--out", type=Path, default=None)
    p_t.set_defaults(func=cmd_template)

    p_r = sub.add_parser("run", help="score an evidence CSV")
    p_r.add_argument("--in", dest="input", type=Path, default=None)
    p_r.add_argument("--out", type=Path, default=None)
    p_r.set_defaults(func=cmd_run)

    p_e = sub.add_parser("explain", help="print the decision procedure")
    p_e.set_defaults(func=cmd_explain)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
