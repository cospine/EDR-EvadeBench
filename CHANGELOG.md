# Changelog

All notable changes to this artifact are recorded here. The repository is
versioned alongside the companion paper.

## 2026-11-10 - final mechanism-description alignment

- Aligned the T20 validation schema, template and README with PE icon and product/version resource masquerading, rather than payload extraction from a resource section.
- Removed T21-specific API-trace conditions from the T19 README.
- No implementation code, final case label or metric value changed.

## 2026-11-10 - publication artifact cleanup

- Aligned T3's display name, description and validation criterion with the current manuscript; retained the existing directory path for compatibility. No outcome level or sample implementation changed.
- Refreshed the case-register exports, test templates, statistics and source fingerprints; recorded release version 2026-11-10.
- Replaced owner-facing documentation tasks with final release text, filled the verified UPX/Resource Hacker version metadata, and added the security contact.
- Removed broken upstream image references and corrected outdated table references and result interpretations.
- Moved the Resource Hacker executable outside the public repository; it is an external dependency obtained from its publisher. Retained the example resource and auxiliary drivers as requested.

## 2026-11-10 - static delivery and build-documentation audit

- Audited all 22 technique directories, 8 Visual Studio solutions and 14 project files; expanded BUILD.md with source/project entries, declared dependencies, component-specific status and remaining release checks.
- Distinguished earlier reported/partial compilation checks from this static review. No evasion sample was compiled or executed; no source, project, binary or experimental result was modified.
- Corrected T1's missing-dependency description: the actual generator uses standard-library imports and requires absent data/templates, rather than absent `enums/` or `utils/` modules.
- Recorded T13 resource/precompiled-header observations, external dependency gaps, current auxiliary-tool version metadata and the existing T3 source/paper mismatch.
- Distinguished experimental code from documented later packaging changes; did not claim that the public package is an unchanged experimental archive.

## 2026-11-07 — integrated test materials and results

- Matched all 828 existing case labels individually to the manuscript-derived result package; no final outcome changed.
- Kept `results/outcomes_scored.csv` as the single source of labels and retained the existing framework, statistical plots and per-technique result tables.
- Added readable final results, 276 case-summary records, a data dictionary, source fingerprints, and a common test protocol. `framework/tools/export_results.py` generates the readable materials and integer summaries from the canonical CSV.
- Removed internal workbook locators/redundant codes from the public CSV and concrete network addresses from the testbed schema. Original screenshots and full logs remain internal.
- Aligned title, default product configuration, AES-protected T0, planned future maintenance and reproducibility statements with the current manuscript.
- Preserved auxiliary scoring/validation templates for new evaluations; no sample implementation or payload was executed or modified in this integration.

## [Unreleased] — packaging pass for public release

Documentation and correctness pass to make the repository consistent with the
paper and directly usable by an evaluator. No change alters an evasion
mechanism or the reported outcome distributions.

### Added

- `REPRODUCIBILITY.md` — explicit statement of what can and cannot be
  reproduced from this repository, and what an evaluator must supply.
- `BUILD.md` — per-technique build matrix, source-specific commands and
  external dependencies.
- `BINARY_PROVENANCE.md` — size, SHA-256, identification and provenance for
  every committed binary, including the two kernel drivers.
- `THIRD_PARTY_NOTICES.md` — upstream projects, paper references, and
  attribution status.
- `SECURITY.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`.
- `.gitignore` — build outputs, generated SysWhispers files, restored
  packages, and the OLLVM build tree.

### Fixed

- Require exactly one evasion-logic row and one payload-functionality row per
  technique before the validation gate can admit it.
- Require coherent command counts and an explicitly live session before an
  outcome can be scored L5.
- Correct the swapped Sophos and Elastic version metadata from Table 8.
- Keep evaluator-generated outcomes, metrics, and figures separate from the
  released paper results by default.
- Emit the actual Layer 2-by-payload Table 3 and give the overall payload
  summary a distinct filename.
- Keep optional regenerated SVG figures separate from the original paper PDFs.

### Added — the four-stage framework itself

The paper's Contribution 2 is a four-stage framework, but the repository
previously shipped only the sample library. The framework's operational core
is now implemented, in standard-library Python 3 (no third-party packages):

- `framework/cases.py` — Stage 1: enumerates the case matrix
  (22 × 3 × 6 × 2 = 792, plus 36 baseline).
- `framework/validate.py` — Stage 2: generates the two-stage validation
  checklist from Table 7 and enforces the quality gate.
- `framework/score.py` — Stage 4a: applies the paper's L1–L5 decision
  procedure to structured evidence, and refuses to score cases whose evidence
  is internally inconsistent.
- `framework/metrics.py` — Stage 4b: PSD (Eq. 1) and BDD (Eq. 2), by
  technique, Layer 1 stage, Layer 2 strategy, payload family and product.
- `framework/figures.py` — renders optional data-equivalent figures as SVG; the five
  ordinal levels use a single-hue ramp validated for both light and dark
  surfaces.
- `framework/schema/techniques.json` — Table 1 + Table 7 + Figure 2,
  machine-readable, including each technique's required privilege, validation
  configuration and success criterion.
- `framework/schema/testbed.json` — Table 8 + the Section 3 protocol
  constants (windows, command set, repetition rule, snapshot policy) and the
  five outcome levels with their definitions.
- `framework/runbook.md` — the operational procedure for all four stages.
- `framework/templates/` — Stage 2 and Stage 3 record templates.
- `framework/tests/test_metrics.py` — framework and result self-checks.
- `results/` — released outcome data, metrics and figures, with its own
  README describing provenance and limits.

Stage 3 (execution) is intentionally **not** scripted: snapshot
orchestration, C2 operation and product alert collection are all
environment- or vendor-specific. `framework/runbook.md` specifies the
procedure precisely and states why.

### Added — released result data

`results/technique_level.csv`, `results/by_product.csv` and
`results/by_payload.csv` are reconstructed losslessly from the outcome tables
in the 22 technique READMEs (every reported percentage is an exact multiple of
1/36, 1/6 or 1/12 rounded to 0.1%, so the integer counts are recoverable).
`framework/tools/build_results_from_readmes.py` rebuilds them and cross-checks
them against every aggregate stated in the paper.

### Added — the case-level outcome matrix, and the figures it unlocks

The paper's original case-level results were added to the repository,
completing the result data:

- `results/outcomes_scored.csv` — the released matrix of 828 original results
  (792 non-baseline + 36 baseline), checked against every paper aggregate and
  every per-technique README distribution.
- `framework/metrics.py` — now computes the **full per-product PSD** (all five
  levels) and `prevention_by_stage.csv` (the data behind Figure 6); it also
  resolves Layer 1/2 membership from the schema, so any outcome file carrying
  a technique id works.
- The original **Figures 4, 5 and 6** are included as PDF files, while
  `framework/figures.py` can render data-equivalent SVG alternatives under
  `results/figures/generated/`.
- New tests: the original matrix must reproduce the paper and the READMEs.

Verified: the full PSD reproduces every Figure-4 number the paper states —
Sophos L2 77.3% and L1+L2 95.5%, Bitdefender L2 81.8%, Kaspersky 27.3/41.7/
16.7, Elastic L1 66.7% and L5 9.1%, Huorong L1 18.2% and L5 57.6%, Microsoft
Defender Antivirus 16.7/5.3/18.2.

### Fixed — the Layer 2 classification of T20 and T21 was swapped

The framework's cross-checker found two rows that did not reconcile: the
Layer 2 BDD for **Obfuscation** and for **Logic Bypass**. Both are now fixed,
and the paper determined the answer.

Figure 2 of the paper places **PE Resource Masquerading (T20) in the
Obfuscation column** and **API-level Behavioral Obfuscation (T21) in the Logic
Bypass column**. The repository had the two swapped. Corrected in:

- the root README's technique table,
- `framework/schema/techniques.json`,
- `T20_PE Resource Masquerading/README.md` and
  `T21_API-level Behavioral Obfuscation/README.md` (their DET classification
  lines).

No outcome data changed — only the group each technique is aggregated into.
Only the L1/L2/L3 split of those two strategies was affected. With the mapping
corrected, the per-technique tables reproduce the paper exactly:

| Strategy | Members | n | L1 | L2 | L3 | L4 | L5 |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Obfuscation | T17, T18, T19, **T20** | 144 | 37.5% | 39.6% | 6.2% | 0.0% | 16.7% |
| Logic Bypass | **T21**, T22 | 72 | 16.7% | 47.2% | 11.1% | 0.0% | 25.0% |

The cross-checker now reports **27 of 27 checks passing**, and
`framework/tests/test_metrics.py` asserts that zero fail.

Note for readers holding the earlier mapping: in the previous packaging pass
T20 was listed under Logic Bypass and T21 under Obfuscation.

### Fixed (portability / correctness — behaviour unchanged)

- **T2** (`amsi-etw-patch.cpp`): cast `FARPROC` to `LPVOID`/`void*` at the
  three `VirtualProtect`/`memcpy` call sites. The previous code compiled only
  under MSVC's permissive implicit conversion; it now also builds with GCC.
- **T22**: renamed `IHxHelpPaneServer.c` → `IHxHelpPaneServer.cpp`. The file
  contains C++ (an interface declaration with virtual methods and
  `__declspec(uuid)`), so the `.c` extension was incorrect and the file
  could not compile as C. Added error handling for `CLSIDFromString`,
  `CoInitializeEx`, `CoCreateInstance`, and `Execute`, and bounds-checked the
  path formatting.
- **T22**: `SWprintf_s` call given an explicit buffer size, so it compiles
  under both MSVC and GCC.

### Documentation corrections

- **T2** README: the ETW component patches `NtTraceEvent`, not
  `EtwEventWrite` as previously stated. The AMSI byte offset (`+0x83`) is
  documented as build-dependent.
- **T3** README: the shipped source sets the
  `BLOCK_NON_MICROSOFT_BINARIES` process-mitigation policy; it does not
  itself disable DLL signature verification. The divergence from the paper's
  T3 definition is now stated explicitly.
- **T6/T8** READMEs: no prebuilt executables are distributed; the
  `*.exe` names are build outputs.
- **T7** README and script: the script no longer reboots automatically by
  default and no longer ships an unsubstituted target path as if runnable.
- **T13**: upstream ImmoralFiber documentation separated from the
  benchmark's own documentation; the upstream Windows 10 build-19044 test
  note is no longer presented next to the benchmark's Windows 11 / Server
  2025 environment.
- Root README: added a reproducibility-scope statement, corrected the
  binaries policy, and added links to the new documents.

## [Paper submission] — initial artifact

- 22 technique directories (`T1`–`T22`) with source, build files, and a
  per-technique README reporting the paper's outcome distributions.
- Root README describing the DET Matrix, the four-stage workflow, the
  five-tiered outcome model, and the headline results.
