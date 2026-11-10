# T17: Code Packing (UPX)

**DET classification:** Detection → Obfuscation

This technique utilizes common binary packers, such as the **Ultimate Packer for eXecutables (UPX)**, to compress the malicious payload and modify its file structure. The original code is encrypted/compressed, and a small decompression stub is prepended to the binary.

The purpose of packing is twofold:

1.  **Static Evasion:** Change the file's hash and file signature, bypassing EDRs and antivirus solutions that rely on known malicious hash lists or byte patterns.
2.  **Hinder Analysis:** Force analysts and automated sandbox systems to unpack the binary before its true malicious functionality can be examined.

Upon execution, the stub rapidly decompresses the original code into memory, which then executes. EDRs must rely on dynamic analysis or signature detection of the decompression stub to catch this technique.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 11.1%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 44.4% | 38.9% | 5.6% | 0.0% | **11.1%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 16.7% | 16.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 66.7% | 0.0% |

**Interpretation.** UPX packing was predominantly prevented early: 44.4% of outcomes at L1 and 38.9% at L2, consistent with well-known packer stub signatures and runtime unpacking heuristics. Only Huorong allowed operational success (L5 in 4 of 6 outcomes); every other product stopped all executions at L1 or L2. This aligns with the paper's finding that the Obfuscation strategy had the lowest L5 rate of all Layer 2 strategies (16.7%), with 77.1% of its outcomes stopped at L1 or L2: altering a sample's static appearance while preserving runtime behavior does not defeat current early-stage detection.

## ⚙️ Usage (Defensive Research)

The implementation requires the use of the UPX tool on the final compiled evasion sample (the payload loader). A copy of the generic UPX utility is included in this folder as auxiliary tooling without payload characteristics.

### Prerequisites

* The **UPX** utility (the bundled copy or a newer release compatible with your target PE architecture, x86/x64) is required.
* A compiled PE file (e.g., your own payload loader built from this repository's sources) to be used as the target file.

### Detailed Execution Steps

1.  **Acquire UPX:**
    * Use the bundled UPX utility or download the latest release, ensuring it is compatible with your target PE architecture (x86/x64).

2.  **Pack the Target File:**
    * Use the UPX tool to compress the target executable.
        ```bash
        upx yourfile.exe
        ```
    * *Note: Always verify that the packed executable still runs correctly before testing against an EDR.*

3.  **Validation:**
    * Submit the packed file to a tool like VirusTotal to see if the packing operation successfully changed its signature.
    * Run the packed executable against the target EDR to test if the EDR's dynamic analysis or decompression stub heuristics are effective.

> **Warning:** While widely supported, UPX is one of the most recognized packers. Modern security products are highly effective at detecting it, making it mainly useful for testing baseline security capability.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Bundled tool | `upx.exe` — unmodified upstream UPX (amd64) |
| Build project | n/a |
| Prebuilt processed sample | Not distributed — pack your own build output |

`upx.exe` size, SHA-256 and provenance are recorded in
[../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** the packed executable runs successfully, the
  original payload still executes in memory, and the C2 beacon is established.
  Packing must not break the sample — verify the packed binary manually before
  testing.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## ▶️ Usage

```bat
upx yourfile.exe
```

## 🧹 Cleanup / Recovery — none required

Packing modifies a file on disk, not system state. Keep both the original and
the packed copy so you can compare signatures.

## ⚠️ Known Limitations

- UPX is the most widely recognised packer in existence; its stub is a
  high-signal static indicator, consistent with the technique's reported
  outcomes (the lowest L5 rate of the Obfuscation strategy).
- The bundled UPX tool reports version **5.0.2**; see
  [../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).
