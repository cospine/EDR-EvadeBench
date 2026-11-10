# T14: Thread Pool-based Process Injection (PoolParty)

**DET classification:** Detection → Memory Concealment

This technique, often referred to as "PoolParty," abuses the native **Windows Thread Pool** mechanism to execute code within a target process. Instead of creating a suspicious remote thread, the method involves:

1.  **Memory Allocation and Write:** Writing the payload (e.g., shellcode) into the target process's memory space.
2.  **Work Item Creation:** Creating a thread pool work item that points to the start address of the shellcode.
3.  **Queueing:** Queueing this malicious work item to the target process's existing thread pool (`QueueUserWorkItem`).

The code is executed by one of the target process's own legitimate thread pool workers. This execution path is often less monitored, as it avoids direct `CreateRemoteThread` calls and blends the malicious activity into the host process's normal thread management behavior.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 0.0%** of its 36 outcomes — no evaluated product allowed operational success.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 83.3% | 16.7% | 0.0% | 0.0% | **0.0%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |

**Interpretation.** PoolParty produced no L5 outcomes against any of the six evaluated products, and 83.3% of all executions were prevented at L1 (pre-execution); the remaining outcomes stopped at L2 (Bitdefender). The L5 rate is 0.0% across all three payload families, indicating that the detection of this technique is robust and payload-independent in the evaluated configurations. Despite avoiding `CreateRemoteThread`, the combination of cross-process memory allocation, protection changes, and work-item queuing into a remote thread pool appears to be well covered by current behavioral detection surfaces.

## ⚙️ Usage (Defensive Research)

The implementation requires compiling the PoolParty utility, which integrates the payload and handles the work item queuing logic.

### Prerequisites

* The source code for the PoolParty injection utility is required.
* A C++ compiler (e.g., Visual Studio) is required for compilation.
* **Administrator privileges** are often required for cross-process injection.

### Detailed Execution Steps

1.  **Prepare Payload and Compile:**
    * Obtain the source code for the PoolParty project.
    * Modify the project's payload section to integrate your own (AES-encrypted) EDR-EvadeBench shellcode; the shipped source contains a placeholder buffer only.
    * Compile the project to produce the injection executable (`PoolParty.exe`).

2.  **Execute the Injection:**
    * Run the compiled executable, specifying the target Process ID (PID) using the `-P` flag and the desired injection variant (e.g., `-V 8`).
        ```bash
        PoolParty.exe -V 8 -P pid
        ```
    * *Note: The argument `-V 8` is an example of a specific Thread Pool variant or injection method defined by the tool. Replace `pid` with the target process ID.*

3.  **Validation:**
    * Verify that the payload executes.
    * If EDR detection occurs, analyze the EDR alert to understand which phase failed: the memory allocation, the memory protection change, or the work item queuing itself.

> **Warning:** This technique is complex and involves cross-process memory manipulation. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `PoolParty/` (`main.cpp`, `PoolParty.cpp`, `ThreadPool.cpp`, `WorkerFactory.cpp`, `HandleHijacker.cpp`, `WinApi.cpp`, `Native.cpp`, `Misc.cpp` + headers) |
| Build project | `PoolParty.sln` / `PoolParty.vcxproj` (toolset `v143`) |
| Package manifest | `PoolParty/packages.config` — Boost 1.82.0 |
| Payload buffer / key | All-zero placeholders — supply your own |
| Prebuilt executable | Not distributed — `PoolParty.exe` is a **build output** ([BUILD.md](../BUILD.md)) |

## ⚙️ Dependencies

Boost 1.82.0 is declared in `packages.config` but the `packages/` folder is
**not vendored**. Restore it before building (`nuget restore PoolParty.sln`,
or simply build the solution in Visual Studio, which restores automatically).
`PoolParty.vcxproj` imports `..\packages\boost…` targets and fails without
them.

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a work item is submitted to the target
  process's thread pool, the payload executes via a worker-thread callback,
  and the C2 beacon is established.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## 🎛️ Variants

`-V <1..8>` selects the injection variant; `-P <pid>` takes a **numeric**
target PID; `-D` requests `SeDebugPrivilege`.

| Variant | Mechanism |
| :---: | :--- |
| 1 | WorkerFactory start-routine overwrite |
| 2 | `TP_WORK` insertion |
| 3 | `TP_WAIT` insertion |
| 4 | `TP_IO` insertion |
| 5 | `TP_ALPC` insertion |
| 6 | `TP_JOB` insertion |
| 7 | `TP_DIRECT` insertion |
| 8 | `TP_TIMER` insertion |

```bat
PoolParty.exe -V 8 -P 1234
```


## 🧹 Cleanup / Recovery

In-process injection into a live target. Terminate the target process and
revert the snapshot between runs.

## ⚠️ Known Limitations

- Boost must be restored first; the repository does not build as-cloned.
- This technique produced **no L5 outcomes against any product** in the
  paper's evaluation (0.0% across all payload families and both
  environments).
