"""Shared helpers for the EDR-EvadeBench evaluation framework.

Standard library only, so the framework runs on a stock Python 3 with no
third-party packages installed.

This module is the single place where the paper's evaluation design is
translated into code:

  * the 22 techniques, their DET classification, required privilege and
    validation criteria          -> schema/techniques.json  (paper Table I, VII, Fig. 2)
  * payload families, environments, products, outcome levels, protocol
    constants                     -> schema/testbed.json     (paper Table VIII, Section III)
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

FRAMEWORK_DIR = Path(__file__).resolve().parent
REPO_ROOT = FRAMEWORK_DIR.parent
SCHEMA_DIR = FRAMEWORK_DIR / "schema"
RESULTS_DIR = REPO_ROOT / "results"

#: The five mutually exclusive prevention-stage levels (paper Section III-C).
LEVELS = ["L1", "L2", "L3", "L4", "L5"]

LEVEL_NAMES = {
    "L1": "Pre-execution Prevention",
    "L2": "Pre-C2 Prevention",
    "L3": "Pre-command Prevention",
    "L4": "Command-stage Prevention",
    "L5": "Operational Success",
}


def _load_json(path: Path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


TECH_SCHEMA = _load_json(SCHEMA_DIR / "techniques.json")
TESTBED = _load_json(SCHEMA_DIR / "testbed.json")

TECHNIQUES = {t["id"]: t for t in TECH_SCHEMA["techniques"]}
TECHNIQUE_ORDER = [t["id"] for t in TECH_SCHEMA["techniques"]]
LAYER1_ORDER = TECH_SCHEMA["layer1_stages"]
LAYER2_ORDER = TECH_SCHEMA["layer2_strategies"]

PRODUCTS = {p["id"]: p for p in TESTBED["products"]}
PRODUCT_ORDER = [p["id"] for p in TESTBED["products"]]

ENVIRONMENTS = {e["id"]: e for e in TESTBED["environments"]}
ENVIRONMENT_ORDER = [e["id"] for e in TESTBED["environments"]]

PAYLOADS = {p["id"]: p for p in TESTBED["payload_families"]}
PAYLOAD_ORDER = [p["id"] for p in TESTBED["payload_families"]]

PROTOCOL = TESTBED["protocol"]
OUTCOME_MODEL = TESTBED["outcome_model"]

#: Technique ids belonging to each Layer 2 strategy (paper Figure 2).
LAYER2_MEMBERS = {s: [t for t in TECHNIQUE_ORDER if TECHNIQUES[t]["layer2"] == s]
                  for s in LAYER2_ORDER}
#: Technique ids belonging to each Layer 1 stage (paper Figure 2).
LAYER1_MEMBERS = {s: [t for t in TECHNIQUE_ORDER if TECHNIQUES[t]["layer1"] == s]
                  for s in LAYER1_ORDER}


def case_id(technique_id: str, payload_id: str, product_id: str, environment_id: str) -> str:
    """Build the canonical case identifier, e.g. ``T1-CS-SOPH-W11``."""
    return "-".join([
        technique_id,
        PAYLOADS[payload_id]["short"],
        PRODUCTS[product_id]["short"],
        ENVIRONMENTS[environment_id]["short"],
    ])


def enumerate_cases(techniques=None, payloads=None, products=None, environments=None,
                    baseline: bool = False) -> list[dict]:
    """Enumerate the evaluation case matrix.

    The full matrix is 22 techniques x 3 payload families x 6 products x
    2 environments = 792 cases, matching the paper's non-baseline outcome
    count. ``baseline=True`` emits the 36 baseline cases instead -- the
    AES-protected payload with no additional evasion logic, i.e. three payload families x
    six products x two environments (paper Section IV-A).
    """
    payloads = payloads or PAYLOAD_ORDER
    products = products or PRODUCT_ORDER
    environments = environments or ENVIRONMENT_ORDER

    if baseline:
        rows = []
        for pl in payloads:
            for pr in products:
                for env in environments:
                    rows.append({
                        "case_id": case_id("T0", pl, pr, env),
                        "technique_id": "T0",
                        "technique_name": "AES-protected Baseline Payload (no additional evasion logic)",
                        "layer1": "",
                        "layer2": "",
                        "payload_family": pl,
                        "product": pr,
                        "environment": env,
                        "required_privilege": "standard-user",
                        "byovd": False,
                        "validation_config": "clean-baseline",
                        "is_baseline": True,
                    })
        return rows

    techniques = techniques or TECHNIQUE_ORDER
    rows = []
    for t in techniques:
        spec = TECHNIQUES[t]
        for pl in payloads:
            for pr in products:
                for env in environments:
                    rows.append({
                        "case_id": case_id(t, pl, pr, env),
                        "technique_id": t,
                        "technique_name": spec["name"],
                        "layer1": spec["layer1"],
                        "layer2": spec["layer2"],
                        "payload_family": pl,
                        "product": pr,
                        "environment": env,
                        "required_privilege": spec["privilege"],
                        "byovd": spec["byovd"],
                        "validation_config": spec["validation_config"],
                        "is_baseline": False,
                    })
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_csv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def counts_by_level(rows: list[dict], level_key: str = "level") -> dict[str, int]:
    """Count rows per level, always returning all five keys."""
    counts = {lvl: 0 for lvl in LEVELS}
    for row in rows:
        lvl = row[level_key]
        if lvl not in counts:
            raise ValueError(f"unknown outcome level: {lvl!r}")
        counts[lvl] += 1
    return counts


def distribution(counts: dict[str, int]) -> dict[str, float]:
    """Normalise counts into a five-element distribution (paper Eq. 1 / Eq. 2)."""
    total = sum(counts.values())
    if total == 0:
        return {lvl: 0.0 for lvl in LEVELS}
    return {lvl: counts[lvl] / total for lvl in LEVELS}
