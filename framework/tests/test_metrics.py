#!/usr/bin/env python3
"""Self-checks for the EDR-EvadeBench framework.

Run with either:

    python framework/tests/test_metrics.py
    python -m unittest discover -s framework/tests

The suite checks that the 22 technique README distributions and the released case-level matrix reproduce the paper aggregates. No unresolved discrepancies are currently permitted.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

FRAMEWORK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FRAMEWORK))
sys.path.insert(0, str(FRAMEWORK / "tools"))

from common import (  # noqa: E402
    LAYER1_ORDER, LEVELS, PAYLOAD_ORDER, PRODUCT_ORDER, RESULTS_DIR,
    TECHNIQUE_ORDER, enumerate_cases, read_csv,
)
import build_results_from_readmes as build  # noqa: E402
import metrics  # noqa: E402
import score  # noqa: E402
import validate  # noqa: E402


class TestValidationGate(unittest.TestCase):
    """Stage 2 requires exactly one result for each validation stage."""

    def test_single_pass_row_does_not_admit_techniques(self):
        rows = [{"technique_id": t, "stage": "evasion_logic", "status": "pass"}
                for t in TECHNIQUE_ORDER]
        admitted, rejected, incomplete = validate.check(rows)
        self.assertEqual(admitted, [])
        self.assertEqual(rejected, [])
        self.assertEqual(incomplete, TECHNIQUE_ORDER)

    def test_duplicate_stage_does_not_replace_missing_stage(self):
        rows = []
        for t in TECHNIQUE_ORDER:
            rows.extend([
                {"technique_id": t, "stage": "evasion_logic", "status": "pass"},
                {"technique_id": t, "stage": "evasion_logic", "status": "pass"},
            ])
        admitted, _, incomplete = validate.check(rows)
        self.assertEqual(admitted, [])
        self.assertEqual(incomplete, TECHNIQUE_ORDER)

    def test_both_passed_stages_admit_techniques(self):
        rows = []
        for t in TECHNIQUE_ORDER:
            rows.extend([
                {"technique_id": t, "stage": "evasion_logic", "status": "pass"},
                {"technique_id": t, "stage": "payload_functionality", "status": "pass"},
            ])
        admitted, rejected, incomplete = validate.check(rows)
        self.assertEqual(admitted, TECHNIQUE_ORDER)
        self.assertEqual(rejected, [])
        self.assertEqual(incomplete, [])


class TestScoring(unittest.TestCase):
    """L5 requires coherent command counts and an explicitly live session."""

    @staticmethod
    def row(**changes):
        row = {
            "process_created": "true",
            "process_terminated_by_product": "false",
            "c2_beacon_observed": "true",
            "commands_sent": "4",
            "commands_completed": "4",
            "session_alive_at_end": "true",
        }
        row.update(changes)
        return row

    def test_l5_requires_session_alive_at_end(self):
        level, status, _ = score.score_row(self.row(session_alive_at_end=""))
        self.assertIsNone(level)
        self.assertEqual(status, "ambiguous")

    def test_completed_cannot_exceed_sent(self):
        level, status, _ = score.score_row(self.row(commands_completed="5"))
        self.assertIsNone(level)
        self.assertEqual(status, "ambiguous")

    def test_coherent_completed_commands_and_live_session_are_l5(self):
        self.assertEqual(score.score_row(self.row())[0], "L5")


class TestCaseMatrix(unittest.TestCase):
    """Stage 1: the case matrix must match the paper's design."""

    def test_full_matrix_size(self):
        rows = enumerate_cases()
        self.assertEqual(len(rows), 792,
                         "22 techniques x 3 payloads x 6 products x 2 environments")

    def test_cases_per_technique(self):
        rows = enumerate_cases()
        per = {t: sum(1 for r in rows if r["technique_id"] == t) for t in TECHNIQUE_ORDER}
        self.assertEqual(set(per.values()), {36})

    def test_case_ids_unique(self):
        rows = enumerate_cases()
        self.assertEqual(len({r["case_id"] for r in rows}), len(rows))

    def test_baseline_matrix(self):
        rows = enumerate_cases(baseline=True)
        self.assertEqual(len(rows), 36, "six products x three payloads x two environments")


class TestReconstruction(unittest.TestCase):
    """The README tables must invert cleanly to integer counts."""

    @classmethod
    def setUpClass(cls):
        cls.result = build.collect()

    def test_level_counts_sum_to_36(self):
        for t, counts in self.result["tech_counts"].items():
            self.assertEqual(sum(counts), 36, f"{t} BDD does not sum to 36")

    def test_product_marginals_sum_to_technique_l5(self):
        for t in TECHNIQUE_ORDER:
            self.assertEqual(sum(self.result["by_product"][t]),
                             self.result["tech_counts"][t][4],
                             f"{t} per-product L5 counts do not sum to its L5 total")

    def test_payload_marginals_sum_to_technique_l5(self):
        for t in TECHNIQUE_ORDER:
            self.assertEqual(sum(self.result["by_payload"][t]),
                             self.result["tech_counts"][t][4],
                             f"{t} per-payload L5 counts do not sum to its L5 total")

    def test_total_outcomes_and_l5(self):
        self.assertEqual(self.result["total_outcomes"], 792)
        self.assertEqual(self.result["total_l5"], 182)


class TestPaperAggregates(unittest.TestCase):
    """Every stated aggregate must reconcile, bar the pinned discrepancies."""

    @classmethod
    def setUpClass(cls):
        cls.result = build.collect()
        cls.failing = {area: (exp, act)
                       for area, exp, act, ok in cls.result["checks"] if not ok}

    def test_only_documented_discrepancies_fail(self):
        self.assertEqual(
            set(self.failing), set(build.KNOWN_DISCREPANCIES),
            "the set of failing cross-checks changed; if this is a new "
            "discrepancy, investigate it and document it in results/README.md"
        )

    def test_all_cross_checks_pass(self):
        self.assertEqual(
            self.failing, {},
            f"unreconciled cross-checks against the paper: {sorted(self.failing)}"
        )

    def test_documented_discrepancy_pins_still_hold(self):
        """Guards any future pinned discrepancy; vacuous while the dict is empty."""
        for area, (exp, act) in build.KNOWN_DISCREPANCIES.items():
            self.assertIn(area, self.failing, f"{area} no longer fails; drop the pin")
            got_exp, got_act = self.failing[area]
            self.assertEqual(got_exp, str(exp), f"{area}: expected-value pin moved")
            self.assertEqual(got_act, str(act), f"{area}: reconstructed value moved")

    def test_every_check_reconciles(self):
        total = len(self.result["checks"])
        self.assertGreater(total, 20, "expected a meaningful number of cross-checks")
        self.assertEqual(total - len(self.failing), total)

    def test_overall_l5_rate(self):
        rate = round(self.result["total_l5"] / self.result["total_outcomes"] * 100, 1)
        self.assertEqual(rate, build.PAPER_EXPECT["overall_l5_rate"])


class TestMetricsOutputs(unittest.TestCase):
    """If metrics.py has been run, its output must be well formed."""

    def setUp(self):
        self.metrics = RESULTS_DIR / "metrics"
        if not (self.metrics / "bdd_layer2.csv").exists():
            self.skipTest("run `python framework/metrics.py` first")

    def test_every_distribution_sums_to_one(self):
        for name in ("bdd_technique.csv", "bdd_layer1.csv", "bdd_layer2.csv"):
            for row in read_csv(self.metrics / name):
                total = sum(float(row[lvl]) for lvl in LEVELS)
                self.assertAlmostEqual(total, 1.0, places=5, msg=f"{name}: {row['group']}")

    def test_layer1_has_all_stages(self):
        groups = {r["group"] for r in read_csv(self.metrics / "bdd_layer1.csv")}
        self.assertEqual(groups, set(LAYER1_ORDER))

    def test_psd_l5_matches_paper_per_product(self):
        path = self.metrics / "psd_by_product_l5_only.csv"
        if not path.exists():
            self.skipTest("PSD L5-only file not present")
        rows = {r["product"]: float(r["L5"]) for r in read_csv(path)}
        for product, expected in build.PAPER_EXPECT["per_product_l5"].items():
            self.assertAlmostEqual(rows[product] * 100, expected, places=1)

    def test_table3_has_layer2_payload_rates(self):
        path = self.metrics / "l5_by_layer2_payload.csv"
        self.assertTrue(path.exists(), "run `python framework/metrics.py` first")
        rows = read_csv(path)
        self.assertEqual(len(rows), 18)
        actual = {(r["layer2"], r["payload_family"]): round(float(r["L5"]) * 100, 1)
                  for r in rows}
        for strategy, expected in build.PAPER_EXPECT["layer2_by_payload_l5"].items():
            for payload, rate in zip(PAYLOAD_ORDER, expected):
                self.assertEqual(actual[strategy, payload], rate)

    def test_table3_computation_from_marginals(self):
        rows = read_csv(RESULTS_DIR / "by_payload.csv")
        self.assertEqual(len(metrics.l5_by_layer2_payload(rows)), 18)


class TestPaperOutcomes(unittest.TestCase):
    """If the case-level outcome matrix is present, it must reproduce the paper."""

    def setUp(self):
        self.path = RESULTS_DIR / "outcomes_scored.csv"
        if not self.path.exists():
            self.skipTest("results/outcomes_scored.csv not present")

    def _rows(self):
        rows = []
        for r in read_csv(self.path):
            r = dict(r)
            r["is_baseline"] = str(r.get("is_baseline", "")).strip().lower() == "true"
            rows.append(r)
        return rows

    def test_shape_and_baseline(self):
        rows = self._rows()
        self.assertEqual(len(rows), 828, "792 non-baseline + 36 baseline")
        baseline = [r for r in rows if r["is_baseline"]]
        self.assertEqual(len(baseline), 36)
        self.assertEqual({r["level"] for r in baseline}, {"L1"},
                         "the paper reports all 36 baseline outcomes as L1")

    def test_case_ids_unique(self):
        rows = self._rows()
        self.assertEqual(len({r["case_id"] for r in rows}), len(rows))

    def test_reproduces_every_paper_aggregate(self):
        import import_outcomes
        self.assertEqual(import_outcomes.verify(self._rows()), [])


class TestCaseEnumerationFiles(unittest.TestCase):
    """If the CSVs have been generated, they must agree with the code."""

    def test_cases_csv(self):
        path = RESULTS_DIR / "cases.csv"
        if not path.exists():
            self.skipTest("run `python framework/cases.py --out results/cases.csv` first")
        rows = read_csv(path)
        self.assertEqual(len(rows), 792)
        self.assertEqual(len({r["case_id"] for r in rows}), 792)


if __name__ == "__main__":
    unittest.main(verbosity=2)
