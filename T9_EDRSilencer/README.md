# T9: EDRSilencer

**DET classification:** Data Transmission → Telemetry Blocking

This technique utilizes the **Windows Filtering Platform (WFP)**, a built-in networking feature, to strategically block the outbound network traffic originating from EDR agent processes. By inserting a high-priority, restrictive filter rule into the WFP network stack, the EDRSilencer PoC prevents the EDR agent from successfully transmitting security events, alerts, or telemetry data back to the central management server.

The EDR agent may still detect the initial malicious activity locally and generate an alert, but the **alert cannot be transmitted or logged remotely**. This creates a "blind spot" for the security team, as the attack is executed but the evidence of the compromise is silenced, fulfilling the evasion objective. The tool typically targets IPv4 and IPv6 traffic specifically for the EDR process.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 33.3%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 16.7% | 33.3% | 0.0% | 16.7% | **33.3%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 33.3% | 33.3% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 100.0% | 100.0% | 0.0% |

**Interpretation.** Blocking telemetry via WFP filters achieved L5 against Elastic Security and Huorong in all tested configurations, and reached L4 (commands sent, but the session disrupted within the timeout) against Microsoft Defender Antivirus in every configuration. Sophos and Bitdefender stopped all outcomes at L2, and Kaspersky at L1. As the only Transmission-stage (Telemetry Blocking) technique in the library, its aggregate should not be generalized to telemetry-blocking techniques as a whole. The L5 rate is identical across all three payload families (33.3%), consistent with a mechanism whose success is gated by privileges and product self-protection rather than payload artifacts. This technique requires elevated administrator privileges (see the paper's Table 7).

## ⚙️ Usage (Defensive Research)

The implementation uses the `EDRSilencer.exe` utility to interact with the Windows Filtering Platform, installing a temporary or persistent network filter.

### Prerequisites

* The `EDRSilencer.exe` executable must be **built from the source in this folder** (`EDRSilencer.c`, `utils.c`); no prebuilt executable is distributed — see [BUILD.md](../BUILD.md).
* **Elevated administrator privileges** are mandatory to install and modify WFP filter rules.

### Compile EDRSilencer

If you need to build the tool from source, use the following MinGW command. Ensure you have the source files available.
```bash
x86_64-w64-mingw32-gcc EDRSilencer.c utils.c -o EDRSilencer.exe -lfwpuclnt
```
### Detailed Execution Steps
1.  **Stage the Executable:**
    * Ensure the `EDRSilencer.exe` executable is available in your working directory.
2.  **Execute the Silencing Command:**
    * Run the executable with Administrator privileges, specifying the command to block EDR communications (often by identifying and targeting the specific EDR process).

    ```bash
    EDRSilencer.exe blockedr
    ```

    * Note: The argument `blockedr` is used to automatically detect known EDR processes and add WFP filters to block their IPv4 and IPv6 outbound traffic.
3.  **Validation:**
    * After execution, confirm the EDR agent's telemetry is blocked (e.g., by running a benign command that should trigger an alert, and verifying that no alert appears on the central EDR console).
    * **Crucially, remember to revert the WFP rule** after testing using the tool's built-in cleanup function to restore network functionality:
    ```bash
    EDRSilencer.exe unblockall
    ```
> **Warning:** Modifying the Windows Filtering Platform can affect system networking. Execute this PoC **only** in isolated VM environments. Always ensure the WFP rules are cleaned up immediately after testing.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `EDRSilencer.c`, `utils.c`, `utils.h` |
| Prebuilt executable | Not distributed — `EDRSilencer.exe` is a **build output** ([BUILD.md](../BUILD.md)) |

`EDRSilencer.c` compiles cleanly with MinGW-w64 gcc 14.2.0:

```bash
x86_64-w64-mingw32-gcc EDRSilencer.c utils.c -o EDRSilencer.exe -lfwpuclnt
```

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Elevated Administrator.
- **Evasion-logic criterion:** EDR telemetry channels are blocked via WFP
  filters, and a test alert generated on the endpoint **does not appear on
  the management server**.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

## ⚙️ Commands

| Command | Effect |
| :--- | :--- |
| `EDRSilencer.exe blockedr` | Detect known EDR processes and block their IPv4/IPv6 outbound traffic |
| `EDRSilencer.exe block "<full path>"` | Block the outbound traffic of one specific process |
| `EDRSilencer.exe unblockall` | Remove every WFP filter added by this tool |
| `EDRSilencer.exe unblock <filter id>` | Remove one filter by id |
| `EDRSilencer.exe -h` | Print usage |

## 🧹 Cleanup / Recovery — required

**Always run `EDRSilencer.exe unblockall` after testing.** The filters this
tool installs persist beyond the process lifetime and will keep blocking
network traffic until removed. Verify with `netsh wfp show filters` if in
doubt, then revert the snapshot.

## ⚠️ Known Limitations

- `blockedr` relies on a built-in list of known EDR process names; a product
  not on that list is not covered.
- This is the only Transmission-stage technique in the library, so its
  aggregate should not be generalised to telemetry blocking as a whole
  (paper Section IV-B).
