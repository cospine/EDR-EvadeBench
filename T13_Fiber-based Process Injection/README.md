# T13: Fiber-based Process Injection

**DET classification:** Detection → Memory Concealment

This technique leverages the Windows **Fiber** mechanism—user-mode constructs for cooperative multitasking—to execute malicious payloads. Unlike standard threads, Fiber creation (`CreateFiber`) and switching (`SwitchToFiber`) often generate less suspicious telemetry and are typically less scrutinized by EDR behavioral sensors.

The primary goal is to **mask the execution context** and **evade call stack analysis**. By injecting the payload into a Fiber context associated with a legitimate host thread (like the PhantomThread method), the malicious execution occurs without creating a distinct, easily identifiable remote thread artifact, effectively hiding the operation from standard EDR injection heuristics.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 22.2%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 33.3% | 16.7% | 27.8% | 0.0% | **22.2%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 33.3% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** Executing the payload inside a fiber context reached operational success against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes), but not against the other four products. Sophos and Bitdefender prevented every execution at L1, Elastic Security terminated every session at L3 (after C2 establishment, before any command), and Kaspersky stopped all outcomes at L2 or L3. The result is payload-dependent (0.0% with Cobalt Strike vs. 33.3% with Havoc and AdaptixC2), indicating that fiber-context execution alone does not conceal payload-specific artifacts from products that correlate memory operations and execution context.

## ⚙️ Usage (Defensive Research)

The implementation is typically based on the **ImmoralFiber** project's `PhantomThread` technique, which requires modifying the project to integrate the EDR-EvadeBench base payload.

### Prerequisites

* The source code for the injection utility (`PhantomThread.exe`) and the payload DLL (`PhantomThreadPayload.dll`) is required; both are **build outputs** of the included Visual Studio solution, not distributed binaries — see [BUILD.md](../BUILD.md).
* A C++ compiler (e.g., Visual Studio) is required for compilation.
* **Administrator privileges** are often required for cross-process injection.

### Detailed Execution Steps

1.  **Prepare Payload and Compile:**
    * Obtain the source code for the Fiber injection project.
    * Modify the project to integrate your own (AES-encrypted) EDR-EvadeBench shellcode loader (or a wrapper DLL, `PhantomThreadPayload.dll`) as the payload to be injected; the shipped source contains a placeholder buffer only.
    * Compile the project to produce the injection executable (`PhantomThread.exe`) and the payload DLL (`PhantomThreadPayload.dll`).

2.  **Execute the Injection:**
    * Run the compiled executable, using the necessary command-line arguments to initiate the injection into a target process (e.g., `explorer.exe`).
        ```bash
        # Example for validating functionality (using 'c' as a common flag to initiate command)
        PhantomThread.exe c
        ```

3.  **Validation:**
    * Verify that the payload executes successfully in the context of the target process without triggering an EDR alert.
    * Attempt to examine the target process's thread list using debugging tools to confirm that the execution is associated with a Fiber or a carefully manipulated thread context.

> **Warning:** Fiber-based injection is complex and carries a risk of destabilizing the target process. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Solution | `ImmoralFiber/ImmoralFiber.sln` |
| Components | `BasicFiber` (benign target), `PoisonFiber` (remote fiber injection), `PhantomThread` (callstack masking), `PhantomThreadPayload` (payload DLL) |
| Payload resources | `c-shellcode-msgbox.bin`, `payload_x64_3.bin` — **all-zero placeholders** |
| Upstream documentation | `ImmoralFiber/README.md` (the upstream project's own README) |
| Prebuilt executables | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

`BasicFiber/BasicFiber.cpp` compiles cleanly with MinGW-w64 gcc 14.2.0. The
resource-bearing projects (`PoisonFiber`, `PhantomThreadPayload`,
`PhantomThread`) build with MSVC via the solution; their `.rc` files embed the
all-zero placeholder blobs, so an out-of-the-box build produces inert
resources — replace the placeholder before functional testing.

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a fiber is created and scheduled within the
  target process, payload execution is transferred to the fiber context, and
  the C2 beacon is established from the target process.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## 📄 Upstream vs. Benchmark Documentation

`ImmoralFiber/README.md` is the **upstream project's** README, retained for
reference. Two things to keep separate when reading it:

- It is written for the upstream project, not for this benchmark.
- It states *"Tested on Windows 10 build 19044"*. That is an upstream testing
  note. The benchmark's evaluation environment is Windows 11 Enterprise
  (build 26200) and Windows Server 2025 (build 26100), per Table 8 of the
  paper. The upstream note does not describe the benchmark's environment.
- The image references in the upstream README (`Images/…`) are not included in
  this repository; those files were not redistributed.

## 🧹 Cleanup / Recovery

Fiber injection manipulates a remote process's fiber objects. Terminate the
injected process and revert the snapshot; overwriting a dormant fiber's code
(the `-do` variant) can leave the target process unstable.

## ⚠️ Known Limitations

- The `PoisonFiber` thread-enumeration path is inherently noisy (the upstream
  documentation notes the ETW-TI and RWX-scanning telemetry it generates).
- Fibers must already be in use in the target process; FLS-based variants
  additionally require fiber local storage to be in use.
