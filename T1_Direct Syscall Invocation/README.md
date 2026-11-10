# T1: Direct Syscall Invocation

**DET classification:** Data Collection → EDR Sensor Disruption

This technique bypasses user-mode API hooking, which is a common mechanism used by EDRs to monitor process, thread, and memory operations (e.g., `CreateRemoteThread`, `NtProtectVirtualMemory`).

Instead of calling high-level Windows API functions (which typically reside in `ntdll.dll` and contain EDR hooks at their entry points), the PoC directly jumps to the kernel using system call instructions (`syscall` or `sysenter`). This is achieved by generating custom assembly stubs that contain the necessary system call number (SSN) and execution logic. This execution path is invisible to user-mode hooks, effectively **blinding the EDR's user-mode sensor layer**.

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

**Interpretation.** Bypassing user-mode hooks alone is not sufficient for reliable evasion. Elastic Security prevented every execution at L1 (pre-execution), while Sophos and Bitdefender stopped all outcomes at L2, showing that static, behavioral, or kernel-level telemetry still captures the downstream operations issued via syscalls. Operational success concentrated on Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes). The result is also payload-dependent — 0.0% with Cobalt Strike but 50.0% with Havoc — indicating that products that did not generalize across payloads drove much of the observed success.

## ⚙️ Usage (Defensive Research)

The implementation requires the use of a Syscall stub generator (like **SysWhispers3**) to create the necessary assembly and C source files before compilation.

### Prerequisites

* **Python 3** and the **SysWhispers3** utility are required for generating the syscall stubs.
* A C/C++ compiler (e.g., MSVC or MinGW-w64) that supports inline assembly or linking with ASM files is necessary for compilation.

### Detailed Execution Steps

1.  **Generate Syscall Stubs:**
    * Use the SysWhispers3 script to specify the kernel functions required for the payload execution (e.g., memory allocation, protection, and thread creation). This generates the header (`.h`), C source (`.c`), and assembly (`.asm`) files.
        ```bash
        py syswhispers.py --functions NtCreateThreadEx,NtProtectVirtualMemory,NtAllocateVirtualMemory -o syscalls_mem --arch x64 --wow64
        ```
    * *Note: The functions listed above are commonly used for shellcode injection.*

2.  **Compile the Test Application:**
    * Compile your main payload loader (`test.c`) along with the generated stubs (`syscalls_mem.c`, `syscalls_mem.h`, and `syscalls_mem.x64.asm`).
    * The compilation process must correctly link the assembly files to ensure the direct syscall invocation logic is included.
    * Integrate your own (AES-encrypted) payload into the loader; the shipped source contains a placeholder buffer only.

3.  **Validation:**
    * Run the compiled executable and check if the payload executes successfully.
    * Use tools like API monitor to verify that the high-level Windows API functions (e.g., `VirtualAllocEx`, `CreateRemoteThread`) were *not* called, confirming that the execution path went through the direct syscall stubs.

> **Warning:** Direct Syscall Invocation bypasses user-mode monitoring but is still susceptible to kernel-level detection. Testing should focus on verifying the successful bypass of user-mode hooks specifically.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Loader source | `test.c` |
| Generator | `syswhispers.py` (standard-library imports; required `data/` JSON and template files are **not** vendored) |
| Generated stubs | **Not included** — `syscalls_mem.h`, `syscalls_mem.c`, `syscalls_mem.x64.asm` must be generated before this sample compiles |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** the intended system service is executed with **no calls to hooked user-mode API functions** — verify with an inline-breakpoint audit or an API monitor that the high-level APIs (e.g. `VirtualAllocEx`, `CreateRemoteThread`) are not reached.
- **Payload-functionality check:** C2 beacon observed on the listener within the 60-second window, and the beacon answers test commands (`whoami`, `ps`).

## 🧹 Cleanup / Recovery

In-process only; nothing is persisted. When the process exits, its execution
context is gone. Use a fresh snapshot for the next run.

## ⚠️ Known Limitations

- Syscall numbers are specific to a Windows build. Stubs generated for one
  build may invoke the wrong service on another.
- This technique blinds **user-mode** hooks only. Kernel-level telemetry
  (ETW-TI, kernel callbacks) still observes the underlying operations —
  consistent with the paper's finding that bypassing user-mode hooks alone is
  not sufficient for reliable evasion.
- The SysWhispers3 revision used for the paper is not pinned here; record it
  if you need bit-exact reproduction.
