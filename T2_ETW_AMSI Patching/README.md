# T2: ETW & AMSI Patching

**DET classification:** Data Collection → EDR Sensor Disruption

This technique simultaneously targets two crucial, built-in security interfaces used by EDRs and Windows Defender: the **Antimalware Scan Interface (AMSI)** and **Event Tracing for Windows (ETW)**.

* **AMSI Bypass:** Achieved by patching the `AmsiScanBuffer` function (typically returning success before any meaningful scan occurs) or corrupting the AMSI script context in memory, effectively allowing malicious scripts (PowerShell, VBScript) or memory buffers to execute unscanned.
* **ETW Bypass:** Achieved by patching the `NtTraceEvent` function in `ntdll.dll` (overwritten with `RET`) to prevent telemetry from being emitted into the ETW logging channels, which EDRs widely consume for behavioral monitoring. `NtTraceEvent` is the lower-level syscall entry that `EtwEventWrite` eventually reaches, so patching it disables the same emission path from this process.

By disabling both mechanisms, the PoC creates a dual-layer blind spot, preventing both memory scanning and event logging of subsequent malicious activities.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 27.8%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 16.7% | 38.9% | 16.7% | 0.0% | **27.8%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 50.0% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 33.3% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** Disabling ETW and AMSI removes two telemetry channels, but products that rely on additional sensors (kernel callbacks, memory inspection, or behavioral analytics) still intervene. Elastic Security prevented every execution at L1, while Sophos and Bitdefender stopped all outcomes at L2. Operational success was reached only against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes). The outcome is strongly payload-dependent (0.0% with Cobalt Strike vs. 50.0% with Havoc), indicating that payload-specific artifacts — not the patching mechanism itself — largely determined success.

## ⚙️ Usage (Defensive Research)

The implementation requires compiling the patching logic into an executable (`amsi-etw-patch.exe`) that executes the patches and then runs the final payload in the newly blind environment.

### Prerequisites

* The source code for the AMSI/ETW patching project is required.
* A C/C++ compiler (e.g., Visual Studio) is required for compilation.
* The PoC must integrate your own (AES-encrypted) EDR-EvadeBench payload; the shipped source contains a placeholder buffer only.

### Detailed Execution Steps

1.  **Prepare Payload and Compile:**
    * Integrate the EDR-EvadeBench base shellcode/loader into the project's source code.
    * Compile the project to produce the final executable (`amsi-etw-patch.exe`).

2.  **Execute the Patch and Payload:**
    * Run the compiled executable with the necessary privileges.
        ```bash
        amsi-etw-patch.exe
        ```
    * *Note: The executable should apply the memory patches (e.g., modifying `ntdll.dll` and `amsi.dll` functions) and then immediately execute the malicious payload.*

3.  **Validation:**
    * Attempt to run a PowerShell script or memory-based payload after running the PoC.
    * Use debugging tools to confirm that the `AmsiScanBuffer` and `NtTraceEvent` functions have been patched in memory (e.g., the function prologue has been overwritten to jump to `ret` or return a success code).

> **Warning:** Patching these system interfaces is highly anomalous and easily detected by integrity monitoring checks. This technique is often used as a direct evasion test for systems relying on these specific telemetry sources.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `amsi-etw-patch/amsi-etw-patch.cpp` |
| Helper header | `amsi-etw-patch/lazy_importer.hpp` |
| Payload buffer | All-zero placeholder (`shellcode_aes_payload`) — supply your own |
| AES key | All-zero placeholder — supply your own |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

This project compiles cleanly with MinGW-w64 gcc 14.2.0; see
[BUILD.md](../BUILD.md) for the exact command.

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** subsequent execution of a benign AMSI test
  string completes **without triggering a scan event**, and ETW event tracing
  is disabled for the process.
- **Payload-functionality check:** C2 beacon observed within the 60-second
  window, and the beacon answers test commands.

## 🧹 Cleanup / Recovery

Both patches are applied to the running process's own in-memory copies of
`amsi.dll` and `ntdll.dll`. Nothing is written to disk and nothing persists;
the patches disappear when the process exits. Revert the VM snapshot between
runs.

## ⚠️ Known Limitations

- **The ETW component patches `NtTraceEvent` (overwritten with `RET`), not
  `EtwEventWrite`.** `NtTraceEvent` is the lower-level syscall entry that
  `EtwEventWrite` eventually reaches; patching it disables the same emission
  path from this process. Reproduce and validate accordingly.
- The AMSI patch writes a single byte at a **hard-coded offset (`+0x83`)**
  into `AmsiScanBuffer`. That offset is a property of a particular `amsi.dll`
  build. Verify the target bytes before and after on your own system; on a
  different build the write may corrupt the function instead of neutralising
  it.
- Patching these interfaces is highly anomalous and is detected by integrity
  monitoring, consistent with the paper's reported outcomes.
