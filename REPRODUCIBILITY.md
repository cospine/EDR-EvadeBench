# Reproducibility Scope

This repository accompanies **EDR-EvadeBench: A Framework for Evaluating EDR Evasion Techniques and Defenses**. It combines implementation source projects, a documented evaluation workflow, complete reported case-level results and analysis tools.

## What the release supports

| Task | Materials and scope |
| --- | --- |
| Inspect implementation source | Technique directories T1-T22; third-party components and attribution are documented separately |
| Compile implementations | Per-technique instructions and [BUILD.md](BUILD.md); build coverage and external dependencies are stated there |
| Read all reported outcomes | [results/FINAL_RESULTS.md](results/FINAL_RESULTS.md) and canonical [outcomes_scored.csv](results/outcomes_scored.csv): 828 labels, including 36 T0 cases |
| Understand case outcomes | [results/CASE_SUMMARIES.md](results/CASE_SUMMARIES.md), using the manuscript L1-L5 criteria |
| Recalculate statistics | `python framework/tools/export_results.py` and `python framework/metrics.py`; no payload or security product is needed for these calculations |
| Conduct a new evaluation | [Test protocol](framework/TEST_PROTOCOL.md), [runbook](framework/runbook.md), schemas, validation and scoring tools; requires the evaluator's payloads and product access |
| Inspect complete historical execution traces | Original screenshots and full logs are retained internally and are not publicly distributed |

## Results and experimental execution

The canonical dataset has one final label per implementation-payload-product-environment combination. All 828 labels were checked against the manuscript result table; the 792 non-baseline cases are used for PSD and BDD. Derived tables and case summaries use the same repository IDs and are generated from that CSV. The calculation definitions, field names and source fingerprints are documented in [results/](results/README.md).

Recomputing metrics from the supplied final labels verifies the numerical summaries. Repeating the experimental protocol is a separate activity and does not guarantee identical outcomes: payload details, product versions, configurations and cloud services may change. Per-technique README results describe the manuscript experiments, not a fresh measurement of the distributed placeholder payloads.

## Public configuration and internal information

Product versions, default protection configurations, framework versions, the 60-second C2 establishment timeout, both five-minute observation windows, snapshot controls and repetition rule are documented in [framework/TEST_PROTOCOL.md](framework/TEST_PROTOCOL.md) and the manuscript. Framework sources and preparation settings are described in manuscript Appendix B. T0 uses the same AES-based encryption and runtime decryption as the other samples without an additional evasion mechanism.

Original screenshots, full logs and the internal notebook contain sensitive environment information and remain internal. The public materials omit concrete network addresses, host/account identifiers, raw management-console exports, credentials, encryption keys, payload binaries and raw shellcode. This statement concerns public availability; it does not assert that the experiments or internal records are absent.

The released code uses placeholder payload data. An evaluator must provide payloads compatible with the source project's expected encryption/buffer format, the corresponding keys, isolated C2 infrastructure, the required privileges, and access to the products. [BUILD.md](BUILD.md) and per-technique READMEs describe the code-specific prerequisites. Those source-format requirements should not be mistaken for additional verified parameters of every historical payload.

The bundled auxiliary tools and drivers are documented in [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Original statistical plots in `results/figures/` remain public; they do not contain the withheld screenshots or full logs. Blank evidence and validation templates are for newly conducted evaluations.

## Verification

```bash
python framework/tools/export_results.py --check
python framework/tools/build_results_from_readmes.py --check
python -m unittest discover -s framework/tests
```

For build problems, follow [CONTRIBUTING.md](CONTRIBUTING.md). Releasing this integrated local repository is separate from uploading or pushing it to a hosting service.
