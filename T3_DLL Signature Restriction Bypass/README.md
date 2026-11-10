# T3: DLL Signature Restriction

**DET classification:** Data Collection → EDR Sensor Disruption

This implementation applies a process signature policy to block non-Microsoft DLL injection. It targets sensor DLLs that would otherwise be loaded into the process. The mechanism and validation criterion match the companion manuscript's T3 entry.

The directory retains its earlier name, `T3_DLL Signature Restriction Bypass`, so existing project paths remain valid. The implementation name used in the manuscript and released results is **DLL Signature Restriction**.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 13.9%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 16.7% | 38.9% | 16.7% | 13.9% | **13.9%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 16.7% | 25.0% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 66.7% | 16.7% |

**Interpretation.** This technique achieved only limited bypass depth. Four products (Sophos, Kaspersky, Bitdefender, and Elastic Security) produced no L5 outcomes: Elastic prevented every execution at L1, while Sophos and Bitdefender stopped all outcomes at L2 and Kaspersky between L2 and L4. Operational success concentrated on Huorong (L5 in 4 of 6 outcomes), with a single L5 against Microsoft Defender Antivirus. Most evaluated products prevented the tested implementation before operational success; these final labels do not identify the products' internal detection signals.

## 📦 Source and build

| Item | Status |
| :--- | :--- |
| Source | `PreventDll/PreventDll.cpp` |
| Helper header | `PreventDll/lazy_importer.hpp` |
| Payload buffer / key | All-zero placeholders |
| Prebuilt sample executable | Not distributed |

Source layout and build requirements are documented in [BUILD.md](../BUILD.md). The cited source is [ired.team's process-mitigation example](https://www.ired.team/offensive-security/defense-evasion/preventing-3rd-party-dlls-from-injecting-into-your-processes).

## 🧪 Validation criteria

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** process signature policy enabled; non-Microsoft DLL injection blocked.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and the beacon answers the prescribed test commands.

## 🧹 Cleanup / Recovery

Terminate the child process and restore the baseline snapshot after testing. The signature policy applies to the child process.

## Scope

The process signature policy does not disable system-wide signature verification. The released result table records the outcomes of the selected implementation, payload families, products and environments.
