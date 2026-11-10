# T20: PE Resource Masquerading

**DET classification:** Detection → Obfuscation

This technique focuses on modifying the **Portable Executable (PE) file structure** of a malicious binary to inherit the rich resource data (icons, version information, manifest, and string tables) from a legitimate, trusted application.

The goal is to defeat **static analysis** and **metadata inspection** performed by EDRs:

1.  **Trust Inheritance:** The binary appears to possess valid, trustworthy metadata (e.g., copyright, product name, version numbers) that matches a known good vendor (like Microsoft), which can reduce the initial suspicion score assigned by the EDR.
2.  **Signature Blending:** By importing a large volume of benign resource data, the unique signatures of the small, malicious loader code can be further obscured.

This method tricks EDR logic that relies on file metadata integrity and resource quality as an indicator of trustworthiness.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 27.8%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 16.7% | 50.0% | 5.6% | 0.0% | **27.8%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 50.0% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 33.3% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** Resource masquerading reached operational success against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes) and, partially, Kaspersky (2 of 6), while Sophos, Bitdefender, and Elastic Security produced no L5 outcomes. The paper explicitly cites this technique as strongly payload-dependent — 0.0% with Cobalt Strike versus 50.0% with Havoc and 33.3% with AdaptixC2 — which shows that trusted metadata can lower suspicion scoring for some payload implementations but does not mask the artifacts of others.

## ⚙️ Usage (Defensive Research)

The implementation requires a resource editing tool (like Resource Hacker) to extract resources from a trusted binary and insert them into the compiled malicious payload. A copy of the generic Resource Hacker utility is included in this folder as auxiliary tooling without payload characteristics.

### Prerequisites

* A PE resource editing tool (e.g., Resource Hacker obtained from its publisher).
* A target legitimate PE file (e.g., `calc.exe`) to steal resources from.
* The executable to be masqueraded (e.g., your own payload loader built from this repository's sources; the repository does not distribute any exe/bin carrying payload characteristics).

### Detailed Execution Steps

1.  **Extract Resources from Trusted Binary:**
    * Use the resource editing tool to open a legitimate application (e.g., `C:\Windows\System32\calc.exe`).
    * Use the tool's function to **save all resources to a `.res` file**.

2.  **Import Resources into Payload:**
    * Open the target executable (`payload.exe`) in the resource editing tool.
    * Use the tool's function to **import the saved `.res` file**. This overwrites the existing resources (or lack thereof) with the legitimate data.
    * Save the modified payload executable.

3.  **Validation:**
    * Right-click the modified payload executable and check its **Properties** -> **Details** tab; it should now display the stolen product and version information.
    * Run the modified executable against the target EDR to verify if the resource modification successfully lowered the suspicion score or delayed detection.

> **Warning:** Masquerading resources does not change the code structure. It is an evasion technique against static metadata analysis only and should be tested alongside other techniques for comprehensive evaluation.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| External tool | [Resource Hacker](https://www.angusj.com/resourcehacker/), obtained separately from its publisher |
| Example resource | `calc.res` |
| Build project | n/a |
| Prebuilt masqueraded sample | Not distributed — apply resources to your own build output |

The example resource file's hash is recorded in
[../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** PE icons and product/version metadata are
  modified to resemble trusted software; the executable runs successfully
  and establishes the C2 beacon.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## ▶️ Usage

1. Open a legitimate binary (e.g. `C:\Windows\System32\calc.exe`) in Resource
   Hacker and **save all resources to a `.res` file**.
2. Open your payload loader, **import the `.res` file**, and save.

## 🧹 Cleanup / Recovery — none required

Resource modification changes a file on disk. Keep the original build output
for comparison.

## ⚠️ Known Limitations

- `calc.res` is an example resource input; see [BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).
- Masquerading changes metadata only; code structure is unchanged, so it does
  not defeat behavioural or memory-based detection.
- The reference Resource Hacker executable reports FileVersion **5.1.7.343**. It is not distributed in this release.
