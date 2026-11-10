# T12: COM-based Process Injection

**DET classification:** Detection → Memory Concealment

This technique leverages the Component Object Model (COM) environment to execute malicious code within a trusted process context, thereby avoiding common process injection heuristics. Instead of directly calling functions like `CreateRemoteThread` or `WriteProcessMemory` which are highly monitored by EDRs, this method utilizes legitimate COM call chains to facilitate the injection.

The core idea is to find a COM object whose instantiation or method invocation leads to memory allocation and execution within a target process. By setting up the payload correctly, the sequence of legitimate COM calls obscures the true malicious intent, allowing the payload to execute in a context that is implicitly trusted by the EDR's behavioral analysis engine. The PoC typically injects a malicious DLL (or shellcode loader) into a specified process.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 27.8%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 0.0% | 52.8% | 19.4% | 0.0% | **27.8%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 16.7% | 33.3% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 100.0% | 66.7% |

**Interpretation.** COM-based injection shows sharply divergent product behavior. All 6 outcomes against Huorong reached L5, and the Havoc and AdaptixC2 variants reached L5 against Microsoft Defender Antivirus in both environments (L5 in 4 of 6 outcomes). Sophos, Kaspersky, and Bitdefender stopped every variant at L2. Elastic Security produced no L5 outcomes: the paper's case study (COM-based injection with the Cobalt Strike payload on Windows 11 Enterprise) shows that, although the injection and the C2 callback initially succeeded (an L3 outcome), Elastic generated six alerts within a 43-ms window across three independent detection surfaces — remote memory write, injected-code execution (unbacked shellcode / anomalous call stack), and in-memory content — terminating the session before any command executed. Notably, no execution of this technique was prevented at L1 across all 36 outcomes, confirming that COM indirection defers detection to post-injection surfaces.

## ⚙️ Usage (Defensive Research)

The implementation requires compiling the COM injection tool (`com_inject.exe`) and providing a path to a malicious DLL (e.g., `TestDll.dll`) that contains the shellcode or final payload.

### Prerequisites

* A C++ compiler (e.g., Visual Studio or MinGW-w64) is required to compile the source code.
* A test DLL (`TestDll.dll`) which contains the malicious logic to be executed in the target process; integrate your own (AES-encrypted) payload — the shipped source contains a placeholder buffer only.
* The target process (PID or Name) for injection must be identified.

### Detailed Execution Steps

1.  **Compile the Injector:**
    * Compile the source code for the COM injection utility (`com_inject.exe`) using your build environment.

2.  **Execute the Injection:**
    * Run the compiled executable, specifying the full path to the malicious DLL you want to inject using the `-d` flag. The executable will handle the COM object creation and injection process.
        ```bash
        com_inject.exe -d yourpath\TestDll.dll
        ```
    * *Note: Ensure the DLL path is correct and accessible by the injector process.*

3.  **Validation:**
    * Post-execution, use tools like Process Explorer or a debugger to confirm that `TestDll.dll` has been loaded into the target process and that the payload (if included in the DLL) has executed successfully.

> **Warning:** Process injection techniques carry a risk of destabilizing the target process or system. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Injector source | `com_inject/com_inject.cpp`, `com_inject/com_inject.h` |
| Build project | `com_inject/com_inject.sln` |
| Demonstration DLL | `com_inject/TestDll/` — displays a MessageBox only |
| Shellcode generator | `com_inject/Shellcode/winexec.cpp` |
| Shellcode blob | `com_inject/Shellcode/notepad.bin` — **all-zero placeholder** |
| Payload buffer / key | All-zero placeholders in `com_inject.cpp` — supply your own |
| Prebuilt executables | Not distributed — `com_inject.exe` is a **build output** ([BUILD.md](../BUILD.md)) |

### Regenerating `notepad.bin`

`Shellcode/winexec.cpp` is a generator: it writes a benign
`WinExec("notepad", SW_SHOW)` shellcode stub to `notepad.bin`. Compile and
run it to replace the all-zero placeholder with a real (still benign) blob.

### Building the injector

`com_inject.cpp` uses `std::ifstream` with a `std::wstring` path, a Microsoft
standard-library extension, so it builds with **MSVC only** — use
`com_inject.sln`. (`TestDll` builds with MinGW as well.)

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** the payload is injected into the target process
  through a COM interface call chain, and the C2 beacon is established **from
  the target process** (not from the injector).
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## 🧹 Cleanup / Recovery

The injector writes into a live trusted process. Terminate that process and
revert the snapshot. Nothing is persisted to disk by the technique itself.

## ⚠️ Known Limitations

- The shipped `TestDll` is a benign MessageBox demonstration, not a payload
  carrier; the placeholder buffer in `com_inject.cpp` is also all-zero.
- The case study in the paper (Section IV-B) shows Elastic Security producing
  six alerts across three detection surfaces within 43 ms for this technique
  — the COM indirection conceals the API path, not the downstream effects.
- `notepad.bin` is not consumed by the injector at runtime (the injector takes
  a DLL path via `-d`); it exists only for the resource build.
