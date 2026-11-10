# EDR-EvadeBench Framework

This directory is the **operational core of the four-stage evaluation
framework** described in Section 3 of the companion paper. The technique
directories (`T1_…`–`T22_…`) are the *sample library*; this directory is the
*framework* that turns a library of samples into a reproducible, scored,
comparable evaluation.

Everything here is standard-library Python 3 — no third-party packages.

## Four stages → artifacts

| Stage | Paper description | What implements it here |
| :--- | :--- | :--- |
| **1. Sample Generation** | three C2-derived payload families; unified AES-based encryption; evasion-logic integration | [`cases.py`](cases.py) enumerates the case matrix (22 × 3 × 6 × 2 = 792, plus 36 baseline). Payload *content* is supplied by the evaluator — see [../REPRODUCIBILITY.md](../REPRODUCIBILITY.md). |
| **2. Function Validation** | evasion-logic verification + payload-functionality check, acting as a quality gate | [`validate.py`](validate.py) generates the per-technique checklist from Table 7 and enforces the gate: a sample is admitted only when every applicable check passes. |
| **3. Sample Execution** | snapshot reset, 60 s beacon window, 5 min pre-command and 5 min post-command observation, repetition to five consecutive identical outcomes | **Deliberately manual.** [`runbook.md`](runbook.md) specifies the procedure precisely; it is not scripted (see below). |
| **4. Effectiveness Evaluation** | five-tiered outcome model; PSD and BDD metrics | [`score.py`](score.py) applies the L1–L5 decision procedure to structured evidence; [`metrics.py`](metrics.py) computes PSD (Eq. 1) and BDD (Eq. 2); [`figures.py`](figures.py) optionally renders data-equivalent SVG figures. |

## Machine-readable design

| File | Contents |
| :--- | :--- |
| [`schema/techniques.json`](schema/techniques.json) | The 22 techniques: id, name, DET Layer 1 stage, DET Layer 2 strategy, required privilege, BYOVD flag, validation configuration, success criterion, and any divergence between the paper's definition and the released source. This is Table 1 + Table 7 + Figure 2 in machine-readable form. |
| [`schema/testbed.json`](schema/testbed.json) | Payload families, environments, products and their versions, hardware, network, the five outcome levels with their definitions, and the protocol constants (windows, command set, repetition rule, snapshot policy). This is Table 8 + Section 3. |

JSON is used rather than YAML so the framework runs on a stock Python 3.

## Quick start

```bash
# Stage 1 — enumerate the case matrix
python framework/cases.py --out results/cases.csv

# Stage 2 — create the validation checklist, fill it in, then run the gate
python framework/validate.py init
python framework/validate.py check

# Stage 3 — run the experiment by hand, following the runbook
#            (one row of evidence per case; see the template below)

# Stage 4 — score, measure, plot
python framework/score.py template --out results/evidence.csv
python framework/score.py run --in results/evidence.csv --out results/outcomes_scored.local.csv
python framework/metrics.py --outcomes results/outcomes_scored.local.csv --outdir results/metrics/local
python framework/figures.py --metrics results/metrics/local --outdir results/figures/generated/local
```

## Reproducing the paper's reported metrics

`results/outcomes_scored.csv` is the canonical matrix: 828 rows (792 non-baseline and 36 baseline). [Readable results](../results/FINAL_RESULTS.md) and [case summaries](../results/CASE_SUMMARIES.md) are generated from it using the same repository IDs. The common [test protocol](TEST_PROTOCOL.md) documents versions, settings and the public/internal material boundary. The per-technique README tables provide an independent aggregate cross-check:

```bash
python framework/tools/export_results.py                    # case-derived readable materials and summaries
python framework/tools/build_results_from_readmes.py --check # independent README cross-check
python framework/metrics.py                                 # PSD / BDD / prevention
python framework/figures.py                                 # optional regenerated SVG equivalents
python framework/tests/test_metrics.py                      # self-checks
```

The original matrix and reconstructed marginals reproduce the paper's Layer 1 BDD (Table 4), Layer 2 BDD
(Figure 5), Table 3, the full per-product PSD (Figure 4), the per-product
prevention rates (Figure 6), the overall L5 rate, and the per-product and
per-payload L5 rates — **all 27 cross-checks pass**.

The matrix checker requires the result to reproduce every paper aggregate
*and* every per-technique README distribution. The first run of the checker
also found that T20 and T21 were
assigned to the wrong Layer 2 strategies; the paper's Figure 2 determined the
correction, recorded in [`../CHANGELOG.md`](../CHANGELOG.md) and
[`../results/README.md`](../results/README.md).

## What is deliberately *not* automated

Three parts of Stage 3 are intentionally left manual, because automating them
would produce something unportable that looks authoritative without being
reliable:

- **Snapshot orchestration.** Reverting the target VM and the C2 VM before
  every execution depends on the hypervisor. The paper used VMware Workstation
  17 Pro; a script for it would not run anywhere else.
- **C2 operation.** Establishing the listener, sending the command set, and
  reading back the console is specific to the framework in use (Cobalt Strike,
  Havoc, AdaptixC2) and to the infrastructure.
- **Product alert collection.** Reading alerts and protection events out of a
  management console is vendor-specific, and several of those consoles have no
  supported local export path.

`score.py` stops at the same boundary: it does not infer outcomes from raw
logs. It applies the paper's decision procedure to evidence a reviewer has
already recorded, and refuses to score cases whose evidence is internally
inconsistent.

## Layout

```
framework/
├── README.md                  this file
├── runbook.md                 the four-stage operational procedure
├── TEST_PROTOCOL.md           common test protocol and public settings
├── common.py                  shared schema loading and helpers
├── cases.py                   Stage 1 — case matrix
├── validate.py                Stage 2 — two-stage validation and quality gate
├── score.py                   Stage 4a — L1–L5 decision procedure
├── metrics.py                 Stage 4b — PSD and BDD
├── figures.py                 optional data-equivalent SVG renderer
├── schema/
│   ├── techniques.json        Table 1 + Table 7 + Figure 2
│   └── testbed.json           Table 8 + Section 3 constants
├── templates/                 evidence templates for Stages 2 and 3
├── tools/
│   ├── export_results.py              case-derived result materials
│   ├── import_outcomes.py              maintainer normalization/check utility
│   └── build_results_from_readmes.py   reconstruct results/ and cross-check
└── tests/
    └── test_metrics.py        self-checks
```
