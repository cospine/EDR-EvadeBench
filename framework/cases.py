#!/usr/bin/env python3
"""Stage 1 (Sample Generation) -- enumerate the evaluation case matrix.

The paper's design is

    technique  x  payload family  x  product  x  environment
       22      x        3         x     6      x      2        = 792 cases

plus 36 baseline cases (3 payload families x 6 products x 2 environments)
using AES-protected payloads without additional evasion logic.

This script materialises that matrix as CSV so that every later stage has a
stable set of case identifiers to attach evidence and outcomes to. It does
NOT generate payloads: per the paper, evaluators supply their own, protected
with the same AES-based encryption / runtime decryption procedure (payload
buffer format ``[16-byte IV] + AES-256-CBC ciphertext``).

Usage
-----
    python framework/cases.py                       # 792 cases -> stdout summary
    python framework/cases.py --out results/cases.csv
    python framework/cases.py --baseline --out results/baseline_cases.csv
    python framework/cases.py --technique T7 --out /tmp/t7.csv
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ENVIRONMENT_ORDER, PAYLOAD_ORDER, PRODUCT_ORDER, TECHNIQUES, TECHNIQUE_ORDER,
    enumerate_cases, write_csv,
)

FIELDS = [
    "case_id", "technique_id", "technique_name", "layer1", "layer2",
    "payload_family", "product", "environment",
    "required_privilege", "byovd", "validation_config", "is_baseline",
]


def main() -> int:
    ap = argparse.ArgumentParser(description="Enumerate the EDR-EvadeBench case matrix.")
    ap.add_argument("--out", type=Path, default=None,
                    help="write the matrix to this CSV path (default: print a summary only)")
    ap.add_argument("--baseline", action="store_true",
                    help="emit the 36 baseline cases (no evasion logic) instead of the 792 non-baseline cases")
    ap.add_argument("--technique", action="append", default=None,
                    help="restrict to a technique id (repeatable), e.g. --technique T7")
    ap.add_argument("--payload", action="append", default=None,
                    help="restrict to a payload family id (repeatable)")
    ap.add_argument("--product", action="append", default=None,
                    help="restrict to a product id (repeatable)")
    ap.add_argument("--environment", action="append", default=None,
                    help="restrict to an environment id (repeatable)")
    args = ap.parse_args()

    techniques = args.technique or TECHNIQUE_ORDER
    unknown = [t for t in techniques if t not in TECHNIQUES]
    if unknown:
        ap.error(f"unknown technique id(s): {', '.join(unknown)}")

    rows = enumerate_cases(
        techniques=techniques,
        payloads=args.payload or PAYLOAD_ORDER,
        products=args.product or PRODUCT_ORDER,
        environments=args.environment or ENVIRONMENT_ORDER,
        baseline=args.baseline,
    )

    if args.out:
        write_csv(args.out, FIELDS, rows)
        print(f"[+] wrote {len(rows)} cases to {args.out}")

    by_tech = Counter(r["technique_id"] for r in rows)
    print(f"[i] cases: {len(rows)}")
    print(f"[i] techniques: {len(by_tech)}")
    print(f"[i] payload families: {len(set(r['payload_family'] for r in rows))}")
    print(f"[i] products: {len(set(r['product'] for r in rows))}")
    print(f"[i] environments: {len(set(r['environment'] for r in rows))}")
    sizes = sorted(set(by_tech.values()))
    print(f"[i] cases per technique: {sizes[0] if len(sizes) == 1 else sizes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
