# T15: Process Hollowing

**DET classification:** Detection → Memory Concealment

Process Hollowing is a classic, widely used process injection technique designed to execute a malicious PE file from within the memory space of a legitimate, trusted host process. The steps involve:

1.  **Creation:** Creating a new instance of a benign executable (the host process, e.g., `svchost.exe`) in a suspended state.
2.  **Hollowing:** Unmapping or overwriting the original, legitimate code in the host process's memory space.
3.  **Mapping:** Writing the malicious PE image (the payload) into the newly emptied memory space.
4.  **Resumption:** Adjusting the host process's context/entry point to point to the malicious code's entry point and resuming the thread.

The core evasion goal is to ensure the execution of the payload appears to originate from a highly trusted, legitimate process, often confusing EDR behavioral analysis.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 16.7%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 33.3% | 50.0% | 0.0% | 0.0% | **16.7%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 16.7% | 16.7% | 16.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 100.0% |

**Interpretation.** Despite being a classic technique, Process Hollowing achieved operational success against only one evaluated product: Microsoft Defender Antivirus, where all 6 outcomes reached L5. Every other product prevented all executions early — Kaspersky and Elastic Security at L1, Sophos, Bitdefender, and Huorong at L2. This confirms robust, multi-layered detection of its core steps (suspended-process creation, cross-process memory write, anomalous thread resumption) in most evaluated products. The L5 rate is identical across all three payload families (16.7%), indicating that success here is product-specific rather than payload-driven.

## ⚙️ Usage (Defensive Research)

The implementation requires a compiled injector executable (`runpe.exe`) that takes the malicious file and the target host process as arguments.

### Prerequisites

* The source code for the Process Hollowing utility is required.
* Two PE files: The **Source Image** (`malware.exe`, the file to be executed) and the **Target Process** (`host.exe`, the legitimate process to be hollowed).
* A C++ compiler (e.g., Visual Studio) is required for compilation.

### Detailed Execution Steps

1.  **Compile the Injector:**
    * Compile the source code for the Process Hollowing project to produce the injector executable (`runpe.exe`).

2.  **Execute the Hollowing Operation:**
    * Run the compiled injector, specifying the path to the malicious executable (the source image) and the path to the benign executable (the target process) that will host the payload.
        ```bash
        runpe.exe <source image> <target process>
        # Example: runpe.exe C:\Path\To\Payload.exe C:\Windows\System32\svchost.exe
        ```

3.  **Validation:**
    * Verify that the original target process (e.g., `svchost.exe`) is running and that the malicious payload's logic is executing within its context.
    * Use tools like Process Explorer to inspect the process's memory regions and entry point to confirm the hollowing operation was successful.

> **Warning:** This technique is easily detected by modern EDRs due to the high-volume of traceable API calls (e.g., `NtUnmapViewOfSection`). It is primarily useful as a baseline test or when combined with other evasion techniques.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `Source/Process Hollowing/Process_Hollowing.cpp` |
| Build project | `Source/Process Hollowing.sln` / `.vcxproj` (toolset `v143`) |
| Output name | `runpe.exe` (`<TargetName>runpe</TargetName>` in the project) |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

The source also compiles directly with MinGW-w64 gcc 14.2.0 (verified); see
[BUILD.md](../BUILD.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** the target process is created in a suspended
  state, its original image is unmapped, and the payload is written into its
  memory — confirmed by a **byte-pattern scan** for a known payload signature.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## ▶️ Usage

```bat
runpe.exe <source image> <target process>
runpe.exe C:\Path\To\Payload.exe C:\Windows\System32\svchost.exe
```

## 🧹 Cleanup / Recovery

The hollowed host process is left running with replaced code. Terminate it
and revert the snapshot.

## ⚠️ Known Limitations

- The **source image and the target process must match in architecture**
  (both x86 or both x64); the sample handles both (including a WOW64 path) but
  will not mix them.
- The source image must be a valid PE with a relocation table where required.
- This is the classic, heavily-signatured form of process hollowing, so it is
  expected to be caught early — consistent with its reported outcomes.
