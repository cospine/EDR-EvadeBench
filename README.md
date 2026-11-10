# EDR-EvadeBench

**Artifact release: 2026-11-10.** [Repository](https://github.com/cospine/EDR-EvadeBench) · [Reproducibility](REPRODUCIBILITY.md) · [Final results](results/FINAL_RESULTS.md)

**A Framework for Evaluating EDR Evasion Techniques and Defenses**

EDR-EvadeBench is a systematic and reproducible framework for evaluating how well Endpoint Detection & Response (EDR) and endpoint-security products resist evasion techniques. It couples a defense-oriented technique taxonomy (the **DET Matrix**) with a validated evasion sample library and a standardized four-stage evaluation workflow, so that different products can be compared under controlled, reproducible conditions.

This repository provides the research materials for the framework:

- **Materials for 22 selected evasion implementations (research-oriented PoCs)**
- **The 3-Layer Defense Evasion Technique (DET) Matrix**
- **A standardized four-stage evaluation workflow**
- **Per-technique documentation, source/build files, scripts, and external-tool instructions as applicable**
- **All 828 final case labels, readable case summaries, a common test protocol, and metric-recalculation tools**

> ⚠️ **Read the [Ethical Considerations](#️-ethical-considerations) and [Disclaimer](#️-disclaimer) before using any sample in this repository.**

---

## 📌 Read First — Scope, Build Status, and Attribution

**What this repository is.** Source-level research artifacts and the
evaluation methodology and complete case-level results for the companion paper.

| Document | What it covers |
| :--- | :--- |
| [REPRODUCIBILITY.md](REPRODUCIBILITY.md) | Precisely what can and cannot be reproduced here, and what an evaluator must supply. |
| [BUILD.md](BUILD.md) | Per-technique build matrix, external dependencies, and source-specific build commands. |
| [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md) | Size, SHA-256, identification and provenance of every committed binary. |
| [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) | Upstream projects this benchmark adapts, with attribution status. |
| [CHANGELOG.md](CHANGELOG.md) | Changes made in each artifact version. |
| [SECURITY.md](SECURITY.md) | Responsible-use and vulnerability-reporting guidance. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to report problems and how to add techniques. |
| [`framework/`](framework/README.md) | The four-stage evaluation framework: case matrix, validation gate, L1–L5 scoring, PSD/BDD metrics, figures. |
| [`framework/runbook.md`](framework/runbook.md) | The operational procedure for running the benchmark. |
| [`results/`](results/README.md) | Complete final results, case summaries, data dictionary, PSD/BDD, and statistical plots. |
| [`results/FINAL_RESULTS.md`](results/FINAL_RESULTS.md) | Read all 828 final labels and their summaries. |
| [`framework/TEST_PROTOCOL.md`](framework/TEST_PROTOCOL.md) | Shared protocol, product/framework versions and the public/internal material boundary. |

**In one sentence:** the samples here let you reproduce the *methodology*, and
[`results/`](results/README.md) ships the case-level outcome matrix, so the
paper's reported numbers are recomputable as well. The [test protocol](framework/TEST_PROTOCOL.md) provides versions and settings; payload binaries, keys, infrastructure identifiers, original screenshots and full logs are not publicly distributed. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

> **No prebuilt executables are distributed.** Executable names that appear in
> the technique READMEs (for example `EDRSilencer.exe`, `RealBlindingEDR.exe`,
> `PowerTool_killer.exe`, `com_inject.exe`) are **build outputs** — compile the
> source in the same folder to produce them. [BUILD.md](BUILD.md) records the
> source layout, toolchains and external dependencies.

---

## ⭐ Key Features

### 1. The 3-Layer DET Matrix

A defense-oriented taxonomy that organizes evasion techniques by the EDR function they primarily target, rather than by adversary objective. It complements (rather than replaces) MITRE ATT&CK Enterprise v19, which separates the former *Defense Evasion* tactic into *Stealth* (TA0005) and *Defense Impairment* (TA0112).

- **Layer 1 — Detection Lifecycle.** The EDR stage a technique targets:
  - Data **Collection**
  - Data **Transmission**
  - **Detection**
- **Layer 2 — Evasion Strategies.** The tactical objective within each stage:
  - *Collection:* EDR Sensor Disruption, EDR Agent Disruption
  - *Transmission:* Telemetry Blocking
  - *Detection:* Memory Concealment, Obfuscation, Logic Bypass
- **Layer 3 — Evasion Techniques.** Specific, testable implementations (T1–T22), each paired with a validated sample and an explicit success condition.

### 2. Standardized Four-Stage Evaluation Workflow

1. **Sample Generation** — three C2-derived payload families + unified AES-based encryption + evasion logic integration
2. **Function Validation** — two-stage verification (evasion-logic verification + payload-functionality check) before deployment
3. **Sample Execution** — controlled execution against each product with clean-snapshot reset between runs
4. **Effectiveness Evaluation** — outcome scoring with the five-tiered prevention-stage model and the PSD / BDD metrics

> **The framework is implemented, not just described.** [`framework/`](framework/README.md)
> contains the operational core of all four stages — the case matrix
> ([`cases.py`](framework/cases.py)), the two-stage validation gate
> ([`validate.py`](framework/validate.py)), the L1–L5 decision procedure
> ([`score.py`](framework/score.py)), the PSD/BDD metrics ([`metrics.py`](framework/metrics.py))
> and the result figures ([`figures.py`](framework/figures.py)) — over a
> machine-readable encoding of Table 7 and Table 8 in
> [`framework/schema/`](framework/schema/). See the
> [runbook](framework/runbook.md) for the operational procedure and
> [`results/`](results/README.md) for the released outcome data.
> Stage 3 (execution) is deliberately manual; the runbook says why.

### 3. Public, Validated Sample Library

- One directory for each of the 22 selected implementations, with adapted source, scripts, or tool-specific preparation instructions as applicable
- Three base payload families derived from **Cobalt Strike**, **Havoc**, and **AdaptixC2**, to reduce single-payload bias
- All payloads protected with the same **AES-based encryption / runtime decryption** procedure
- The paper reports that every sample passed both evasion-logic verification and payload-functionality checks before inclusion; the per-technique success criteria are stated in each technique README and in Table 7 of the paper

> 📦 **Binaries policy.** This repository **does not include any exe/bin file that carries payload characteristics**. In particular, no real C2 payloads, weaponized samples, or malicious payload binaries are distributed. Concretely, the binaries present are limited to three categories:
>
> 1. **Generic auxiliary tooling** — the unmodified UPX packer (T17). Resource Hacker (T20) is obtained separately from its publisher.
> 2. **Auxiliary kernel drivers required by privilege-dependent techniques (BYOVD)** — `echo_driver.sys` (T6) and `kEvP64.bin` (T8). These are third-party binaries whose source is **not** included, so their behaviour is not source-auditable from this repository. Their hashes and provenance are recorded in [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md).
> 3. **All-zero placeholder files** — the `*.bin` files in T12 and T13 are entirely zero-filled, sized placeholders so that the shipped resource builds succeed; they contain no executable code. Replace them (or regenerate them, for T12's `notepad.bin`) before functional testing.
>
> No sample executable is distributed. Evaluators must supply their own payload for operational testing. See [Using the Samples](#-using-the-samples) and [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

### 4. Five-Tiered Prevention-Stage Outcome Model

Rather than a binary "detected / not detected" label, every execution is assigned one of five mutually exclusive levels describing **where** the product intervened:

| Level | Name | Meaning |
| :---: | :--- | :--- |
| **L1** | Pre-execution Prevention | Blocked before any process is created |
| **L2** | Pre-C2 Prevention | Process runs but is terminated before a C2 connection is established |
| **L3** | Pre-command Prevention | C2 connects, but the session is terminated before any command is sent |
| **L4** | Command-stage Prevention | Commands are sent but do not complete, or the session is terminated |
| **L5** | Operational Success | All commands execute and the session survives the observation window |

### 5. Quantitative Metrics

- **PSD (Prevention Stage Distribution).** For a *product*, the proportion of its outcomes at each of the five levels — i.e., *how prevention stages are distributed for a product*.
- **BDD (Bypass Depth Distribution).** For a *DET category or individual technique*, the proportion of its outcomes at each of the five levels — i.e., *how bypass depths are distributed*.

---

## 📊 Key Findings (Companion Paper)

The following headline results come from the companion paper's controlled evaluation of **six endpoint-security products** against **22 selected implementations × 3 payload families × 2 Windows environments**. See the paper for full methodology and caveats.

**Overall effectiveness.** Across all products, **23.0%** of the 792 non-baseline outcomes reached **L5 (Operational Success)**. All 36 AES-protected baseline cases, without additional evasion mechanisms, were stopped at **L1**, providing a common reference for the evasion cases.

**Per-product L5 (Operational Success) rate.**

| Product | Type | L5 Rate |
| :--- | :--- | :---: |
| Sophos Endpoint Detection and Response | Commercial | 0.0% |
| Bitdefender Endpoint Security Tools | Commercial | 0.0% |
| Elastic Security | Open-source | 9.1% |
| Kaspersky Endpoint Security | Commercial | 16.7% |
| Microsoft Defender Antivirus (built-in baseline) | Built-in | 54.5% |
| Huorong Endpoint Security | Commercial | 57.6% |

These results group into three defensive profiles: **early preventers** (Sophos, Bitdefender), **mixed-stage preventers** (Kaspersky, Elastic Security), and products with **high operational-success exposure** (Huorong, Microsoft Defender Antivirus). The Microsoft Defender Antivirus result characterizes only the tested built-in stack (not onboarded to Microsoft Defender for Endpoint) and should not be extrapolated to the full MDE product.

**Three recurring defensive weaknesses.**

1. **Vulnerable sensors and inconsistent self-protection.** Disrupting telemetry collection, transmission, or the agent itself can substantially degrade protection; resilience varies by product. *Symlink-based EDR Corruption (T7)* reached L5 in 66.7% of its outcomes.
2. **Blind spots in memory injection and trusted-process execution.** Several products did not consistently prevent the tested memory-injection and trusted-process execution samples. Technique-level L5 ranged from 0.0% (T14 PoolParty) to 36.1% (T11 DLL Hijacking).
3. **Payload-dependent defensive outcomes.** The same evasion mechanism yielded different outcomes by payload family: overall L5 was 8.7% for Cobalt Strike vs. 32.6% (Havoc) and 27.7% (AdaptixC2).

> Results are tied to the specific product versions, configurations, payloads, and environments tested, and are **not** permanent product rankings.

---

## 📁 Repository Structure

The repository is organized by technique ID. Each folder contains a dedicated README and the materials for that implementation: adapted source and build files, scripts, or tool-specific preparation instructions. External dependencies are listed in [BUILD.md](BUILD.md).

```text
EDR-EvadeBench/
├── T1_Direct Syscall Invocation/
├── T2_ETW_AMSI Patching/
├── T3_DLL Signature Restriction Bypass/
├── T4_Hook Overwriting/
├── T5_NTDLL Hook Removal/
├── T6_Kernel Callback Removal/
├── T7_Symlink-based EDR Corruption/
├── T8_EDR Process Termination/
├── T9_EDRSilencer/
├── T10_COM Hijacking/
├── T11_DLL Hijacking/
├── T12_COM-based Process Injection/
├── T13_Fiber-based Process Injection/
├── T14_Thread Pool-based Injection/
├── T15_Process Hollowing/
├── T16_Module Stomping/
├── T17_Code Packing/
├── T18_Code Virtualization/
├── T19_Compiler-level Obfuscation/
├── T20_PE Resource Masquerading/
├── T21_API-level Behavioral Obfuscation/
├── T22_COM-based Process Creation/
├── framework/                ← the four-stage framework (code + schema + runbook)
│   ├── README.md
│   ├── runbook.md
│   ├── cases.py  validate.py  score.py  metrics.py  figures.py
│   ├── schema/               ← Table 1 + Table 7 + Table 8, machine-readable
│   ├── templates/            ← Stage 2 and Stage 3 record templates
│   ├── tools/                ← reconstructs results/ and cross-checks the paper
│   └── tests/                ← self-checks
├── results/                  ← released outcome data, metrics and figures
├── README.md                 ← this file
├── REPRODUCIBILITY.md        ← what can and cannot be reproduced here
├── BUILD.md                  ← build matrix and source-specific commands
├── BINARY_PROVENANCE.md      ← hashes and provenance of bundled binaries
├── THIRD_PARTY_NOTICES.md    ← upstream projects and attribution
├── LICENSES/                 ← retained third-party license texts
├── CHANGELOG.md
├── SECURITY.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## 🛠 Technique Library (T1–T22)

Each Layer 3 technique below is mapped to its DET Matrix Layer 1 stage and Layer 2 strategy.

| ID | Technique | DET Stage | DET Strategy |
| :---: | :--- | :--- | :--- |
| T1 | Direct Syscall Invocation | Collection | EDR Sensor Disruption |
| T2 | ETW & AMSI Patching | Collection | EDR Sensor Disruption |
| T3 | DLL Signature Restriction | Collection | EDR Sensor Disruption |
| T4 | Hook Overwriting | Collection | EDR Sensor Disruption |
| T5 | NTDLL Hook Removal | Collection | EDR Sensor Disruption |
| T6 | Kernel Callback Removal | Collection | EDR Agent Disruption |
| T7 | Symlink-based EDR Corruption | Collection | EDR Agent Disruption |
| T8 | EDR Process Termination | Collection | EDR Agent Disruption |
| T9 | EDRSilencer | Transmission | Telemetry Blocking |
| T10 | COM Hijacking | Detection | Memory Concealment |
| T11 | DLL Hijacking | Detection | Memory Concealment |
| T12 | COM-based Process Injection | Detection | Memory Concealment |
| T13 | Fiber-based Process Injection | Detection | Memory Concealment |
| T14 | Thread Pool-based Injection (PoolParty) | Detection | Memory Concealment |
| T15 | Process Hollowing | Detection | Memory Concealment |
| T16 | Module Stomping | Detection | Memory Concealment |
| T17 | Code Packing (UPX) | Detection | Obfuscation |
| T18 | Code Virtualization (VMProtect) | Detection | Obfuscation |
| T19 | Compiler-level Obfuscation (OLLVM) | Detection | Obfuscation |
| T20 | PE Resource Masquerading | Detection | Obfuscation |
| T21 | API-level Behavioral Obfuscation | Detection | Logic Bypass |
| T22 | COM-based Process Creation | Detection | Logic Bypass |

> **Privilege assumptions.** Most techniques run as Standard User. T6 and T8 additionally require an elevated administrator context and a vulnerable signed driver (BYOVD); T7 and T9 require elevated administrator. Outcomes for elevated or driver-assisted techniques characterize **post-compromise EDR self-protection**, not prevention of the preceding privilege escalation. See the paper (Table 7) for the full privilege and success-criteria checklist.

---

## 🧪 Using the Samples

To replicate the methodology, follow the four-stage workflow:

1. **Sample Generation**
   - Navigate to a technique folder (e.g., `T1_Direct Syscall Invocation`).
   - Follow that technique's README to compile the source into the evasion sample. [BUILD.md](BUILD.md) lists which builds are self-contained and which need generated files or external dependencies.
   - **Supply your own payload.** Source projects ship with placeholder payload buffers only (the `shellcode_aes_payload` arrays and the bundled `*.bin` files are all-zero). Integrate your own (AES-encrypted) shellcode/payload, and the matching AES-256 key, before operational use. Per the repository's binaries policy, no exe/bin carrying payload characteristics is included; see [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md) for exactly what is bundled and why.

2. **Function Validation**
   - First confirm the evasion logic reaches its post-condition (per the technique's success criteria).
   - Then confirm the payload beacons and responds to test commands (e.g., `whoami`, `ps`).
   - Samples that target EDR state (e.g., T4, T6–T9) are validated with the target product's relevant components present.

3. **Sample Execution**
   - Deploy the validated sample on the target environment with the product installed with its default protection configuration.
   - Revert the VM (and the C2 host) to a clean snapshot before every execution to prevent cross-case carryover.

4. **Effectiveness Evaluation**
   - Assign each execution one of the five outcome levels (L1–L5) by correlating endpoint state, C2 logs, and product alerts/protection logs.
   - Aggregate into PSD (per product) and BDD (per category/technique).

---

## 📜 Licence and Attribution

This benchmark adapts code from a number of upstream projects, listed with
their paper references in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
Those components remain under their own licences.

The authors' own contributions are available for non-commercial scientific
evaluation under [LICENSE](LICENSE). Third-party components remain under their
own terms, as listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); copies
of the retained upstream licenses are in [LICENSES/](LICENSES/). The authors'
license does not restrict rights granted by those upstream licenses.

Bundled binary files — including the two auxiliary kernel drivers, UPX, and
zero-filled payload placeholders — are documented in
[BINARY_PROVENANCE.md](BINARY_PROVENANCE.md). Resource Hacker is an external
dependency obtained from its publisher; it is not bundled.

## 🔄 Versioning and Maintenance

The reported experiments used the first adapted implementation versions, without revisions during evaluation. Monthly collection, GPT-4o candidate ranking and expert review are planned future maintenance, not procedures used to construct the evaluated set. Future revisions would repeat the same validation checks and retain version/change records. Repository documentation and portability changes are recorded in [CHANGELOG.md](CHANGELOG.md).

Because the released source is the artifact the paper references, any change
that alters an evasion mechanism or a sample's observable behaviour is
recorded explicitly in the changelog rather than made silently.

---

## ⚖️ Ethical Considerations

EDR-EvadeBench is intended **strictly for academic, defensive, and product-hardening research**.

- All experiments were conducted on **isolated virtual machines** and researcher-controlled infrastructure, with no interaction with production systems or unrelated third-party hosts.
- The samples are **research-oriented proofs of concept** that demonstrate behavioral mechanisms; they omit active infrastructure, credentials, vendor-specific secrets, turnkey deployment instructions, and weaponization guidance for production endpoints.
- A **coordinated disclosure** process was followed: product-specific findings, supporting evidence, and mitigation suggestions were reported to the evaluated vendors before publication.
- The released artifacts reproduce the **methodology**, not necessarily the exact reported results (evaluators supply their own payloads).

## 🛡️ Disclaimer

This project is intended **solely for research and educational purposes**. Do not use any part of this repository for unauthorized or malicious activities. You are solely responsible for complying with all applicable laws and regulations.
