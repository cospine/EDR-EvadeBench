# Reported Results and Test Materials

The manuscript is the authority for the reported outcomes. This directory contains **all 828 final case labels**, consisting of 792 non-baseline cases and 36 T0 cases. They have been matched individually against the manuscript result table. Source code remains in the technique directories; the common test protocol is in [framework/TEST_PROTOCOL.md](../framework/TEST_PROTOCOL.md).

## Start here

| File | Purpose |
| --- | --- |
| [FINAL_RESULTS.md](FINAL_RESULTS.md) | Complete readable register, PSD/BDD, DET membership and other summaries |
| [outcomes_scored.csv](outcomes_scored.csv) | Canonical machine-readable labels; the single data source for exports and metrics |
| [CASE_SUMMARIES.md](CASE_SUMMARIES.md) | Final-outcome descriptions for 828 cases in 276 product/environment records |
| [DATA_DICTIONARY.md](DATA_DICTIONARY.md) | Actual CSV fields, repository IDs, counting rules and privacy scope |
| [PROVENANCE.json](PROVENANCE.json) | Manuscript-table and dataset fingerprints |
| [metrics/](metrics/) | Full PSD, implementation/DET/environment BDD and other computed tables |
| [technique_level.csv](technique_level.csv), [by_product.csv](by_product.csv), [by_payload.csv](by_payload.csv) | Integer summaries generated from the canonical case data |
| [consistency_report.md](consistency_report.md) | Independent cross-checks against per-technique README tables and paper aggregates |
| [figures/](figures/) | Original paper plots; these are statistical figures, not experiment screenshots |

`cases.csv` is a generated 792-case design list. `validation.template.csv` and `evidence.template.csv` are blank templates for new evaluations, not records from the reported experiments.

## Recompute and verify

Run from the repository root; only standard-library Python is required:

```bash
python framework/tools/export_results.py
python framework/metrics.py
python framework/tools/export_results.py --check
python framework/tools/build_results_from_readmes.py --check
python -m unittest discover -s framework/tests
```

The expected total is 182 L5 outcomes among 792 non-baseline cases (23.0% rounded). The scripts also compute the complete product PSD, implementation and DET BDD, payload/environment distributions, Layer 2-by-payload L5 rates, and prevention rates by product and detection-lifecycle stage. The original plots remain available; `python framework/figures.py` optionally renders data-equivalent SVGs.

`export_results.py` derives the readable materials and integer summaries from `outcomes_scored.csv`. The README reconstruction utility provides an independent check of the 22 technique distributions; it does not determine individual case labels. Historical corrections to T20/T21 classification are recorded in [CHANGELOG.md](../CHANGELOG.md).

## Public and internal materials

Original screenshots, full logs and the internal notebook are retained internally because they contain sensitive experimental-environment information. This release provides final outcomes, the test protocol and calculation tools. It supports checking the reported data and recomputing statistics, without distributing complete historical per-execution traces. See [REPRODUCIBILITY.md](../REPRODUCIBILITY.md).

## New evaluations

Keep new evidence and results in local files, such as `results/evidence.local.csv` and `results/outcomes_scored.local.csv`. Use `framework/metrics.py --outcomes results/outcomes_scored.local.csv --outdir results/metrics/local`. Do not overwrite the published outcome matrix. The evaluation procedure and template usage are documented in [the runbook](../framework/runbook.md).
