# T7: Symlink-based EDR Corruption

**DET classification:** Data Collection → EDR Agent Disruption

This technique is implemented based on the concept of symbolic link abuse to achieve EDR corruption. It exploits a file system flaw, often in conjunction with a vulnerable service or a Time-of-Check to Time-of-Use (TOCTOU) race condition, to force a system process to overwrite or corrupt a critical file belonging to the EDR agent.

By creating a file system symbolic link (symlink) that redirects a legitimate, **privileged write operation** (e.g., a file written by Process Monitor or a vulnerable boot service) to the EDR's executable or configuration file, an attacker can silently destroy the EDR's integrity. Upon the next system or service restart, the EDR agent may fail to initialize, resulting in a **complete loss of endpoint visibility**.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 66.7%** of its 36 outcomes — the highest L5 rate among all 22 evaluated techniques.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 33.3% | 0.0% | **66.7%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 66.7% | 66.7% | 66.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 100.0% | 0.0% | 100.0% | 100.0% | 100.0% |

**Interpretation.** This is the most effective technique in the benchmark, and it is completely payload-independent: the L5 rate is identical (66.7%) across all three payload families and both Windows environments. It reached L5 against Kaspersky, Microsoft Defender Antivirus, Elastic Security, and Huorong in every tested configuration, while Sophos and Bitdefender stopped every execution at L3. The paper's case study attributes this to a self-protection boundary failure: a privileged third-party write (the Process Monitor minifilter's boot-log output) was redirected through a symbolic link to overwrite the security product's executable before its service started, disabling the protection component before any payload inspection began. Sophos and Bitdefender contained the failure — their protected executables remained intact and the payloads were terminated at L3. Because this technique requires elevated administrator privileges, its outcomes characterize **post-compromise EDR self-protection**.

## ⚙️ Usage (Defensive Research)

The provided sample is a Proof-of-Concept demonstration using the Windows `mklink` utility, often leveraging the behavior of tools like **Process Monitor (Procmon)** or other system utilities that write to predictable, privileged locations during boot.

### Requirements
* **Elevated administrator privileges** are mandatory to create system symbolic links (see the paper's Table 7 for the required-privilege checklist).
* **Target EDR file path** must be correctly identified.
* The system requires a restart to trigger the privileged write operation (by Procmon or the vulnerable service) against the linked path.

### Detailed Execution Steps

To test this mechanism by hijacking Process Monitor's boot logging file (`Procmon.pmb`):

1.  **Prepare Process Monitor (Baseline Setup):**
    * Download and run Process Monitor (Procmon).
    * In the application menu, navigate to **Options** -> **Enable Boot Logging**.
    * This action configures the system to write log data to `C:\Windows\Procmon.pmb` during the next boot, which serves as our privileged write path.

2.  **Run the PoC Script:**
    * From an **elevated command prompt**, pass the path of the EDR file you intend to corrupt (e.g., the main EDR executable or a key configuration file) as the argument:
        ```bat
        T7-Symlink-Corruption.bat "C:\Program Files\Vendor\edr.exe"
        ```
    * The script refuses to run if the target path is missing or still the literal placeholder, prints the link it is about to create, and requires you to type `YES` before creating anything.
    * It then creates the symbolic link:
        ```bat
        mklink C:\Windows\Procmon.pmb "<your target file path>"
        ```

3.  **Reboot to Trigger the Corruption:**
    * By default the script does **not** reboot — it reports that the link is in place and how to undo it. Reboot manually, or pass `--reboot` to let the script run `shutdown /r /t 5` for you.
    * **Take a VM snapshot before rebooting.** The corruption occurs during the boot sequence, when Procmon attempts its privileged write. Once that has happened the target file has been overwritten.
    * To abort before rebooting, delete the link:
        ```bat
        del C:\Windows\Procmon.pmb
        ```

> **Warning:** This technique attempts to destroy a critical security component. Execute this PoC **only** in isolated VM environments with frequent, verifiable snapshots to prevent system damage.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Script | `T7-Symlink-Corruption.bat` |
| Prebuilt executable | n/a — the technique is a script plus an external tool |
| External requirement | Process Monitor (Procmon), configured for boot logging |
| External requirement | The path of the security-product file to target |

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Elevated Administrator.
- **Evasion-logic criterion:** the symbolic link redirected the Process
  Monitor boot-log output to the targeted security-product executable; the
  privileged boot-time write corrupted that executable; and the
  corresponding protection component **failed to start**.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

## ▶️ Running It Safely

The script is written to be **fail-safe by default**. It will:

1. require elevation;
2. refuse to run unless you have edited in a real target path (the shipped
   value is the literal placeholder `your_target_file_path_here`);
3. print the symlink it intends to create and require explicit confirmation
   before creating it;
4. **not reboot on its own** unless you pass `--reboot`;
5. tell you exactly how to remove the link if you abort.

Read the script before running it. The corruption only occurs at the next
boot, so between creating the link and rebooting you can always undo it with
`del C:\Windows\Procmon.pmb`.

## 🧹 Cleanup / Recovery

- Before rebooting: `del C:\Windows\Procmon.pmb` removes the link and nothing
  is damaged.
- After the boot-time write has occurred: the target file has been
  overwritten. Restore it from the product's installer or from a VM snapshot.
  **Snapshot before rebooting.**
- Remove the Procmon boot-logging configuration afterwards.

## ⚠️ Known Limitations

- The technique depends on Procmon's boot-logging write path and on the
  target product's self-protection behaviour; both are environment-specific.
- This technique is destructive by design. It is the only technique in the
  benchmark that can leave a security product non-functional after the test.
