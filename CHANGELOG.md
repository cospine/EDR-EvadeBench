# Changelog

Changes to the research artifact are recorded below. The reported experimental
outcomes are unchanged by the release preparation.

## 2026-11-10 - artifact release

### Materials and documentation

- Provide source projects, scripts, resources, and preparation instructions for
  the 22 selected implementations, with external dependencies listed in BUILD.md.
- Provide the complete 828-case outcome matrix, final-result register, case
  summaries, test protocol, and calculation tools for PSD, BDD, and the reported
  summaries. The dataset remains the source for generated result files.
- Include reproducibility, build, binary-provenance, attribution, security, and
  contribution documentation. Retain third-party license texts in LICENSES/;
  LICENSE applies only to the authors' own contributions.
- Describe the package as research materials and distinguish source-based samples
  from scripts and tool-based preparation. Resource Hacker is obtained separately
  from its publisher; UPX remains a bundled auxiliary tool.
- Document the default product configurations, AES-protected T0, observation
  windows, repetition rule, and snapshot controls. Monthly collection, GPT-4o
  ranking, and expert review remain future maintenance plans.

### Alignment with the manuscript

- Use DLL Signature Restriction as T3's display name and validation criterion.
  Keep the existing T3 directory name for path compatibility.
- Describe T20 as PE icon and product/version resource masquerading. Place T20
  under Obfuscation and T21 under Logic Bypass in the DET mapping.
- Remove T21-specific API-trace conditions from the T19 README.
- Align table references, technique descriptions, product versions, and result
  interpretations with the manuscript.

### Packaging changes

- Keep original screenshots, full logs, concrete environment identifiers,
  operational payloads, and payload keys outside the public materials.
- Replace public payload buffers and designated binary inputs with placeholders;
  record the identities and hashes of retained auxiliary binaries.
- Retain earlier portability changes: explicit pointer casts in T2 and the C++
  source extension, buffer-size checks, and error handling in T22. These release
  changes do not constitute new experiments or changes to the reported labels.
- Keep T7's reboot action manual and its target path configurable. Separate the
  retained upstream ImmoralFiber documentation from the benchmark instructions.
- Keep outputs from new evaluations separate from the released result matrix.

### Verification

- Match all 828 final case labels to the manuscript-derived result package.
- Cross-check the case-derived summaries against the per-technique README tables
  and all 27 stated aggregate checks.
- Include framework self-checks for validation, scoring, case coverage, and metrics.

## 2026-11-07 - integrated test materials and results

- Integrate the final case labels, 276 case-summary records, data dictionary,
  source fingerprints, common test protocol, and metric exports.
- Use results/outcomes_scored.csv as the canonical source for generated materials.
  Use the README reconstruction tool as an independent aggregate check.
- Retain the original statistical figures and blank templates for new evaluations.
  Original screenshots and full logs remain internal.

## Initial paper artifact

- Provide the technique directories and per-technique outcome tables.
- Describe the DET Matrix, four-stage workflow, L1-L5 outcome model, and headline
  results in the repository documentation.
