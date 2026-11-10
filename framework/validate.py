#!/usr/bin/env python3
"""Stage 2 (Function Validation) -- the two-stage quality gate.

The paper (Section III-B) requires every sample to pass two checks *before*
it is used in the evaluation:

  1. **Evasion Logic Verification** -- the sample's core evasion mechanism
     reaches its predefined post-condition under the designated validation
     configuration. For techniques that depend on product-specific security
     state, the required target state is confirmed to exist *before* the run
     and the state change is confirmed *after*.

  2. **Payload Functionality Check** -- the underlying payload still works
     after the bypass: the beacon calls back within 60 s and answers the test
     commands (``whoami``, ``ipconfig``, ``tasklist``, ``upload``).

A sample that fails either check because of an implementation defect or an
unmet prerequisite is logged with its point of failure and **returned for
revision**. Only samples that satisfy all applicable criteria are admitted.

This script operationalises that gate:

    python framework/validate.py init                 # write a blank checklist
    python framework/validate.py init --out my.csv
    python framework/validate.py check                # evaluate the gate
    python framework/validate.py check --file my.csv

Validation rows are one per (technique, stage). ``status`` is one of
``pass``, ``fail``, ``not_applicable``, ``pending``.

Exit code of ``check`` is 0 only if every technique in scope is admitted.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS_DIR, TECHNIQUES, TECHNIQUE_ORDER, read_csv, write_csv  # noqa: E402

FIELDS = [
    "technique_id", "technique_name", "stage", "criterion", "expected_state",
    "validation_config", "status", "evidence_ref", "reviewer", "date", "notes",
]

STAGES = ["evasion_logic", "payload_functionality"]

PAYLOAD_CRITERION = (
    "C2 beacon observed on the listener within the 60-second window, and the "
    "beacon answers the test commands (whoami, ipconfig, tasklist, upload) "
    "after the bypass logic has been applied."
)


def build_template(techniques: list[str]) -> list[dict]:
    rows = []
    for t in techniques:
        spec = TECHNIQUES[t]
        rows.append({
            "technique_id": t,
            "technique_name": spec["name"],
            "stage": "evasion_logic",
            "criterion": spec["evasion_logic_criterion"],
            "expected_state": ("target components present and verified before the run; "
                               "state change verified after"
                               if spec["validation_config"] == "product-present"
                               else "post-condition verified in a clean baseline environment"),
            "validation_config": spec["validation_config"],
            "status": "pending",
            "evidence_ref": "",
            "reviewer": "",
            "date": "",
            "notes": spec.get("divergence", "") or spec.get("implementation_note", ""),
        })
        rows.append({
            "technique_id": t,
            "technique_name": spec["name"],
            "stage": "payload_functionality",
            "criterion": PAYLOAD_CRITERION,
            "expected_state": "beacon + command response observed",
            "validation_config": spec["validation_config"],
            "status": "pending",
            "evidence_ref": "",
            "reviewer": "",
            "date": "",
            "notes": "",
        })
    return rows


def check(rows: list[dict]) -> tuple[list[str], list[str], list[str]]:
    """Return (admitted, rejected, incomplete) technique id lists."""
    by_tech: dict[str, list[dict]] = {}
    for row in rows:
        by_tech.setdefault(row["technique_id"], []).append(row)

    admitted, rejected, incomplete = [], [], []
    for t in TECHNIQUE_ORDER:
        checks = by_tech.get(t)
        if not checks:
            incomplete.append(t)
            continue
        stages = [c.get("stage", "") for c in checks]
        statuses = [c.get("status", "") for c in checks]
        if (len(checks) != len(STAGES)
                or set(stages) != set(STAGES)
                or len(stages) != len(set(stages))
                or any(status not in {"pass", "fail", "not_applicable", "pending"}
                       for status in statuses)):
            incomplete.append(t)
            continue
        applicable = [c for c in checks if c["status"] != "not_applicable"]
        if not applicable:
            incomplete.append(t)
        elif any(c["status"] == "fail" for c in applicable):
            rejected.append(t)
        elif any(c["status"] == "pending" for c in applicable):
            incomplete.append(t)
        elif all(c["status"] == "pass" for c in applicable):
            admitted.append(t)
        else:
            incomplete.append(t)
    return admitted, rejected, incomplete


def cmd_init(args) -> int:
    techniques = args.technique or TECHNIQUE_ORDER
    out = args.out or (RESULTS_DIR / "validation.template.csv")
    rows = build_template(techniques)
    write_csv(out, FIELDS, rows)
    print(f"[+] wrote {len(rows)} validation rows ({len(techniques)} techniques x 2 stages) to {out}")
    print("[i] copy it to results/validation.csv, fill in status/evidence_ref/reviewer/date,")
    print("    then run:  python framework/validate.py check")
    return 0


def cmd_check(args) -> int:
    path = args.file or (RESULTS_DIR / "validation.csv")
    if not path.exists():
        print(f"[!] no validation file at {path}")
        print("[i] create one with:  python framework/validate.py init")
        print("    then copy results/validation.template.csv to results/validation.csv and fill it in")
        return 2
    rows = read_csv(path)
    admitted, rejected, incomplete = check(rows)

    print(f"[i] validation file: {path}")
    print(f"[i] techniques admitted : {len(admitted):2}  {', '.join(admitted) or '-'}")
    print(f"[i] techniques rejected : {len(rejected):2}  {', '.join(rejected) or '-'}")
    print(f"[i] incomplete/pending  : {len(incomplete):2}  {', '.join(incomplete) or '-'}")

    for t in rejected:
        fails = [r for r in rows if r["technique_id"] == t and r["status"] == "fail"]
        for f in fails:
            print(f"    [!] {t} / {f['stage']}: {f['notes'] or 'no point of failure recorded'}")

    if rejected or incomplete:
        print("\n[!] quality gate NOT passed: samples above must not enter the evaluation")
        return 1
    print("\n[+] quality gate passed: all techniques admitted")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Two-stage function validation and quality gate.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="write a blank validation checklist")
    p_init.add_argument("--out", type=Path, default=None)
    p_init.add_argument("--technique", action="append", default=None)
    p_init.set_defaults(func=cmd_init)

    p_check = sub.add_parser("check", help="evaluate the quality gate over a filled checklist")
    p_check.add_argument("--file", type=Path, default=None)
    p_check.set_defaults(func=cmd_check)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
