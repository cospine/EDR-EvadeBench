# T4: Hook Overwriting

**DET classification:** Data Collection → EDR Sensor Disruption

This technique is a targeted attack against user-mode API hooking implemented by EDR agents in foreign processes. When an EDR injects its DLL into a target process (e.g., `explorer.exe` or `notepad.exe`) and places hooks (e.g., `JMP` instructions) at the beginning of critical API functions, this PoC aims to neutralize those hooks.

The **Hook Overwriting** process involves:

1.  **Identification:** Identifying the target process (PID) and the hooked API function (e.g., `NtAllocateVirtualMemory`).
2.  **Original Byte Restoration:** Reading the original, unhooked bytes from a clean copy of the DLL (e.g., from disk) or calculating the expected original prologue bytes.
3.  **Remote Write:** Using memory manipulation APIs (like `WriteProcessMemory`, which must itself be unhooked or bypassed) to remotely overwrite the hooked function prologue in the target process's memory with the original bytes.

This successfully removes the EDR's intercepting logic from the target process, creating a blind spot for subsequent malicious activity within that process.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 22.2%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 16.7% | 52.8% | 2.8% | 5.6% | **22.2%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 16.7% | 33.3% | 16.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 100.0% | 33.3% |

**Interpretation.** Hook overwriting fully succeeded only against Huorong, where all 6 outcomes reached L5, indicating that its user-mode hooks were removed without triggering compensating sensors. Microsoft Defender Antivirus reached L5 in 2 of 6 outcomes. Sophos and Bitdefender stopped every execution at L2, Kaspersky between L2 and L4, and Elastic Security prevented all outcomes at L1 — showing that hook-integrity checks, kernel-level telemetry, or static detection still cover this technique for most evaluated products. Note that, per the paper's validation protocol, this technique is validated with the target product's hooks present, since manipulating EDR hooks is its functional prerequisite.

## ⚙️ Usage (Defensive Research)

The implementation requires a compiled executable (`Hook_Overwriting.exe`) that performs the remote memory operation against a running, hooked target process.

### Prerequisites

* The source code for the hook overwriting project is required.
* A C/C++ compiler (e.g., Visual Studio) is required for compilation.
* **Administrator privileges** are necessary to interact with most target processes (e.g., to gain sufficient handle access via `OpenProcess`).

### Detailed Execution Steps

1.  **Prepare the Target:**
    * Launch a benign process (e.g., `notepad.exe`) that you know the target EDR is hooking.
    * Find the Process ID (PID) of this target process using Task Manager or Process Explorer.

2.  **Compile the Overwriter:**
    * Compile the source code for the utility to produce the final executable (`Hook_Overwriting.exe`).

3.  **Execute the Hook Removal:**
    * Run the compiled executable, specifying the PID of the hooked target process as an argument:
        ```bash
        Hook_Overwriting.exe <PID_of_Target_Process>
        # Example: Hook_Overwriting.exe 4567
        ```

4.  **Validation:**
    * Verify the successful removal of the hook using a remote debugger or memory scanning tool on the target process's memory space.
    * Run a secondary, suspicious action (e.g., injection of a benign payload) into the target process and verify that the EDR fails to detect the second action, confirming the success of the initial hook removal.

> **Warning:** This technique involves complex cross-process memory manipulation. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `Hook_Overwriting.cpp` |
| Payload buffer | All-zero placeholder — supply your own |
| AES key | All-zero placeholder — supply your own |
| Build project | None — compile the single source directly |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

This project compiles cleanly with MinGW-w64 gcc 14.2.0; see
[BUILD.md](../BUILD.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User (paper Table 7). In practice,
  opening an arbitrary foreign process with the access rights this sample
  requests may require elevation; if `OpenProcess` fails, record the privilege
  you used.
- **Evasion-logic criterion:** the original EDR hook trampoline is restored,
  and subsequent API calls route to the system service without EDR
  interception. Confirm by scanning the target function's prologue in the
  remote process **before** and **after** the overwrite.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

This technique is validated **with the target product's hooks present**,
because manipulating EDR hooks is its functional prerequisite (paper
Section 3-B).

## 🧹 Cleanup / Recovery

The overwrite mutates another live process's memory. Terminate the target
process and revert the VM snapshot before the next run; do not reuse a target
whose hooks were already overwritten, or the "before" state will no longer be
observable.

## ⚠️ Known Limitations

- The sample must itself issue the remote write. If the product hooks
  `WriteProcessMemory`, the write needs its own unhooking path — the warning
  in this README is accurate.
- Hook layout differs per product and per build; there is no universal
  "original bytes" value.
