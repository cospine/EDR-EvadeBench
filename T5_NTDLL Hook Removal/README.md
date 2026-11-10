# T5: NTDLL Hook Removal

**DET classification:** Data Collection → EDR Sensor Disruption

This technique targets user-mode API hooking, a primary mechanism EDRs use to capture low-level telemetry by injecting a hook into the prologue of critical functions within `ntdll.dll`.

The NTDLL Hook Removal PoC works by:

1.  **Locating the Original Binary:** Identifying a clean, unhooked copy of `ntdll.dll` (e.g., from disk or from an isolated system module).
2.  **Memory Overwrite:** Iterating through the hooked functions in the currently loaded `ntdll.dll` and overwriting their modified prologues with the original, benign bytes from the clean copy.

Once the hooks are removed, any subsequent calls to the affected functions will execute their intended logic directly, bypassing the EDR's injected monitoring function and effectively **blinding the user-mode sensor layer**.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 16.7%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 33.3% | 38.9% | 11.1% | 0.0% | **16.7%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 33.3% | 16.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 33.3% | 0.0% | 0.0% | 0.0% | 66.7% |

**Interpretation.** Restoring the original `ntdll.dll` prologues achieved operational success mainly against Microsoft Defender Antivirus (L5 in 4 of 6 outcomes) and, partially, Kaspersky (2 of 6). Elastic Security and Huorong prevented every execution at L1, while Sophos and Bitdefender stopped all outcomes at L2 — evidence that products with hook-integrity monitoring, static detection, or kernel-level validation are not defeated by in-process unhooking alone. The technique is moderately payload-dependent (0.0% with Cobalt Strike vs. 33.3% with Havoc).

## ⚙️ Usage (Defensive Research)

The implementation requires a compiled executable (`unhook.exe`) that embeds the unhooking logic and the final shellcode execution.

### Prerequisites

* The source code for the unhooking project is required.
* A C/C++ compiler (e.g., Visual Studio) is required for compilation.
* The PoC must contain your own (AES-encrypted) EDR-EvadeBench payload; the shipped source contains a placeholder buffer only.

### Detailed Execution Steps

1.  **Prepare Payload and Compile:**
    * Integrate the EDR-EvadeBench base shellcode/loader into the unhooking project's source code.
    * Compile the project to produce the final executable (e.g., `unhook.exe`).

2.  **Execute the Unhooking and Payload:**
    * Run the compiled executable with the necessary privileges.
        ```bash
        unhook.exe
        ```
    * *Note: The PoC is designed to execute the unhooking routine first, immediately followed by the execution of the shellcode payload, ensuring the payload runs in a blind environment.*

3.  **Validation:**
    * Use a tool like API Monitor or a debugger to confirm that the EDR's hooks are visibly absent from functions like `NtAllocateVirtualMemory` or `NtCreateThreadEx` in the process memory, and verify that the embedded payload executes successfully without generating an alert.

> **Warning:** This technique involves highly sensitive memory manipulation. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `unhook.cpp` |
| Helper header | `lazy_importer.hpp` |
| Payload buffer | All-zero placeholder — supply your own |
| AES key | All-zero placeholder — supply your own |
| Build project | None — compile the single source directly |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

This project compiles cleanly with MinGW-w64 gcc 14.2.0; see
[BUILD.md](../BUILD.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a fresh copy of `ntdll.dll` is mapped from
  disk, the in-memory function prologues are restored to their original
  bytes, and API calls bypass the user-mode hooks. Verify by comparing the
  prologue bytes of e.g. `NtAllocateVirtualMemory` / `NtCreateThreadEx`
  against the on-disk image.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

## 🧹 Cleanup / Recovery

In-process only. Revert the VM snapshot between runs.

## ⚠️ Known Limitations

- The clean copy is read from the hard-coded path
  `C:\Windows\System32\ntdll.dll`; a redirected or relocated system directory
  will break it.
- Removing hooks does not remove kernel-level telemetry, consistent with the
  paper's finding that in-process unhooking alone is not sufficient.
