# T16: Module Stomping

**DET classification:** Detection → Memory Concealment

Module Stomping is a specialized in-memory code injection technique designed to evade EDRs that check memory region attributes and ownership. It involves:

1.  **Loading a Benign Module:** The attacker or the host process loads a legitimate, trusted DLL into the target process's memory (this module is fully mapped and tracked by the OS/EDR).
2.  **Stomping:** The malicious Shellcode or PE payload is written to (overwritten onto) the executable sections (e.g., `.text`) of the legitimately mapped benign module.
3.  **Execution:** Execution is transferred to the overwritten section.

The key evasion benefit is that the memory region containing the payload retains the legitimate file metadata (module name, file path, digital signature) associated with the original DLL. EDRs attempting to trace the origin of the execution will see the malicious code running from memory belonging to a **trusted module**.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 22.2%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 16.7% | 50.0% | 5.6% | 5.6% | **22.2%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 33.3% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** Masking the payload behind a legitimately mapped module's metadata reached operational success against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes), while Sophos, Kaspersky, Bitdefender, and Elastic Security produced no L5 outcomes (most executions stopped at L2, Elastic at L1). The technique is payload-dependent (0.0% with Cobalt Strike vs. 33.3% with Havoc and AdaptixC2), showing that trusted-module attribution does not by itself conceal payload-specific memory artifacts from products performing memory-content inspection or cross-stage correlation.

## ⚙️ Usage (Defensive Research)

The implementation requires a compiled executable (`ModuleStomping.exe`) that executes the remote stomping operation against a running process.

### Prerequisites

* The source code for the Module Stomping utility is required.
* A C/C++ compiler (e.g., Visual Studio) is required for compilation.
* A target process (e.g., `notepad.exe`) running, which the EDR is monitoring.
* **Administrator privileges** are often required for cross-process memory manipulation.

### Detailed Execution Steps

1.  **Prepare the Target:**
    * Launch a benign process (e.g., `notepad.exe`).
    * Find the Process ID (PID) of this target process using Task Manager or Process Explorer.

2.  **Compile the Stomping Utility:**
    * Integrate your own (AES-encrypted) EDR-EvadeBench payload into the project's source code; the shipped source contains a placeholder buffer only.
    * Compile the utility to produce the final executable (`ModuleStomping.exe`).

3.  **Execute the Stomping Operation:**
    * Run the compiled executable, passing the target PID as an argument. The utility will handle locating a suitable module and performing the memory overwrite.
        ```bash
        "Module Stomping.exe" <PID_of_Target_Process>
        # Example: "Module Stomping.exe" 1234
        ```

4.  **Validation:**
    * Verify that the payload executes successfully.
    * Use Process Explorer or a custom memory scanner to inspect the memory region of the overwritten module in the target process. The region's path/module name should correspond to the benign module, even though the content is malicious.

> **Warning:** Module Stomping involves highly complex and potentially destructive cross-process memory operations. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `Module Stomping/Module Stomping.cpp` |
| Helper header | `Module Stomping/lazy_importer.hpp` |
| Build project | `Module Stomping.sln` / `.vcxproj` (toolset `v143`) |
| Payload buffer / key | All-zero placeholders — supply your own |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

The source also compiles directly with MinGW-w64 gcc 14.2.0 (verified); see
[BUILD.md](../BUILD.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a legitimate DLL module is loaded, its
  executable section is overwritten with the payload, and the C2 beacon is
  established **with the module name appearing as a signed binary**.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## ▶️ Usage and Output Name

The build-output name is not consistent across the shipped files:

- `Module Stomping.vcxproj` produces an executable named after the project
  (`Module Stomping.exe`, i.e. with a space);
- the source header comment refers to `module_stomping_encrypted.exe`.

Use the name your build actually produces, and **quote the path** because it
contains a space:

```bat
"Module Stomping.exe" 1234
```

## 🧹 Cleanup / Recovery

The stomped module's `.text` is overwritten in a live target process.
Terminate the target and revert the snapshot; a stomped module can crash the
target when the original export is called.

## ⚠️ Known Limitations

- The default target module is `C:\Windows\System32\amsi.dll`; the `.text`
  section must be large enough to hold the payload.
- Stomping an export the process later calls will crash it — pick a module
  whose exports are not exercised, or use a dedicated target process.
