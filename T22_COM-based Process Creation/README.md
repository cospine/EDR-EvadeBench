# T22: COM-based Process Creation

**DET classification:** Detection → Logic Bypass

This technique exploits the Component Object Model (COM) framework by utilizing specific COM interfaces that expose process creation functionality (e.g., interfaces associated with help or diagnostic services, like `IHxHelpPaneServer`).

The core evasion logic relies on:

1.  **Instantiating a Trusted COM Object:** Creating an instance of a COM object that has the privilege and functionality to launch other processes.
2.  **Abusing an Exposed Method:** Calling a method on that interface (e.g., `Execute` or similar) and passing the path to the malicious executable as an argument.

By using a trusted COM call chain, the resulting process creation event is attributed to the trusted COM host (e.g., `dllhost.exe` or another system process) rather than the attacker's executable, lowering the overall behavioral anomaly score assigned by the EDR. This constitutes a **Logic Bypass** of standard process monitoring heuristics.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 22.2%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 33.3% | 33.3% | 11.1% | 0.0% | **22.2%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 33.3% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** Launching the payload through a trusted COM interface reached operational success against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes), but not against the other four products: Kaspersky and Elastic Security prevented every execution at L1, while Sophos and Bitdefender stopped all outcomes at L2. This split indicates that products tracking process lineage across intermediate COM hosts — or applying static detection to the launched payload — are not fooled by the trusted parent attribution, whereas products keyed primarily to direct `CreateProcess`-style heuristics remain vulnerable. The result is payload-dependent (0.0% with Cobalt Strike vs. 33.3% with Havoc and AdaptixC2).

## ⚙️ Usage (Defensive Research)

The implementation requires compiling an executable (`test.exe`) that handles the COM object instantiation and method calling, and providing the full path to the payload executable to be launched.

### Prerequisites

* The source code for the COM client utility (e.g., based on the `IHxHelpPaneServer` abuse) is required.
* The executable to be launched (your own payload, e.g., `payload.exe`; the repository does not distribute any exe/bin carrying payload characteristics).
* A C++ compiler (e.g., Visual Studio) is required for compilation.

### Detailed Execution Steps

1.  **Prepare the Payload:**
    * Ensure your payload executable (the file you wish to launch) is compiled and its full path is known.

2.  **Compile the COM Client:**
    * Compile the source code for the COM abuse utility to produce the final executable (`test.exe`).

3.  **Execute the COM Creation:**
    * Run the compiled client executable, providing the full path to the target executable you wish to launch.

    ```bash
    test.exe "C:\Path\To\Payload.exe"
    ```

4.  **Validation:**
    * Verify that the payload executable successfully launched.
    * Use Process Explorer or EDR telemetry analysis tools to examine the parent process of the launched payload. If successful, the parent process should be the trusted COM host (e.g., `dllhost.exe`), not `test.exe`.

> **Warning:** COM interface abuse can be fragile, as CLSIDs and method behaviors may change across Windows versions. Execute this PoC **only** in isolated VM environments.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `IHxHelpPaneServer.cpp` |
| Build project | None — compile the single source directly |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

Compiles cleanly with MinGW-w64 gcc 14.2.0:

```bash
x86_64-w64-mingw32-gcc "IHxHelpPaneServer.cpp" -lole32 -loleaut32 -luuid -lstdc++ -municode -o IHxHelpPaneServer.exe
```

> **Note:** this file was previously named `IHxHelpPaneServer.c`. It contains
> C++ (an interface declaration with virtual methods and
> `__declspec(uuid)`), so the `.c` extension was incorrect and the file could
> not compile as C. It has been renamed to `.cpp`.

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a new process is created via a trusted COM
  interface, and the C2 beacon is established **from the child process spawned
  by a trusted parent process** (e.g. `dllhost.exe`) rather than from this
  executable.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

Verify by inspecting the child process's parent: it should be the trusted COM
host, not `IHxHelpPaneServer.exe`.

## ▶️ Usage

```bat
IHxHelpPaneServer.exe "C:\Path\To\Payload.exe"
```

## 🧹 Cleanup / Recovery

The launched payload process runs independently. Terminate it and revert the
snapshot. Nothing is persisted to disk or the registry by this technique.

## ⚠️ Known Limitations

- COM interfaces and CLSIDs can change between Windows versions; the
  `IHxHelpPaneServer` CLSID targeted here is version-specific.
- The technique fails cleanly with a diagnostic if the COM object cannot be
  instantiated (for example if the Help Pane component is not present on the
  target SKU).
