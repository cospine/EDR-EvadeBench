# T6: Kernel Callback Removal

**DET classification:** Data Collection → EDR Agent Disruption

This technique targets the heart of EDR's kernel-level monitoring by utilizing a **Bring Your Own Vulnerable Driver (BYOVD)** approach to gain kernel execution access. Once executed in kernel space, the malicious code enumerates system notification routines and callbacks, such as:

* `PsSetCreateProcessNotifyRoutine` (Process creation monitoring)
* `PsSetCreateThreadNotifyRoutine` (Thread creation monitoring)
* `PsSetLoadImageNotifyRoutine` (Module/DLL loading monitoring)
* `CmRegisterCallback` (Registry access monitoring)
* MiniFilter Callbacks (File system activity monitoring)

The PoC's objective is to locate and unregister the entries belonging to the EDR agent, effectively **blinding the EDR's core sensors** at the lowest level of the operating system.

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

**Interpretation.** All L5 outcomes of this technique concentrated on a single product: Microsoft Defender Antivirus, where every one of the 6 outcomes reached operational success after the kernel callbacks were removed. Every other product prevented all executions at L1 or L2 (Bitdefender and Huorong at L1; Sophos, Kaspersky, and Elastic Security at L2), indicating effective protection of kernel callback registrations or detection of the BYOVD chain itself. The L5 rate is identical across all three payload families (16.7%), consistent with a mechanism whose success is gated by privileges and product self-protection rather than by payload artifacts. Because this technique requires elevated privileges and a vulnerable signed driver, its outcomes characterize **post-compromise EDR self-protection**, not prevention of initial access or privilege escalation.

## ⚙️ Usage (Defensive Research)

The implementation requires a driver file (`echo_driver.sys`) which contains the necessary code to gain kernel access and perform the callback removal, and a user-mode executable (`RealBlindingEDR.exe`) to trigger the operation.

### Prerequisites

* The driver file (`echo_driver.sys`) is required, and the user-mode controller must be **built from the source in this folder** (`RealBlindingEDR.exe` is a build output, not distributed — see [BUILD.md](../BUILD.md)).
* **Elevated administrator privileges** are mandatory for driver interaction (see the paper's Table 7 for the required-privilege checklist).

### Detailed Execution Steps

1.  **Stage the Files:**
    * Ensure the driver file (`echo_driver.sys`) is present and that you have built `RealBlindingEDR.exe` from the source in `RealBlindingEDR/`.
    * Copy the driver file to the C drive root as required by the PoC logic:
        ```bash
        copy /Y echo_driver.sys c:\echo_driver.sys
        ```

2.  **Execute the Callback Removal:**
    * Run the user-mode executable with Administrator privileges, providing the path to the staged driver and the command parameter (`1`).
    * *Note: This process typically involves the executable loading the driver, executing the kernel-level routine to remove EDR callbacks, and then potentially unloading the driver.*
        ```bash
        RealBlindingEDR.exe c:\echo_driver.sys 1
        ```

3.  **Validation:**
    * Post-execution, attempts to run a malicious payload (e.g., shellcode execution) should now bypass the EDR's behavioral monitoring hooks that relied on the removed callbacks.

> **Warning:** This technique involves loading a kernel driver with full system access. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots. **Kernel tampering can lead to system instability.**

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| User-mode source | `RealBlindingEDR/RealBlindingEDR/RealBlindingEDR.cpp` and `.h` |
| Build project | `RealBlindingEDR/RealBlindingEDR.sln` (Visual Studio) |
| Kernel driver | `echo_driver.sys` — **binary only, source not included** |
| Prebuilt executable | Not distributed — `RealBlindingEDR.exe` is a **build output** ([BUILD.md](../BUILD.md)) |

The driver's size, SHA-256 and observed provenance are recorded in
[../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).

## ⚠️ Auditability Caveat

The callback-enumeration and callback-removal logic lives in
`echo_driver.sys`, which ships as an opaque binary with **no source and no
build project**. The user-mode code in this folder is a controller: it loads
the driver, opens a device, and issues `DeviceIoControl` requests. It does not
itself enumerate or unregister callbacks.

The controller supports two driver protocols:

| `Driver_Type` | Device opened | IOCTLs used |
| :---: | :--- | :--- |
| `1` (default, `echo_driver.sys`) | `\\.\EchoDrv` | `0x9e6a0594` (init), `0xe6224248` (acquire handle), `0x60a26124` (kernel read/write) |
| `2` | `\\.\DBUtil_2_3` | `0x9B0C1EC4` (read), `0x9B0C1EC8` (write) |

Because the device name and protocol belong to the driver, **the shipped
driver must match the controller**; a different `echo_driver.sys` build with
different IOCTL codes will not work.

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Elevated Administrator **plus a vulnerable signed
  driver** (BYOVD).
- **Evasion-logic criterion:** the targeted kernel callback routines are
  removed from their callback arrays, and the corresponding system events no
  longer trigger EDR notifications. Confirm the callback entry exists before
  the run and is absent afterwards.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

Because this technique requires elevation and a vulnerable driver, its
outcomes characterise **post-compromise EDR self-protection**, not prevention
of initial access (paper Section 3).

## 🧹 Cleanup / Recovery

1. Unload the driver (the sample's `UnloadDrive` invokes `NtUnloadDriver`).
2. Delete the service registry key the sample created under
   `HKLM\System\CurrentControlSet\Services\<RandomName>`.
3. Confirm no handle to `\\.\EchoDrv` remains, then revert the snapshot.

## ⚠️ Known Limitations

- On a driver whose signing certificate has been revoked, loading fails with
  `0xC0000603`; the sample prints a message in that case.
- Driver version, signing status and redistribution terms are unrecorded —
  see [../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).
