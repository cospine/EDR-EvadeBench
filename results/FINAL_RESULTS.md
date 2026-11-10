# Complete Final Results

All 828 final case labels follow the manuscript result table: 792 non-baseline cases and 36 T0 cases. The canonical machine-readable dataset is [outcomes_scored.csv](outcomes_scored.csv). This file and [CASE_SUMMARIES.md](CASE_SUMMARIES.md) are generated from that dataset; both use the repository case identifiers.

## Outcome definitions

| Level | Meaning | Criterion |
| --- | --- | --- |
| L1 | Pre-execution Prevention | The product blocked the sample before process creation. |
| L2 | Pre-C2 Prevention | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| L3 | Pre-command Prevention | C2 was established, but the product terminated the session before any command was sent. |
| L4 | Command-stage Prevention | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| L5 | Operational Success | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

T0 uses the same AES-based encryption and runtime decryption, with no additional evasion mechanism. Every case contributes one final label after the repetition procedure. T0 is excluded from PSD and BDD. See [the test protocol](../framework/TEST_PROTOCOL.md) and [data dictionary](DATA_DICTIONARY.md).

## Totals

| Item | Count |
| --- | --- |
| All cases | 828 |
| Non-baseline cases | 792 |
| T0 cases | 36 |
| Non-baseline L5 cases | 182 |
| Overall L5 proportion | 23.0% |

## Product summary (PSD)

| Group | Cases | L1 | L2 | L3 | L4 | L5 | L1 % | L2 % | L3 % | L4 % | L5 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sophos | 132 | 24 | 102 | 6 | 0 | 0 | 18.2% | 77.3% | 4.5% | 0.0% | 0.0% |
| Kaspersky | 132 | 36 | 55 | 15 | 4 | 22 | 27.3% | 41.7% | 11.4% | 3.0% | 16.7% |
| Bitdefender | 132 | 18 | 108 | 6 | 0 | 0 | 13.6% | 81.8% | 4.5% | 0.0% | 0.0% |
| Elastic | 132 | 88 | 19 | 13 | 0 | 12 | 66.7% | 14.4% | 9.8% | 0.0% | 9.1% |
| Huorong | 132 | 24 | 14 | 14 | 4 | 76 | 18.2% | 10.6% | 10.6% | 3.0% | 57.6% |
| DefenderAV | 132 | 22 | 7 | 24 | 7 | 72 | 16.7% | 5.3% | 18.2% | 5.3% | 54.5% |

## Implementation summary (BDD)

| Group | Cases | L1 | L2 | L3 | L4 | L5 | L1 % | L2 % | L3 % | L4 % | L5 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | 36 | 6 | 14 | 6 | 0 | 10 | 16.7% | 38.9% | 16.7% | 0.0% | 27.8% |
| T2 | 36 | 6 | 14 | 6 | 0 | 10 | 16.7% | 38.9% | 16.7% | 0.0% | 27.8% |
| T3 | 36 | 6 | 14 | 6 | 5 | 5 | 16.7% | 38.9% | 16.7% | 13.9% | 13.9% |
| T4 | 36 | 6 | 19 | 1 | 2 | 8 | 16.7% | 52.8% | 2.8% | 5.6% | 22.2% |
| T5 | 36 | 12 | 14 | 4 | 0 | 6 | 33.3% | 38.9% | 11.1% | 0.0% | 16.7% |
| T6 | 36 | 12 | 18 | 0 | 0 | 6 | 33.3% | 50.0% | 0.0% | 0.0% | 16.7% |
| T7 | 36 | 0 | 0 | 12 | 0 | 24 | 0.0% | 0.0% | 33.3% | 0.0% | 66.7% |
| T8 | 36 | 24 | 6 | 0 | 0 | 6 | 66.7% | 16.7% | 0.0% | 0.0% | 16.7% |
| T9 | 36 | 6 | 12 | 0 | 6 | 12 | 16.7% | 33.3% | 0.0% | 16.7% | 33.3% |
| T10 | 36 | 4 | 20 | 4 | 0 | 8 | 11.1% | 55.6% | 11.1% | 0.0% | 22.2% |
| T11 | 36 | 4 | 16 | 3 | 0 | 13 | 11.1% | 44.4% | 8.3% | 0.0% | 36.1% |
| T12 | 36 | 0 | 19 | 7 | 0 | 10 | 0.0% | 52.8% | 19.4% | 0.0% | 27.8% |
| T13 | 36 | 12 | 6 | 10 | 0 | 8 | 33.3% | 16.7% | 27.8% | 0.0% | 22.2% |
| T14 | 36 | 30 | 6 | 0 | 0 | 0 | 83.3% | 16.7% | 0.0% | 0.0% | 0.0% |
| T15 | 36 | 12 | 18 | 0 | 0 | 6 | 33.3% | 50.0% | 0.0% | 0.0% | 16.7% |
| T16 | 36 | 6 | 18 | 2 | 2 | 8 | 16.7% | 50.0% | 5.6% | 5.6% | 22.2% |
| T17 | 36 | 16 | 14 | 2 | 0 | 4 | 44.4% | 38.9% | 5.6% | 0.0% | 11.1% |
| T18 | 36 | 20 | 10 | 2 | 0 | 4 | 55.6% | 27.8% | 5.6% | 0.0% | 11.1% |
| T19 | 36 | 12 | 15 | 3 | 0 | 6 | 33.3% | 41.7% | 8.3% | 0.0% | 16.7% |
| T20 | 36 | 6 | 18 | 2 | 0 | 10 | 16.7% | 50.0% | 5.6% | 0.0% | 27.8% |
| T21 | 36 | 0 | 22 | 4 | 0 | 10 | 0.0% | 61.1% | 11.1% | 0.0% | 27.8% |
| T22 | 36 | 12 | 12 | 4 | 0 | 8 | 33.3% | 33.3% | 11.1% | 0.0% | 22.2% |

## DET membership

| Strategy | Stage | Implementations |
| --- | --- | --- |
| EDR Sensor Disruption | Collection | T1, T2, T3, T4, T5 |
| EDR Agent Disruption | Collection | T6, T7, T8 |
| Telemetry Blocking | Transmission | T9 |
| Memory Concealment | Detection | T10, T11, T12, T13, T14, T15, T16 |
| Obfuscation | Detection | T17, T18, T19, T20 |
| Logic Bypass | Detection | T21, T22 |

## Layer 2 BDD

| Group | Cases | L1 | L2 | L3 | L4 | L5 | L1 % | L2 % | L3 % | L4 % | L5 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EDR Sensor Disruption | 180 | 36 | 75 | 23 | 7 | 39 | 20.0% | 41.7% | 12.8% | 3.9% | 21.7% |
| EDR Agent Disruption | 108 | 36 | 24 | 12 | 0 | 36 | 33.3% | 22.2% | 11.1% | 0.0% | 33.3% |
| Telemetry Blocking | 36 | 6 | 12 | 0 | 6 | 12 | 16.7% | 33.3% | 0.0% | 16.7% | 33.3% |
| Memory Concealment | 252 | 68 | 103 | 26 | 2 | 53 | 27.0% | 40.9% | 10.3% | 0.8% | 21.0% |
| Obfuscation | 144 | 54 | 57 | 9 | 0 | 24 | 37.5% | 39.6% | 6.2% | 0.0% | 16.7% |
| Logic Bypass | 72 | 12 | 34 | 8 | 0 | 18 | 16.7% | 47.2% | 11.1% | 0.0% | 25.0% |

## Layer 1 BDD

| Group | Cases | L1 | L2 | L3 | L4 | L5 | L1 % | L2 % | L3 % | L4 % | L5 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Collection | 288 | 72 | 99 | 35 | 7 | 75 | 25.0% | 34.4% | 12.2% | 2.4% | 26.0% |
| Transmission | 36 | 6 | 12 | 0 | 6 | 12 | 16.7% | 33.3% | 0.0% | 16.7% | 33.3% |
| Detection | 468 | 134 | 194 | 43 | 2 | 95 | 28.6% | 41.5% | 9.2% | 0.4% | 20.3% |

## Payload summary

| Group | Cases | L1 | L2 | L3 | L4 | L5 | L1 % | L2 % | L3 % | L4 % | L5 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CobaltStrike | 264 | 66 | 125 | 44 | 6 | 23 | 25.0% | 47.3% | 16.7% | 2.3% | 8.7% |
| Havoc | 264 | 73 | 89 | 9 | 7 | 86 | 27.7% | 33.7% | 3.4% | 2.7% | 32.6% |
| AdaptixC2 | 264 | 73 | 91 | 25 | 2 | 73 | 27.7% | 34.5% | 9.5% | 0.8% | 27.7% |

## Environment summary

| Group | Cases | L1 | L2 | L3 | L4 | L5 | L1 % | L2 % | L3 % | L4 % | L5 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Win11Enterprise | 396 | 107 | 151 | 39 | 7 | 92 | 27.0% | 38.1% | 9.8% | 1.8% | 23.2% |
| Server2025 | 396 | 105 | 154 | 39 | 8 | 90 | 26.5% | 38.9% | 9.8% | 2.0% | 22.7% |

## Complete case register

| Case ID | Implementation | Name | Payload | Product | Environment | Baseline | Level |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T0-CS-SOPH-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Sophos | Win11Enterprise | Yes | L1 |
| T0-HV-SOPH-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Sophos | Win11Enterprise | Yes | L1 |
| T0-AX-SOPH-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Sophos | Win11Enterprise | Yes | L1 |
| T0-CS-SOPH-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Sophos | Server2025 | Yes | L1 |
| T0-HV-SOPH-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Sophos | Server2025 | Yes | L1 |
| T0-AX-SOPH-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Sophos | Server2025 | Yes | L1 |
| T0-CS-KASP-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Kaspersky | Win11Enterprise | Yes | L1 |
| T0-HV-KASP-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Kaspersky | Win11Enterprise | Yes | L1 |
| T0-AX-KASP-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Kaspersky | Win11Enterprise | Yes | L1 |
| T0-CS-KASP-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Kaspersky | Server2025 | Yes | L1 |
| T0-HV-KASP-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Kaspersky | Server2025 | Yes | L1 |
| T0-AX-KASP-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Kaspersky | Server2025 | Yes | L1 |
| T0-CS-BITD-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Bitdefender | Win11Enterprise | Yes | L1 |
| T0-HV-BITD-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Bitdefender | Win11Enterprise | Yes | L1 |
| T0-AX-BITD-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Bitdefender | Win11Enterprise | Yes | L1 |
| T0-CS-BITD-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Bitdefender | Server2025 | Yes | L1 |
| T0-HV-BITD-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Bitdefender | Server2025 | Yes | L1 |
| T0-AX-BITD-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Bitdefender | Server2025 | Yes | L1 |
| T0-CS-ELAS-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Elastic | Win11Enterprise | Yes | L1 |
| T0-HV-ELAS-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Elastic | Win11Enterprise | Yes | L1 |
| T0-AX-ELAS-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Elastic | Win11Enterprise | Yes | L1 |
| T0-CS-ELAS-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Elastic | Server2025 | Yes | L1 |
| T0-HV-ELAS-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Elastic | Server2025 | Yes | L1 |
| T0-AX-ELAS-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Elastic | Server2025 | Yes | L1 |
| T0-CS-HUOR-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Huorong | Win11Enterprise | Yes | L1 |
| T0-HV-HUOR-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Huorong | Win11Enterprise | Yes | L1 |
| T0-AX-HUOR-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Huorong | Win11Enterprise | Yes | L1 |
| T0-CS-HUOR-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | Huorong | Server2025 | Yes | L1 |
| T0-HV-HUOR-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | Huorong | Server2025 | Yes | L1 |
| T0-AX-HUOR-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | Huorong | Server2025 | Yes | L1 |
| T0-CS-MDAV-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | DefenderAV | Win11Enterprise | Yes | L1 |
| T0-HV-MDAV-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | DefenderAV | Win11Enterprise | Yes | L1 |
| T0-AX-MDAV-W11 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | DefenderAV | Win11Enterprise | Yes | L1 |
| T0-CS-MDAV-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | CobaltStrike | DefenderAV | Server2025 | Yes | L1 |
| T0-HV-MDAV-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | Havoc | DefenderAV | Server2025 | Yes | L1 |
| T0-AX-MDAV-S25 | T0 | AES-protected Baseline Payload (no additional evasion logic) | AdaptixC2 | DefenderAV | Server2025 | Yes | L1 |
| T1-CS-SOPH-W11 | T1 | Direct Syscall Invocation | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T1-HV-SOPH-W11 | T1 | Direct Syscall Invocation | Havoc | Sophos | Win11Enterprise | No | L2 |
| T1-AX-SOPH-W11 | T1 | Direct Syscall Invocation | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T1-CS-SOPH-S25 | T1 | Direct Syscall Invocation | CobaltStrike | Sophos | Server2025 | No | L2 |
| T1-HV-SOPH-S25 | T1 | Direct Syscall Invocation | Havoc | Sophos | Server2025 | No | L2 |
| T1-AX-SOPH-S25 | T1 | Direct Syscall Invocation | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T1-CS-KASP-W11 | T1 | Direct Syscall Invocation | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T1-HV-KASP-W11 | T1 | Direct Syscall Invocation | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T1-AX-KASP-W11 | T1 | Direct Syscall Invocation | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T1-CS-KASP-S25 | T1 | Direct Syscall Invocation | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T1-HV-KASP-S25 | T1 | Direct Syscall Invocation | Havoc | Kaspersky | Server2025 | No | L5 |
| T1-AX-KASP-S25 | T1 | Direct Syscall Invocation | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T1-CS-BITD-W11 | T1 | Direct Syscall Invocation | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T1-HV-BITD-W11 | T1 | Direct Syscall Invocation | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T1-AX-BITD-W11 | T1 | Direct Syscall Invocation | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T1-CS-BITD-S25 | T1 | Direct Syscall Invocation | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T1-HV-BITD-S25 | T1 | Direct Syscall Invocation | Havoc | Bitdefender | Server2025 | No | L2 |
| T1-AX-BITD-S25 | T1 | Direct Syscall Invocation | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T1-CS-ELAS-W11 | T1 | Direct Syscall Invocation | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T1-HV-ELAS-W11 | T1 | Direct Syscall Invocation | Havoc | Elastic | Win11Enterprise | No | L1 |
| T1-AX-ELAS-W11 | T1 | Direct Syscall Invocation | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T1-CS-ELAS-S25 | T1 | Direct Syscall Invocation | CobaltStrike | Elastic | Server2025 | No | L1 |
| T1-HV-ELAS-S25 | T1 | Direct Syscall Invocation | Havoc | Elastic | Server2025 | No | L1 |
| T1-AX-ELAS-S25 | T1 | Direct Syscall Invocation | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T1-CS-HUOR-W11 | T1 | Direct Syscall Invocation | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T1-HV-HUOR-W11 | T1 | Direct Syscall Invocation | Havoc | Huorong | Win11Enterprise | No | L5 |
| T1-AX-HUOR-W11 | T1 | Direct Syscall Invocation | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T1-CS-HUOR-S25 | T1 | Direct Syscall Invocation | CobaltStrike | Huorong | Server2025 | No | L3 |
| T1-HV-HUOR-S25 | T1 | Direct Syscall Invocation | Havoc | Huorong | Server2025 | No | L5 |
| T1-AX-HUOR-S25 | T1 | Direct Syscall Invocation | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T1-CS-MDAV-W11 | T1 | Direct Syscall Invocation | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T1-HV-MDAV-W11 | T1 | Direct Syscall Invocation | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T1-AX-MDAV-W11 | T1 | Direct Syscall Invocation | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T1-CS-MDAV-S25 | T1 | Direct Syscall Invocation | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T1-HV-MDAV-S25 | T1 | Direct Syscall Invocation | Havoc | DefenderAV | Server2025 | No | L5 |
| T1-AX-MDAV-S25 | T1 | Direct Syscall Invocation | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T2-CS-SOPH-W11 | T2 | ETW & AMSI Patching | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T2-HV-SOPH-W11 | T2 | ETW & AMSI Patching | Havoc | Sophos | Win11Enterprise | No | L2 |
| T2-AX-SOPH-W11 | T2 | ETW & AMSI Patching | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T2-CS-SOPH-S25 | T2 | ETW & AMSI Patching | CobaltStrike | Sophos | Server2025 | No | L2 |
| T2-HV-SOPH-S25 | T2 | ETW & AMSI Patching | Havoc | Sophos | Server2025 | No | L2 |
| T2-AX-SOPH-S25 | T2 | ETW & AMSI Patching | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T2-CS-KASP-W11 | T2 | ETW & AMSI Patching | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T2-HV-KASP-W11 | T2 | ETW & AMSI Patching | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T2-AX-KASP-W11 | T2 | ETW & AMSI Patching | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T2-CS-KASP-S25 | T2 | ETW & AMSI Patching | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T2-HV-KASP-S25 | T2 | ETW & AMSI Patching | Havoc | Kaspersky | Server2025 | No | L5 |
| T2-AX-KASP-S25 | T2 | ETW & AMSI Patching | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T2-CS-BITD-W11 | T2 | ETW & AMSI Patching | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T2-HV-BITD-W11 | T2 | ETW & AMSI Patching | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T2-AX-BITD-W11 | T2 | ETW & AMSI Patching | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T2-CS-BITD-S25 | T2 | ETW & AMSI Patching | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T2-HV-BITD-S25 | T2 | ETW & AMSI Patching | Havoc | Bitdefender | Server2025 | No | L2 |
| T2-AX-BITD-S25 | T2 | ETW & AMSI Patching | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T2-CS-ELAS-W11 | T2 | ETW & AMSI Patching | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T2-HV-ELAS-W11 | T2 | ETW & AMSI Patching | Havoc | Elastic | Win11Enterprise | No | L1 |
| T2-AX-ELAS-W11 | T2 | ETW & AMSI Patching | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T2-CS-ELAS-S25 | T2 | ETW & AMSI Patching | CobaltStrike | Elastic | Server2025 | No | L1 |
| T2-HV-ELAS-S25 | T2 | ETW & AMSI Patching | Havoc | Elastic | Server2025 | No | L1 |
| T2-AX-ELAS-S25 | T2 | ETW & AMSI Patching | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T2-CS-HUOR-W11 | T2 | ETW & AMSI Patching | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T2-HV-HUOR-W11 | T2 | ETW & AMSI Patching | Havoc | Huorong | Win11Enterprise | No | L5 |
| T2-AX-HUOR-W11 | T2 | ETW & AMSI Patching | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T2-CS-HUOR-S25 | T2 | ETW & AMSI Patching | CobaltStrike | Huorong | Server2025 | No | L3 |
| T2-HV-HUOR-S25 | T2 | ETW & AMSI Patching | Havoc | Huorong | Server2025 | No | L5 |
| T2-AX-HUOR-S25 | T2 | ETW & AMSI Patching | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T2-CS-MDAV-W11 | T2 | ETW & AMSI Patching | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T2-HV-MDAV-W11 | T2 | ETW & AMSI Patching | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T2-AX-MDAV-W11 | T2 | ETW & AMSI Patching | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T2-CS-MDAV-S25 | T2 | ETW & AMSI Patching | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T2-HV-MDAV-S25 | T2 | ETW & AMSI Patching | Havoc | DefenderAV | Server2025 | No | L5 |
| T2-AX-MDAV-S25 | T2 | ETW & AMSI Patching | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T3-CS-SOPH-W11 | T3 | DLL Signature Restriction | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T3-HV-SOPH-W11 | T3 | DLL Signature Restriction | Havoc | Sophos | Win11Enterprise | No | L2 |
| T3-AX-SOPH-W11 | T3 | DLL Signature Restriction | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T3-CS-SOPH-S25 | T3 | DLL Signature Restriction | CobaltStrike | Sophos | Server2025 | No | L2 |
| T3-HV-SOPH-S25 | T3 | DLL Signature Restriction | Havoc | Sophos | Server2025 | No | L2 |
| T3-AX-SOPH-S25 | T3 | DLL Signature Restriction | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T3-CS-KASP-W11 | T3 | DLL Signature Restriction | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T3-HV-KASP-W11 | T3 | DLL Signature Restriction | Havoc | Kaspersky | Win11Enterprise | No | L4 |
| T3-AX-KASP-W11 | T3 | DLL Signature Restriction | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T3-CS-KASP-S25 | T3 | DLL Signature Restriction | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T3-HV-KASP-S25 | T3 | DLL Signature Restriction | Havoc | Kaspersky | Server2025 | No | L4 |
| T3-AX-KASP-S25 | T3 | DLL Signature Restriction | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T3-CS-BITD-W11 | T3 | DLL Signature Restriction | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T3-HV-BITD-W11 | T3 | DLL Signature Restriction | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T3-AX-BITD-W11 | T3 | DLL Signature Restriction | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T3-CS-BITD-S25 | T3 | DLL Signature Restriction | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T3-HV-BITD-S25 | T3 | DLL Signature Restriction | Havoc | Bitdefender | Server2025 | No | L2 |
| T3-AX-BITD-S25 | T3 | DLL Signature Restriction | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T3-CS-ELAS-W11 | T3 | DLL Signature Restriction | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T3-HV-ELAS-W11 | T3 | DLL Signature Restriction | Havoc | Elastic | Win11Enterprise | No | L1 |
| T3-AX-ELAS-W11 | T3 | DLL Signature Restriction | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T3-CS-ELAS-S25 | T3 | DLL Signature Restriction | CobaltStrike | Elastic | Server2025 | No | L1 |
| T3-HV-ELAS-S25 | T3 | DLL Signature Restriction | Havoc | Elastic | Server2025 | No | L1 |
| T3-AX-ELAS-S25 | T3 | DLL Signature Restriction | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T3-CS-HUOR-W11 | T3 | DLL Signature Restriction | CobaltStrike | Huorong | Win11Enterprise | No | L4 |
| T3-HV-HUOR-W11 | T3 | DLL Signature Restriction | Havoc | Huorong | Win11Enterprise | No | L5 |
| T3-AX-HUOR-W11 | T3 | DLL Signature Restriction | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T3-CS-HUOR-S25 | T3 | DLL Signature Restriction | CobaltStrike | Huorong | Server2025 | No | L4 |
| T3-HV-HUOR-S25 | T3 | DLL Signature Restriction | Havoc | Huorong | Server2025 | No | L5 |
| T3-AX-HUOR-S25 | T3 | DLL Signature Restriction | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T3-CS-MDAV-W11 | T3 | DLL Signature Restriction | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T3-HV-MDAV-W11 | T3 | DLL Signature Restriction | Havoc | DefenderAV | Win11Enterprise | No | L3 |
| T3-AX-MDAV-W11 | T3 | DLL Signature Restriction | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T3-CS-MDAV-S25 | T3 | DLL Signature Restriction | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T3-HV-MDAV-S25 | T3 | DLL Signature Restriction | Havoc | DefenderAV | Server2025 | No | L4 |
| T3-AX-MDAV-S25 | T3 | DLL Signature Restriction | AdaptixC2 | DefenderAV | Server2025 | No | L3 |
| T4-CS-SOPH-W11 | T4 | Hook Overwriting | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T4-HV-SOPH-W11 | T4 | Hook Overwriting | Havoc | Sophos | Win11Enterprise | No | L2 |
| T4-AX-SOPH-W11 | T4 | Hook Overwriting | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T4-CS-SOPH-S25 | T4 | Hook Overwriting | CobaltStrike | Sophos | Server2025 | No | L2 |
| T4-HV-SOPH-S25 | T4 | Hook Overwriting | Havoc | Sophos | Server2025 | No | L2 |
| T4-AX-SOPH-S25 | T4 | Hook Overwriting | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T4-CS-KASP-W11 | T4 | Hook Overwriting | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T4-HV-KASP-W11 | T4 | Hook Overwriting | Havoc | Kaspersky | Win11Enterprise | No | L4 |
| T4-AX-KASP-W11 | T4 | Hook Overwriting | AdaptixC2 | Kaspersky | Win11Enterprise | No | L2 |
| T4-CS-KASP-S25 | T4 | Hook Overwriting | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T4-HV-KASP-S25 | T4 | Hook Overwriting | Havoc | Kaspersky | Server2025 | No | L4 |
| T4-AX-KASP-S25 | T4 | Hook Overwriting | AdaptixC2 | Kaspersky | Server2025 | No | L2 |
| T4-CS-BITD-W11 | T4 | Hook Overwriting | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T4-HV-BITD-W11 | T4 | Hook Overwriting | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T4-AX-BITD-W11 | T4 | Hook Overwriting | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T4-CS-BITD-S25 | T4 | Hook Overwriting | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T4-HV-BITD-S25 | T4 | Hook Overwriting | Havoc | Bitdefender | Server2025 | No | L2 |
| T4-AX-BITD-S25 | T4 | Hook Overwriting | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T4-CS-ELAS-W11 | T4 | Hook Overwriting | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T4-HV-ELAS-W11 | T4 | Hook Overwriting | Havoc | Elastic | Win11Enterprise | No | L1 |
| T4-AX-ELAS-W11 | T4 | Hook Overwriting | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T4-CS-ELAS-S25 | T4 | Hook Overwriting | CobaltStrike | Elastic | Server2025 | No | L1 |
| T4-HV-ELAS-S25 | T4 | Hook Overwriting | Havoc | Elastic | Server2025 | No | L1 |
| T4-AX-ELAS-S25 | T4 | Hook Overwriting | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T4-CS-HUOR-W11 | T4 | Hook Overwriting | CobaltStrike | Huorong | Win11Enterprise | No | L5 |
| T4-HV-HUOR-W11 | T4 | Hook Overwriting | Havoc | Huorong | Win11Enterprise | No | L5 |
| T4-AX-HUOR-W11 | T4 | Hook Overwriting | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T4-CS-HUOR-S25 | T4 | Hook Overwriting | CobaltStrike | Huorong | Server2025 | No | L5 |
| T4-HV-HUOR-S25 | T4 | Hook Overwriting | Havoc | Huorong | Server2025 | No | L5 |
| T4-AX-HUOR-S25 | T4 | Hook Overwriting | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T4-CS-MDAV-W11 | T4 | Hook Overwriting | CobaltStrike | DefenderAV | Win11Enterprise | No | L2 |
| T4-HV-MDAV-W11 | T4 | Hook Overwriting | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T4-AX-MDAV-W11 | T4 | Hook Overwriting | AdaptixC2 | DefenderAV | Win11Enterprise | No | L2 |
| T4-CS-MDAV-S25 | T4 | Hook Overwriting | CobaltStrike | DefenderAV | Server2025 | No | L2 |
| T4-HV-MDAV-S25 | T4 | Hook Overwriting | Havoc | DefenderAV | Server2025 | No | L5 |
| T4-AX-MDAV-S25 | T4 | Hook Overwriting | AdaptixC2 | DefenderAV | Server2025 | No | L3 |
| T5-CS-SOPH-W11 | T5 | NTDLL Hook Removal | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T5-HV-SOPH-W11 | T5 | NTDLL Hook Removal | Havoc | Sophos | Win11Enterprise | No | L2 |
| T5-AX-SOPH-W11 | T5 | NTDLL Hook Removal | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T5-CS-SOPH-S25 | T5 | NTDLL Hook Removal | CobaltStrike | Sophos | Server2025 | No | L2 |
| T5-HV-SOPH-S25 | T5 | NTDLL Hook Removal | Havoc | Sophos | Server2025 | No | L2 |
| T5-AX-SOPH-S25 | T5 | NTDLL Hook Removal | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T5-CS-KASP-W11 | T5 | NTDLL Hook Removal | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T5-HV-KASP-W11 | T5 | NTDLL Hook Removal | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T5-AX-KASP-W11 | T5 | NTDLL Hook Removal | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T5-CS-KASP-S25 | T5 | NTDLL Hook Removal | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T5-HV-KASP-S25 | T5 | NTDLL Hook Removal | Havoc | Kaspersky | Server2025 | No | L5 |
| T5-AX-KASP-S25 | T5 | NTDLL Hook Removal | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T5-CS-BITD-W11 | T5 | NTDLL Hook Removal | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T5-HV-BITD-W11 | T5 | NTDLL Hook Removal | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T5-AX-BITD-W11 | T5 | NTDLL Hook Removal | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T5-CS-BITD-S25 | T5 | NTDLL Hook Removal | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T5-HV-BITD-S25 | T5 | NTDLL Hook Removal | Havoc | Bitdefender | Server2025 | No | L2 |
| T5-AX-BITD-S25 | T5 | NTDLL Hook Removal | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T5-CS-ELAS-W11 | T5 | NTDLL Hook Removal | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T5-HV-ELAS-W11 | T5 | NTDLL Hook Removal | Havoc | Elastic | Win11Enterprise | No | L1 |
| T5-AX-ELAS-W11 | T5 | NTDLL Hook Removal | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T5-CS-ELAS-S25 | T5 | NTDLL Hook Removal | CobaltStrike | Elastic | Server2025 | No | L1 |
| T5-HV-ELAS-S25 | T5 | NTDLL Hook Removal | Havoc | Elastic | Server2025 | No | L1 |
| T5-AX-ELAS-S25 | T5 | NTDLL Hook Removal | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T5-CS-HUOR-W11 | T5 | NTDLL Hook Removal | CobaltStrike | Huorong | Win11Enterprise | No | L1 |
| T5-HV-HUOR-W11 | T5 | NTDLL Hook Removal | Havoc | Huorong | Win11Enterprise | No | L1 |
| T5-AX-HUOR-W11 | T5 | NTDLL Hook Removal | AdaptixC2 | Huorong | Win11Enterprise | No | L1 |
| T5-CS-HUOR-S25 | T5 | NTDLL Hook Removal | CobaltStrike | Huorong | Server2025 | No | L1 |
| T5-HV-HUOR-S25 | T5 | NTDLL Hook Removal | Havoc | Huorong | Server2025 | No | L1 |
| T5-AX-HUOR-S25 | T5 | NTDLL Hook Removal | AdaptixC2 | Huorong | Server2025 | No | L1 |
| T5-CS-MDAV-W11 | T5 | NTDLL Hook Removal | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T5-HV-MDAV-W11 | T5 | NTDLL Hook Removal | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T5-AX-MDAV-W11 | T5 | NTDLL Hook Removal | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T5-CS-MDAV-S25 | T5 | NTDLL Hook Removal | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T5-HV-MDAV-S25 | T5 | NTDLL Hook Removal | Havoc | DefenderAV | Server2025 | No | L5 |
| T5-AX-MDAV-S25 | T5 | NTDLL Hook Removal | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T6-CS-SOPH-W11 | T6 | Kernel Callback Removal | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T6-HV-SOPH-W11 | T6 | Kernel Callback Removal | Havoc | Sophos | Win11Enterprise | No | L2 |
| T6-AX-SOPH-W11 | T6 | Kernel Callback Removal | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T6-CS-SOPH-S25 | T6 | Kernel Callback Removal | CobaltStrike | Sophos | Server2025 | No | L2 |
| T6-HV-SOPH-S25 | T6 | Kernel Callback Removal | Havoc | Sophos | Server2025 | No | L2 |
| T6-AX-SOPH-S25 | T6 | Kernel Callback Removal | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T6-CS-KASP-W11 | T6 | Kernel Callback Removal | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T6-HV-KASP-W11 | T6 | Kernel Callback Removal | Havoc | Kaspersky | Win11Enterprise | No | L2 |
| T6-AX-KASP-W11 | T6 | Kernel Callback Removal | AdaptixC2 | Kaspersky | Win11Enterprise | No | L2 |
| T6-CS-KASP-S25 | T6 | Kernel Callback Removal | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T6-HV-KASP-S25 | T6 | Kernel Callback Removal | Havoc | Kaspersky | Server2025 | No | L2 |
| T6-AX-KASP-S25 | T6 | Kernel Callback Removal | AdaptixC2 | Kaspersky | Server2025 | No | L2 |
| T6-CS-BITD-W11 | T6 | Kernel Callback Removal | CobaltStrike | Bitdefender | Win11Enterprise | No | L1 |
| T6-HV-BITD-W11 | T6 | Kernel Callback Removal | Havoc | Bitdefender | Win11Enterprise | No | L1 |
| T6-AX-BITD-W11 | T6 | Kernel Callback Removal | AdaptixC2 | Bitdefender | Win11Enterprise | No | L1 |
| T6-CS-BITD-S25 | T6 | Kernel Callback Removal | CobaltStrike | Bitdefender | Server2025 | No | L1 |
| T6-HV-BITD-S25 | T6 | Kernel Callback Removal | Havoc | Bitdefender | Server2025 | No | L1 |
| T6-AX-BITD-S25 | T6 | Kernel Callback Removal | AdaptixC2 | Bitdefender | Server2025 | No | L1 |
| T6-CS-ELAS-W11 | T6 | Kernel Callback Removal | CobaltStrike | Elastic | Win11Enterprise | No | L2 |
| T6-HV-ELAS-W11 | T6 | Kernel Callback Removal | Havoc | Elastic | Win11Enterprise | No | L2 |
| T6-AX-ELAS-W11 | T6 | Kernel Callback Removal | AdaptixC2 | Elastic | Win11Enterprise | No | L2 |
| T6-CS-ELAS-S25 | T6 | Kernel Callback Removal | CobaltStrike | Elastic | Server2025 | No | L2 |
| T6-HV-ELAS-S25 | T6 | Kernel Callback Removal | Havoc | Elastic | Server2025 | No | L2 |
| T6-AX-ELAS-S25 | T6 | Kernel Callback Removal | AdaptixC2 | Elastic | Server2025 | No | L2 |
| T6-CS-HUOR-W11 | T6 | Kernel Callback Removal | CobaltStrike | Huorong | Win11Enterprise | No | L1 |
| T6-HV-HUOR-W11 | T6 | Kernel Callback Removal | Havoc | Huorong | Win11Enterprise | No | L1 |
| T6-AX-HUOR-W11 | T6 | Kernel Callback Removal | AdaptixC2 | Huorong | Win11Enterprise | No | L1 |
| T6-CS-HUOR-S25 | T6 | Kernel Callback Removal | CobaltStrike | Huorong | Server2025 | No | L1 |
| T6-HV-HUOR-S25 | T6 | Kernel Callback Removal | Havoc | Huorong | Server2025 | No | L1 |
| T6-AX-HUOR-S25 | T6 | Kernel Callback Removal | AdaptixC2 | Huorong | Server2025 | No | L1 |
| T6-CS-MDAV-W11 | T6 | Kernel Callback Removal | CobaltStrike | DefenderAV | Win11Enterprise | No | L5 |
| T6-HV-MDAV-W11 | T6 | Kernel Callback Removal | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T6-AX-MDAV-W11 | T6 | Kernel Callback Removal | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T6-CS-MDAV-S25 | T6 | Kernel Callback Removal | CobaltStrike | DefenderAV | Server2025 | No | L5 |
| T6-HV-MDAV-S25 | T6 | Kernel Callback Removal | Havoc | DefenderAV | Server2025 | No | L5 |
| T6-AX-MDAV-S25 | T6 | Kernel Callback Removal | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T7-CS-SOPH-W11 | T7 | Symlink-based EDR Corruption | CobaltStrike | Sophos | Win11Enterprise | No | L3 |
| T7-HV-SOPH-W11 | T7 | Symlink-based EDR Corruption | Havoc | Sophos | Win11Enterprise | No | L3 |
| T7-AX-SOPH-W11 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Sophos | Win11Enterprise | No | L3 |
| T7-CS-SOPH-S25 | T7 | Symlink-based EDR Corruption | CobaltStrike | Sophos | Server2025 | No | L3 |
| T7-HV-SOPH-S25 | T7 | Symlink-based EDR Corruption | Havoc | Sophos | Server2025 | No | L3 |
| T7-AX-SOPH-S25 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Sophos | Server2025 | No | L3 |
| T7-CS-KASP-W11 | T7 | Symlink-based EDR Corruption | CobaltStrike | Kaspersky | Win11Enterprise | No | L5 |
| T7-HV-KASP-W11 | T7 | Symlink-based EDR Corruption | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T7-AX-KASP-W11 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Kaspersky | Win11Enterprise | No | L5 |
| T7-CS-KASP-S25 | T7 | Symlink-based EDR Corruption | CobaltStrike | Kaspersky | Server2025 | No | L5 |
| T7-HV-KASP-S25 | T7 | Symlink-based EDR Corruption | Havoc | Kaspersky | Server2025 | No | L5 |
| T7-AX-KASP-S25 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Kaspersky | Server2025 | No | L5 |
| T7-CS-BITD-W11 | T7 | Symlink-based EDR Corruption | CobaltStrike | Bitdefender | Win11Enterprise | No | L3 |
| T7-HV-BITD-W11 | T7 | Symlink-based EDR Corruption | Havoc | Bitdefender | Win11Enterprise | No | L3 |
| T7-AX-BITD-W11 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Bitdefender | Win11Enterprise | No | L3 |
| T7-CS-BITD-S25 | T7 | Symlink-based EDR Corruption | CobaltStrike | Bitdefender | Server2025 | No | L3 |
| T7-HV-BITD-S25 | T7 | Symlink-based EDR Corruption | Havoc | Bitdefender | Server2025 | No | L3 |
| T7-AX-BITD-S25 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Bitdefender | Server2025 | No | L3 |
| T7-CS-ELAS-W11 | T7 | Symlink-based EDR Corruption | CobaltStrike | Elastic | Win11Enterprise | No | L5 |
| T7-HV-ELAS-W11 | T7 | Symlink-based EDR Corruption | Havoc | Elastic | Win11Enterprise | No | L5 |
| T7-AX-ELAS-W11 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Elastic | Win11Enterprise | No | L5 |
| T7-CS-ELAS-S25 | T7 | Symlink-based EDR Corruption | CobaltStrike | Elastic | Server2025 | No | L5 |
| T7-HV-ELAS-S25 | T7 | Symlink-based EDR Corruption | Havoc | Elastic | Server2025 | No | L5 |
| T7-AX-ELAS-S25 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Elastic | Server2025 | No | L5 |
| T7-CS-HUOR-W11 | T7 | Symlink-based EDR Corruption | CobaltStrike | Huorong | Win11Enterprise | No | L5 |
| T7-HV-HUOR-W11 | T7 | Symlink-based EDR Corruption | Havoc | Huorong | Win11Enterprise | No | L5 |
| T7-AX-HUOR-W11 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T7-CS-HUOR-S25 | T7 | Symlink-based EDR Corruption | CobaltStrike | Huorong | Server2025 | No | L5 |
| T7-HV-HUOR-S25 | T7 | Symlink-based EDR Corruption | Havoc | Huorong | Server2025 | No | L5 |
| T7-AX-HUOR-S25 | T7 | Symlink-based EDR Corruption | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T7-CS-MDAV-W11 | T7 | Symlink-based EDR Corruption | CobaltStrike | DefenderAV | Win11Enterprise | No | L5 |
| T7-HV-MDAV-W11 | T7 | Symlink-based EDR Corruption | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T7-AX-MDAV-W11 | T7 | Symlink-based EDR Corruption | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T7-CS-MDAV-S25 | T7 | Symlink-based EDR Corruption | CobaltStrike | DefenderAV | Server2025 | No | L5 |
| T7-HV-MDAV-S25 | T7 | Symlink-based EDR Corruption | Havoc | DefenderAV | Server2025 | No | L5 |
| T7-AX-MDAV-S25 | T7 | Symlink-based EDR Corruption | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T8-CS-SOPH-W11 | T8 | EDR Process Termination | CobaltStrike | Sophos | Win11Enterprise | No | L1 |
| T8-HV-SOPH-W11 | T8 | EDR Process Termination | Havoc | Sophos | Win11Enterprise | No | L1 |
| T8-AX-SOPH-W11 | T8 | EDR Process Termination | AdaptixC2 | Sophos | Win11Enterprise | No | L1 |
| T8-CS-SOPH-S25 | T8 | EDR Process Termination | CobaltStrike | Sophos | Server2025 | No | L1 |
| T8-HV-SOPH-S25 | T8 | EDR Process Termination | Havoc | Sophos | Server2025 | No | L1 |
| T8-AX-SOPH-S25 | T8 | EDR Process Termination | AdaptixC2 | Sophos | Server2025 | No | L1 |
| T8-CS-KASP-W11 | T8 | EDR Process Termination | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T8-HV-KASP-W11 | T8 | EDR Process Termination | Havoc | Kaspersky | Win11Enterprise | No | L2 |
| T8-AX-KASP-W11 | T8 | EDR Process Termination | AdaptixC2 | Kaspersky | Win11Enterprise | No | L2 |
| T8-CS-KASP-S25 | T8 | EDR Process Termination | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T8-HV-KASP-S25 | T8 | EDR Process Termination | Havoc | Kaspersky | Server2025 | No | L2 |
| T8-AX-KASP-S25 | T8 | EDR Process Termination | AdaptixC2 | Kaspersky | Server2025 | No | L2 |
| T8-CS-BITD-W11 | T8 | EDR Process Termination | CobaltStrike | Bitdefender | Win11Enterprise | No | L1 |
| T8-HV-BITD-W11 | T8 | EDR Process Termination | Havoc | Bitdefender | Win11Enterprise | No | L1 |
| T8-AX-BITD-W11 | T8 | EDR Process Termination | AdaptixC2 | Bitdefender | Win11Enterprise | No | L1 |
| T8-CS-BITD-S25 | T8 | EDR Process Termination | CobaltStrike | Bitdefender | Server2025 | No | L1 |
| T8-HV-BITD-S25 | T8 | EDR Process Termination | Havoc | Bitdefender | Server2025 | No | L1 |
| T8-AX-BITD-S25 | T8 | EDR Process Termination | AdaptixC2 | Bitdefender | Server2025 | No | L1 |
| T8-CS-ELAS-W11 | T8 | EDR Process Termination | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T8-HV-ELAS-W11 | T8 | EDR Process Termination | Havoc | Elastic | Win11Enterprise | No | L1 |
| T8-AX-ELAS-W11 | T8 | EDR Process Termination | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T8-CS-ELAS-S25 | T8 | EDR Process Termination | CobaltStrike | Elastic | Server2025 | No | L1 |
| T8-HV-ELAS-S25 | T8 | EDR Process Termination | Havoc | Elastic | Server2025 | No | L1 |
| T8-AX-ELAS-S25 | T8 | EDR Process Termination | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T8-CS-HUOR-W11 | T8 | EDR Process Termination | CobaltStrike | Huorong | Win11Enterprise | No | L1 |
| T8-HV-HUOR-W11 | T8 | EDR Process Termination | Havoc | Huorong | Win11Enterprise | No | L1 |
| T8-AX-HUOR-W11 | T8 | EDR Process Termination | AdaptixC2 | Huorong | Win11Enterprise | No | L1 |
| T8-CS-HUOR-S25 | T8 | EDR Process Termination | CobaltStrike | Huorong | Server2025 | No | L1 |
| T8-HV-HUOR-S25 | T8 | EDR Process Termination | Havoc | Huorong | Server2025 | No | L1 |
| T8-AX-HUOR-S25 | T8 | EDR Process Termination | AdaptixC2 | Huorong | Server2025 | No | L1 |
| T8-CS-MDAV-W11 | T8 | EDR Process Termination | CobaltStrike | DefenderAV | Win11Enterprise | No | L5 |
| T8-HV-MDAV-W11 | T8 | EDR Process Termination | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T8-AX-MDAV-W11 | T8 | EDR Process Termination | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T8-CS-MDAV-S25 | T8 | EDR Process Termination | CobaltStrike | DefenderAV | Server2025 | No | L5 |
| T8-HV-MDAV-S25 | T8 | EDR Process Termination | Havoc | DefenderAV | Server2025 | No | L5 |
| T8-AX-MDAV-S25 | T8 | EDR Process Termination | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T9-CS-SOPH-W11 | T9 | EDRSilencer | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T9-HV-SOPH-W11 | T9 | EDRSilencer | Havoc | Sophos | Win11Enterprise | No | L2 |
| T9-AX-SOPH-W11 | T9 | EDRSilencer | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T9-CS-SOPH-S25 | T9 | EDRSilencer | CobaltStrike | Sophos | Server2025 | No | L2 |
| T9-HV-SOPH-S25 | T9 | EDRSilencer | Havoc | Sophos | Server2025 | No | L2 |
| T9-AX-SOPH-S25 | T9 | EDRSilencer | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T9-CS-KASP-W11 | T9 | EDRSilencer | CobaltStrike | Kaspersky | Win11Enterprise | No | L1 |
| T9-HV-KASP-W11 | T9 | EDRSilencer | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T9-AX-KASP-W11 | T9 | EDRSilencer | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T9-CS-KASP-S25 | T9 | EDRSilencer | CobaltStrike | Kaspersky | Server2025 | No | L1 |
| T9-HV-KASP-S25 | T9 | EDRSilencer | Havoc | Kaspersky | Server2025 | No | L1 |
| T9-AX-KASP-S25 | T9 | EDRSilencer | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T9-CS-BITD-W11 | T9 | EDRSilencer | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T9-HV-BITD-W11 | T9 | EDRSilencer | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T9-AX-BITD-W11 | T9 | EDRSilencer | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T9-CS-BITD-S25 | T9 | EDRSilencer | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T9-HV-BITD-S25 | T9 | EDRSilencer | Havoc | Bitdefender | Server2025 | No | L2 |
| T9-AX-BITD-S25 | T9 | EDRSilencer | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T9-CS-ELAS-W11 | T9 | EDRSilencer | CobaltStrike | Elastic | Win11Enterprise | No | L5 |
| T9-HV-ELAS-W11 | T9 | EDRSilencer | Havoc | Elastic | Win11Enterprise | No | L5 |
| T9-AX-ELAS-W11 | T9 | EDRSilencer | AdaptixC2 | Elastic | Win11Enterprise | No | L5 |
| T9-CS-ELAS-S25 | T9 | EDRSilencer | CobaltStrike | Elastic | Server2025 | No | L5 |
| T9-HV-ELAS-S25 | T9 | EDRSilencer | Havoc | Elastic | Server2025 | No | L5 |
| T9-AX-ELAS-S25 | T9 | EDRSilencer | AdaptixC2 | Elastic | Server2025 | No | L5 |
| T9-CS-HUOR-W11 | T9 | EDRSilencer | CobaltStrike | Huorong | Win11Enterprise | No | L5 |
| T9-HV-HUOR-W11 | T9 | EDRSilencer | Havoc | Huorong | Win11Enterprise | No | L5 |
| T9-AX-HUOR-W11 | T9 | EDRSilencer | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T9-CS-HUOR-S25 | T9 | EDRSilencer | CobaltStrike | Huorong | Server2025 | No | L5 |
| T9-HV-HUOR-S25 | T9 | EDRSilencer | Havoc | Huorong | Server2025 | No | L5 |
| T9-AX-HUOR-S25 | T9 | EDRSilencer | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T9-CS-MDAV-W11 | T9 | EDRSilencer | CobaltStrike | DefenderAV | Win11Enterprise | No | L4 |
| T9-HV-MDAV-W11 | T9 | EDRSilencer | Havoc | DefenderAV | Win11Enterprise | No | L4 |
| T9-AX-MDAV-W11 | T9 | EDRSilencer | AdaptixC2 | DefenderAV | Win11Enterprise | No | L4 |
| T9-CS-MDAV-S25 | T9 | EDRSilencer | CobaltStrike | DefenderAV | Server2025 | No | L4 |
| T9-HV-MDAV-S25 | T9 | EDRSilencer | Havoc | DefenderAV | Server2025 | No | L4 |
| T9-AX-MDAV-S25 | T9 | EDRSilencer | AdaptixC2 | DefenderAV | Server2025 | No | L4 |
| T10-CS-SOPH-W11 | T10 | COM Hijacking | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T10-HV-SOPH-W11 | T10 | COM Hijacking | Havoc | Sophos | Win11Enterprise | No | L2 |
| T10-AX-SOPH-W11 | T10 | COM Hijacking | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T10-CS-SOPH-S25 | T10 | COM Hijacking | CobaltStrike | Sophos | Server2025 | No | L2 |
| T10-HV-SOPH-S25 | T10 | COM Hijacking | Havoc | Sophos | Server2025 | No | L2 |
| T10-AX-SOPH-S25 | T10 | COM Hijacking | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T10-CS-KASP-W11 | T10 | COM Hijacking | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T10-HV-KASP-W11 | T10 | COM Hijacking | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T10-AX-KASP-W11 | T10 | COM Hijacking | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T10-CS-KASP-S25 | T10 | COM Hijacking | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T10-HV-KASP-S25 | T10 | COM Hijacking | Havoc | Kaspersky | Server2025 | No | L1 |
| T10-AX-KASP-S25 | T10 | COM Hijacking | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T10-CS-BITD-W11 | T10 | COM Hijacking | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T10-HV-BITD-W11 | T10 | COM Hijacking | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T10-AX-BITD-W11 | T10 | COM Hijacking | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T10-CS-BITD-S25 | T10 | COM Hijacking | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T10-HV-BITD-S25 | T10 | COM Hijacking | Havoc | Bitdefender | Server2025 | No | L2 |
| T10-AX-BITD-S25 | T10 | COM Hijacking | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T10-CS-ELAS-W11 | T10 | COM Hijacking | CobaltStrike | Elastic | Win11Enterprise | No | L2 |
| T10-HV-ELAS-W11 | T10 | COM Hijacking | Havoc | Elastic | Win11Enterprise | No | L2 |
| T10-AX-ELAS-W11 | T10 | COM Hijacking | AdaptixC2 | Elastic | Win11Enterprise | No | L2 |
| T10-CS-ELAS-S25 | T10 | COM Hijacking | CobaltStrike | Elastic | Server2025 | No | L2 |
| T10-HV-ELAS-S25 | T10 | COM Hijacking | Havoc | Elastic | Server2025 | No | L2 |
| T10-AX-ELAS-S25 | T10 | COM Hijacking | AdaptixC2 | Elastic | Server2025 | No | L2 |
| T10-CS-HUOR-W11 | T10 | COM Hijacking | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T10-HV-HUOR-W11 | T10 | COM Hijacking | Havoc | Huorong | Win11Enterprise | No | L5 |
| T10-AX-HUOR-W11 | T10 | COM Hijacking | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T10-CS-HUOR-S25 | T10 | COM Hijacking | CobaltStrike | Huorong | Server2025 | No | L3 |
| T10-HV-HUOR-S25 | T10 | COM Hijacking | Havoc | Huorong | Server2025 | No | L5 |
| T10-AX-HUOR-S25 | T10 | COM Hijacking | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T10-CS-MDAV-W11 | T10 | COM Hijacking | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T10-HV-MDAV-W11 | T10 | COM Hijacking | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T10-AX-MDAV-W11 | T10 | COM Hijacking | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T10-CS-MDAV-S25 | T10 | COM Hijacking | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T10-HV-MDAV-S25 | T10 | COM Hijacking | Havoc | DefenderAV | Server2025 | No | L5 |
| T10-AX-MDAV-S25 | T10 | COM Hijacking | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T11-CS-SOPH-W11 | T11 | DLL Hijacking | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T11-HV-SOPH-W11 | T11 | DLL Hijacking | Havoc | Sophos | Win11Enterprise | No | L2 |
| T11-AX-SOPH-W11 | T11 | DLL Hijacking | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T11-CS-SOPH-S25 | T11 | DLL Hijacking | CobaltStrike | Sophos | Server2025 | No | L2 |
| T11-HV-SOPH-S25 | T11 | DLL Hijacking | Havoc | Sophos | Server2025 | No | L2 |
| T11-AX-SOPH-S25 | T11 | DLL Hijacking | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T11-CS-KASP-W11 | T11 | DLL Hijacking | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T11-HV-KASP-W11 | T11 | DLL Hijacking | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T11-AX-KASP-W11 | T11 | DLL Hijacking | AdaptixC2 | Kaspersky | Win11Enterprise | No | L5 |
| T11-CS-KASP-S25 | T11 | DLL Hijacking | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T11-HV-KASP-S25 | T11 | DLL Hijacking | Havoc | Kaspersky | Server2025 | No | L5 |
| T11-AX-KASP-S25 | T11 | DLL Hijacking | AdaptixC2 | Kaspersky | Server2025 | No | L5 |
| T11-CS-BITD-W11 | T11 | DLL Hijacking | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T11-HV-BITD-W11 | T11 | DLL Hijacking | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T11-AX-BITD-W11 | T11 | DLL Hijacking | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T11-CS-BITD-S25 | T11 | DLL Hijacking | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T11-HV-BITD-S25 | T11 | DLL Hijacking | Havoc | Bitdefender | Server2025 | No | L2 |
| T11-AX-BITD-S25 | T11 | DLL Hijacking | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T11-CS-ELAS-W11 | T11 | DLL Hijacking | CobaltStrike | Elastic | Win11Enterprise | No | L3 |
| T11-HV-ELAS-W11 | T11 | DLL Hijacking | Havoc | Elastic | Win11Enterprise | No | L1 |
| T11-AX-ELAS-W11 | T11 | DLL Hijacking | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T11-CS-ELAS-S25 | T11 | DLL Hijacking | CobaltStrike | Elastic | Server2025 | No | L3 |
| T11-HV-ELAS-S25 | T11 | DLL Hijacking | Havoc | Elastic | Server2025 | No | L1 |
| T11-AX-ELAS-S25 | T11 | DLL Hijacking | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T11-CS-HUOR-W11 | T11 | DLL Hijacking | CobaltStrike | Huorong | Win11Enterprise | No | L2 |
| T11-HV-HUOR-W11 | T11 | DLL Hijacking | Havoc | Huorong | Win11Enterprise | No | L5 |
| T11-AX-HUOR-W11 | T11 | DLL Hijacking | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T11-CS-HUOR-S25 | T11 | DLL Hijacking | CobaltStrike | Huorong | Server2025 | No | L2 |
| T11-HV-HUOR-S25 | T11 | DLL Hijacking | Havoc | Huorong | Server2025 | No | L5 |
| T11-AX-HUOR-S25 | T11 | DLL Hijacking | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T11-CS-MDAV-W11 | T11 | DLL Hijacking | CobaltStrike | DefenderAV | Win11Enterprise | No | L5 |
| T11-HV-MDAV-W11 | T11 | DLL Hijacking | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T11-AX-MDAV-W11 | T11 | DLL Hijacking | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T11-CS-MDAV-S25 | T11 | DLL Hijacking | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T11-HV-MDAV-S25 | T11 | DLL Hijacking | Havoc | DefenderAV | Server2025 | No | L5 |
| T11-AX-MDAV-S25 | T11 | DLL Hijacking | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T12-CS-SOPH-W11 | T12 | COM-based Process Injection | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T12-HV-SOPH-W11 | T12 | COM-based Process Injection | Havoc | Sophos | Win11Enterprise | No | L2 |
| T12-AX-SOPH-W11 | T12 | COM-based Process Injection | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T12-CS-SOPH-S25 | T12 | COM-based Process Injection | CobaltStrike | Sophos | Server2025 | No | L2 |
| T12-HV-SOPH-S25 | T12 | COM-based Process Injection | Havoc | Sophos | Server2025 | No | L2 |
| T12-AX-SOPH-S25 | T12 | COM-based Process Injection | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T12-CS-KASP-W11 | T12 | COM-based Process Injection | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T12-HV-KASP-W11 | T12 | COM-based Process Injection | Havoc | Kaspersky | Win11Enterprise | No | L2 |
| T12-AX-KASP-W11 | T12 | COM-based Process Injection | AdaptixC2 | Kaspersky | Win11Enterprise | No | L2 |
| T12-CS-KASP-S25 | T12 | COM-based Process Injection | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T12-HV-KASP-S25 | T12 | COM-based Process Injection | Havoc | Kaspersky | Server2025 | No | L2 |
| T12-AX-KASP-S25 | T12 | COM-based Process Injection | AdaptixC2 | Kaspersky | Server2025 | No | L2 |
| T12-CS-BITD-W11 | T12 | COM-based Process Injection | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T12-HV-BITD-W11 | T12 | COM-based Process Injection | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T12-AX-BITD-W11 | T12 | COM-based Process Injection | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T12-CS-BITD-S25 | T12 | COM-based Process Injection | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T12-HV-BITD-S25 | T12 | COM-based Process Injection | Havoc | Bitdefender | Server2025 | No | L2 |
| T12-AX-BITD-S25 | T12 | COM-based Process Injection | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T12-CS-ELAS-W11 | T12 | COM-based Process Injection | CobaltStrike | Elastic | Win11Enterprise | No | L3 |
| T12-HV-ELAS-W11 | T12 | COM-based Process Injection | Havoc | Elastic | Win11Enterprise | No | L3 |
| T12-AX-ELAS-W11 | T12 | COM-based Process Injection | AdaptixC2 | Elastic | Win11Enterprise | No | L3 |
| T12-CS-ELAS-S25 | T12 | COM-based Process Injection | CobaltStrike | Elastic | Server2025 | No | L2 |
| T12-HV-ELAS-S25 | T12 | COM-based Process Injection | Havoc | Elastic | Server2025 | No | L3 |
| T12-AX-ELAS-S25 | T12 | COM-based Process Injection | AdaptixC2 | Elastic | Server2025 | No | L3 |
| T12-CS-HUOR-W11 | T12 | COM-based Process Injection | CobaltStrike | Huorong | Win11Enterprise | No | L5 |
| T12-HV-HUOR-W11 | T12 | COM-based Process Injection | Havoc | Huorong | Win11Enterprise | No | L5 |
| T12-AX-HUOR-W11 | T12 | COM-based Process Injection | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T12-CS-HUOR-S25 | T12 | COM-based Process Injection | CobaltStrike | Huorong | Server2025 | No | L5 |
| T12-HV-HUOR-S25 | T12 | COM-based Process Injection | Havoc | Huorong | Server2025 | No | L5 |
| T12-AX-HUOR-S25 | T12 | COM-based Process Injection | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T12-CS-MDAV-W11 | T12 | COM-based Process Injection | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T12-HV-MDAV-W11 | T12 | COM-based Process Injection | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T12-AX-MDAV-W11 | T12 | COM-based Process Injection | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T12-CS-MDAV-S25 | T12 | COM-based Process Injection | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T12-HV-MDAV-S25 | T12 | COM-based Process Injection | Havoc | DefenderAV | Server2025 | No | L5 |
| T12-AX-MDAV-S25 | T12 | COM-based Process Injection | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T13-CS-SOPH-W11 | T13 | Fiber-based Process Injection | CobaltStrike | Sophos | Win11Enterprise | No | L1 |
| T13-HV-SOPH-W11 | T13 | Fiber-based Process Injection | Havoc | Sophos | Win11Enterprise | No | L1 |
| T13-AX-SOPH-W11 | T13 | Fiber-based Process Injection | AdaptixC2 | Sophos | Win11Enterprise | No | L1 |
| T13-CS-SOPH-S25 | T13 | Fiber-based Process Injection | CobaltStrike | Sophos | Server2025 | No | L1 |
| T13-HV-SOPH-S25 | T13 | Fiber-based Process Injection | Havoc | Sophos | Server2025 | No | L1 |
| T13-AX-SOPH-S25 | T13 | Fiber-based Process Injection | AdaptixC2 | Sophos | Server2025 | No | L1 |
| T13-CS-KASP-W11 | T13 | Fiber-based Process Injection | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T13-HV-KASP-W11 | T13 | Fiber-based Process Injection | Havoc | Kaspersky | Win11Enterprise | No | L2 |
| T13-AX-KASP-W11 | T13 | Fiber-based Process Injection | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T13-CS-KASP-S25 | T13 | Fiber-based Process Injection | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T13-HV-KASP-S25 | T13 | Fiber-based Process Injection | Havoc | Kaspersky | Server2025 | No | L2 |
| T13-AX-KASP-S25 | T13 | Fiber-based Process Injection | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T13-CS-BITD-W11 | T13 | Fiber-based Process Injection | CobaltStrike | Bitdefender | Win11Enterprise | No | L1 |
| T13-HV-BITD-W11 | T13 | Fiber-based Process Injection | Havoc | Bitdefender | Win11Enterprise | No | L1 |
| T13-AX-BITD-W11 | T13 | Fiber-based Process Injection | AdaptixC2 | Bitdefender | Win11Enterprise | No | L1 |
| T13-CS-BITD-S25 | T13 | Fiber-based Process Injection | CobaltStrike | Bitdefender | Server2025 | No | L1 |
| T13-HV-BITD-S25 | T13 | Fiber-based Process Injection | Havoc | Bitdefender | Server2025 | No | L1 |
| T13-AX-BITD-S25 | T13 | Fiber-based Process Injection | AdaptixC2 | Bitdefender | Server2025 | No | L1 |
| T13-CS-ELAS-W11 | T13 | Fiber-based Process Injection | CobaltStrike | Elastic | Win11Enterprise | No | L3 |
| T13-HV-ELAS-W11 | T13 | Fiber-based Process Injection | Havoc | Elastic | Win11Enterprise | No | L3 |
| T13-AX-ELAS-W11 | T13 | Fiber-based Process Injection | AdaptixC2 | Elastic | Win11Enterprise | No | L3 |
| T13-CS-ELAS-S25 | T13 | Fiber-based Process Injection | CobaltStrike | Elastic | Server2025 | No | L3 |
| T13-HV-ELAS-S25 | T13 | Fiber-based Process Injection | Havoc | Elastic | Server2025 | No | L3 |
| T13-AX-ELAS-S25 | T13 | Fiber-based Process Injection | AdaptixC2 | Elastic | Server2025 | No | L3 |
| T13-CS-HUOR-W11 | T13 | Fiber-based Process Injection | CobaltStrike | Huorong | Win11Enterprise | No | L2 |
| T13-HV-HUOR-W11 | T13 | Fiber-based Process Injection | Havoc | Huorong | Win11Enterprise | No | L5 |
| T13-AX-HUOR-W11 | T13 | Fiber-based Process Injection | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T13-CS-HUOR-S25 | T13 | Fiber-based Process Injection | CobaltStrike | Huorong | Server2025 | No | L2 |
| T13-HV-HUOR-S25 | T13 | Fiber-based Process Injection | Havoc | Huorong | Server2025 | No | L5 |
| T13-AX-HUOR-S25 | T13 | Fiber-based Process Injection | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T13-CS-MDAV-W11 | T13 | Fiber-based Process Injection | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T13-HV-MDAV-W11 | T13 | Fiber-based Process Injection | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T13-AX-MDAV-W11 | T13 | Fiber-based Process Injection | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T13-CS-MDAV-S25 | T13 | Fiber-based Process Injection | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T13-HV-MDAV-S25 | T13 | Fiber-based Process Injection | Havoc | DefenderAV | Server2025 | No | L5 |
| T13-AX-MDAV-S25 | T13 | Fiber-based Process Injection | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T14-CS-SOPH-W11 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Sophos | Win11Enterprise | No | L1 |
| T14-HV-SOPH-W11 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Sophos | Win11Enterprise | No | L1 |
| T14-AX-SOPH-W11 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Sophos | Win11Enterprise | No | L1 |
| T14-CS-SOPH-S25 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Sophos | Server2025 | No | L1 |
| T14-HV-SOPH-S25 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Sophos | Server2025 | No | L1 |
| T14-AX-SOPH-S25 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Sophos | Server2025 | No | L1 |
| T14-CS-KASP-W11 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Kaspersky | Win11Enterprise | No | L1 |
| T14-HV-KASP-W11 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T14-AX-KASP-W11 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T14-CS-KASP-S25 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Kaspersky | Server2025 | No | L1 |
| T14-HV-KASP-S25 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Kaspersky | Server2025 | No | L1 |
| T14-AX-KASP-S25 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T14-CS-BITD-W11 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T14-HV-BITD-W11 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T14-AX-BITD-W11 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T14-CS-BITD-S25 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T14-HV-BITD-S25 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Bitdefender | Server2025 | No | L2 |
| T14-AX-BITD-S25 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T14-CS-ELAS-W11 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T14-HV-ELAS-W11 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Elastic | Win11Enterprise | No | L1 |
| T14-AX-ELAS-W11 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T14-CS-ELAS-S25 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Elastic | Server2025 | No | L1 |
| T14-HV-ELAS-S25 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Elastic | Server2025 | No | L1 |
| T14-AX-ELAS-S25 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T14-CS-HUOR-W11 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Huorong | Win11Enterprise | No | L1 |
| T14-HV-HUOR-W11 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Huorong | Win11Enterprise | No | L1 |
| T14-AX-HUOR-W11 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Huorong | Win11Enterprise | No | L1 |
| T14-CS-HUOR-S25 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | Huorong | Server2025 | No | L1 |
| T14-HV-HUOR-S25 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | Huorong | Server2025 | No | L1 |
| T14-AX-HUOR-S25 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | Huorong | Server2025 | No | L1 |
| T14-CS-MDAV-W11 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | DefenderAV | Win11Enterprise | No | L1 |
| T14-HV-MDAV-W11 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | DefenderAV | Win11Enterprise | No | L1 |
| T14-AX-MDAV-W11 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | DefenderAV | Win11Enterprise | No | L1 |
| T14-CS-MDAV-S25 | T14 | Thread Pool-based Injection (PoolParty) | CobaltStrike | DefenderAV | Server2025 | No | L1 |
| T14-HV-MDAV-S25 | T14 | Thread Pool-based Injection (PoolParty) | Havoc | DefenderAV | Server2025 | No | L1 |
| T14-AX-MDAV-S25 | T14 | Thread Pool-based Injection (PoolParty) | AdaptixC2 | DefenderAV | Server2025 | No | L1 |
| T15-CS-SOPH-W11 | T15 | Process Hollowing | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T15-HV-SOPH-W11 | T15 | Process Hollowing | Havoc | Sophos | Win11Enterprise | No | L2 |
| T15-AX-SOPH-W11 | T15 | Process Hollowing | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T15-CS-SOPH-S25 | T15 | Process Hollowing | CobaltStrike | Sophos | Server2025 | No | L2 |
| T15-HV-SOPH-S25 | T15 | Process Hollowing | Havoc | Sophos | Server2025 | No | L2 |
| T15-AX-SOPH-S25 | T15 | Process Hollowing | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T15-CS-KASP-W11 | T15 | Process Hollowing | CobaltStrike | Kaspersky | Win11Enterprise | No | L1 |
| T15-HV-KASP-W11 | T15 | Process Hollowing | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T15-AX-KASP-W11 | T15 | Process Hollowing | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T15-CS-KASP-S25 | T15 | Process Hollowing | CobaltStrike | Kaspersky | Server2025 | No | L1 |
| T15-HV-KASP-S25 | T15 | Process Hollowing | Havoc | Kaspersky | Server2025 | No | L1 |
| T15-AX-KASP-S25 | T15 | Process Hollowing | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T15-CS-BITD-W11 | T15 | Process Hollowing | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T15-HV-BITD-W11 | T15 | Process Hollowing | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T15-AX-BITD-W11 | T15 | Process Hollowing | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T15-CS-BITD-S25 | T15 | Process Hollowing | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T15-HV-BITD-S25 | T15 | Process Hollowing | Havoc | Bitdefender | Server2025 | No | L2 |
| T15-AX-BITD-S25 | T15 | Process Hollowing | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T15-CS-ELAS-W11 | T15 | Process Hollowing | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T15-HV-ELAS-W11 | T15 | Process Hollowing | Havoc | Elastic | Win11Enterprise | No | L1 |
| T15-AX-ELAS-W11 | T15 | Process Hollowing | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T15-CS-ELAS-S25 | T15 | Process Hollowing | CobaltStrike | Elastic | Server2025 | No | L1 |
| T15-HV-ELAS-S25 | T15 | Process Hollowing | Havoc | Elastic | Server2025 | No | L1 |
| T15-AX-ELAS-S25 | T15 | Process Hollowing | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T15-CS-HUOR-W11 | T15 | Process Hollowing | CobaltStrike | Huorong | Win11Enterprise | No | L2 |
| T15-HV-HUOR-W11 | T15 | Process Hollowing | Havoc | Huorong | Win11Enterprise | No | L2 |
| T15-AX-HUOR-W11 | T15 | Process Hollowing | AdaptixC2 | Huorong | Win11Enterprise | No | L2 |
| T15-CS-HUOR-S25 | T15 | Process Hollowing | CobaltStrike | Huorong | Server2025 | No | L2 |
| T15-HV-HUOR-S25 | T15 | Process Hollowing | Havoc | Huorong | Server2025 | No | L2 |
| T15-AX-HUOR-S25 | T15 | Process Hollowing | AdaptixC2 | Huorong | Server2025 | No | L2 |
| T15-CS-MDAV-W11 | T15 | Process Hollowing | CobaltStrike | DefenderAV | Win11Enterprise | No | L5 |
| T15-HV-MDAV-W11 | T15 | Process Hollowing | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T15-AX-MDAV-W11 | T15 | Process Hollowing | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T15-CS-MDAV-S25 | T15 | Process Hollowing | CobaltStrike | DefenderAV | Server2025 | No | L5 |
| T15-HV-MDAV-S25 | T15 | Process Hollowing | Havoc | DefenderAV | Server2025 | No | L5 |
| T15-AX-MDAV-S25 | T15 | Process Hollowing | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T16-CS-SOPH-W11 | T16 | Module Stomping | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T16-HV-SOPH-W11 | T16 | Module Stomping | Havoc | Sophos | Win11Enterprise | No | L2 |
| T16-AX-SOPH-W11 | T16 | Module Stomping | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T16-CS-SOPH-S25 | T16 | Module Stomping | CobaltStrike | Sophos | Server2025 | No | L2 |
| T16-HV-SOPH-S25 | T16 | Module Stomping | Havoc | Sophos | Server2025 | No | L2 |
| T16-AX-SOPH-S25 | T16 | Module Stomping | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T16-CS-KASP-W11 | T16 | Module Stomping | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T16-HV-KASP-W11 | T16 | Module Stomping | Havoc | Kaspersky | Win11Enterprise | No | L2 |
| T16-AX-KASP-W11 | T16 | Module Stomping | AdaptixC2 | Kaspersky | Win11Enterprise | No | L2 |
| T16-CS-KASP-S25 | T16 | Module Stomping | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T16-HV-KASP-S25 | T16 | Module Stomping | Havoc | Kaspersky | Server2025 | No | L2 |
| T16-AX-KASP-S25 | T16 | Module Stomping | AdaptixC2 | Kaspersky | Server2025 | No | L2 |
| T16-CS-BITD-W11 | T16 | Module Stomping | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T16-HV-BITD-W11 | T16 | Module Stomping | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T16-AX-BITD-W11 | T16 | Module Stomping | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T16-CS-BITD-S25 | T16 | Module Stomping | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T16-HV-BITD-S25 | T16 | Module Stomping | Havoc | Bitdefender | Server2025 | No | L2 |
| T16-AX-BITD-S25 | T16 | Module Stomping | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T16-CS-ELAS-W11 | T16 | Module Stomping | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T16-HV-ELAS-W11 | T16 | Module Stomping | Havoc | Elastic | Win11Enterprise | No | L1 |
| T16-AX-ELAS-W11 | T16 | Module Stomping | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T16-CS-ELAS-S25 | T16 | Module Stomping | CobaltStrike | Elastic | Server2025 | No | L1 |
| T16-HV-ELAS-S25 | T16 | Module Stomping | Havoc | Elastic | Server2025 | No | L1 |
| T16-AX-ELAS-S25 | T16 | Module Stomping | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T16-CS-HUOR-W11 | T16 | Module Stomping | CobaltStrike | Huorong | Win11Enterprise | No | L4 |
| T16-HV-HUOR-W11 | T16 | Module Stomping | Havoc | Huorong | Win11Enterprise | No | L5 |
| T16-AX-HUOR-W11 | T16 | Module Stomping | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T16-CS-HUOR-S25 | T16 | Module Stomping | CobaltStrike | Huorong | Server2025 | No | L4 |
| T16-HV-HUOR-S25 | T16 | Module Stomping | Havoc | Huorong | Server2025 | No | L5 |
| T16-AX-HUOR-S25 | T16 | Module Stomping | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T16-CS-MDAV-W11 | T16 | Module Stomping | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T16-HV-MDAV-W11 | T16 | Module Stomping | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T16-AX-MDAV-W11 | T16 | Module Stomping | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T16-CS-MDAV-S25 | T16 | Module Stomping | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T16-HV-MDAV-S25 | T16 | Module Stomping | Havoc | DefenderAV | Server2025 | No | L5 |
| T16-AX-MDAV-S25 | T16 | Module Stomping | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T17-CS-SOPH-W11 | T17 | Code Packing (UPX) | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T17-HV-SOPH-W11 | T17 | Code Packing (UPX) | Havoc | Sophos | Win11Enterprise | No | L2 |
| T17-AX-SOPH-W11 | T17 | Code Packing (UPX) | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T17-CS-SOPH-S25 | T17 | Code Packing (UPX) | CobaltStrike | Sophos | Server2025 | No | L2 |
| T17-HV-SOPH-S25 | T17 | Code Packing (UPX) | Havoc | Sophos | Server2025 | No | L2 |
| T17-AX-SOPH-S25 | T17 | Code Packing (UPX) | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T17-CS-KASP-W11 | T17 | Code Packing (UPX) | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T17-HV-KASP-W11 | T17 | Code Packing (UPX) | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T17-AX-KASP-W11 | T17 | Code Packing (UPX) | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T17-CS-KASP-S25 | T17 | Code Packing (UPX) | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T17-HV-KASP-S25 | T17 | Code Packing (UPX) | Havoc | Kaspersky | Server2025 | No | L1 |
| T17-AX-KASP-S25 | T17 | Code Packing (UPX) | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T17-CS-BITD-W11 | T17 | Code Packing (UPX) | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T17-HV-BITD-W11 | T17 | Code Packing (UPX) | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T17-AX-BITD-W11 | T17 | Code Packing (UPX) | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T17-CS-BITD-S25 | T17 | Code Packing (UPX) | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T17-HV-BITD-S25 | T17 | Code Packing (UPX) | Havoc | Bitdefender | Server2025 | No | L2 |
| T17-AX-BITD-S25 | T17 | Code Packing (UPX) | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T17-CS-ELAS-W11 | T17 | Code Packing (UPX) | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T17-HV-ELAS-W11 | T17 | Code Packing (UPX) | Havoc | Elastic | Win11Enterprise | No | L1 |
| T17-AX-ELAS-W11 | T17 | Code Packing (UPX) | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T17-CS-ELAS-S25 | T17 | Code Packing (UPX) | CobaltStrike | Elastic | Server2025 | No | L1 |
| T17-HV-ELAS-S25 | T17 | Code Packing (UPX) | Havoc | Elastic | Server2025 | No | L1 |
| T17-AX-ELAS-S25 | T17 | Code Packing (UPX) | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T17-CS-HUOR-W11 | T17 | Code Packing (UPX) | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T17-HV-HUOR-W11 | T17 | Code Packing (UPX) | Havoc | Huorong | Win11Enterprise | No | L5 |
| T17-AX-HUOR-W11 | T17 | Code Packing (UPX) | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T17-CS-HUOR-S25 | T17 | Code Packing (UPX) | CobaltStrike | Huorong | Server2025 | No | L3 |
| T17-HV-HUOR-S25 | T17 | Code Packing (UPX) | Havoc | Huorong | Server2025 | No | L5 |
| T17-AX-HUOR-S25 | T17 | Code Packing (UPX) | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T17-CS-MDAV-W11 | T17 | Code Packing (UPX) | CobaltStrike | DefenderAV | Win11Enterprise | No | L1 |
| T17-HV-MDAV-W11 | T17 | Code Packing (UPX) | Havoc | DefenderAV | Win11Enterprise | No | L1 |
| T17-AX-MDAV-W11 | T17 | Code Packing (UPX) | AdaptixC2 | DefenderAV | Win11Enterprise | No | L1 |
| T17-CS-MDAV-S25 | T17 | Code Packing (UPX) | CobaltStrike | DefenderAV | Server2025 | No | L1 |
| T17-HV-MDAV-S25 | T17 | Code Packing (UPX) | Havoc | DefenderAV | Server2025 | No | L1 |
| T17-AX-MDAV-S25 | T17 | Code Packing (UPX) | AdaptixC2 | DefenderAV | Server2025 | No | L1 |
| T18-CS-SOPH-W11 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Sophos | Win11Enterprise | No | L1 |
| T18-HV-SOPH-W11 | T18 | Code Virtualization (VMProtect) | Havoc | Sophos | Win11Enterprise | No | L1 |
| T18-AX-SOPH-W11 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Sophos | Win11Enterprise | No | L1 |
| T18-CS-SOPH-S25 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Sophos | Server2025 | No | L1 |
| T18-HV-SOPH-S25 | T18 | Code Virtualization (VMProtect) | Havoc | Sophos | Server2025 | No | L1 |
| T18-AX-SOPH-S25 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Sophos | Server2025 | No | L1 |
| T18-CS-KASP-W11 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T18-HV-KASP-W11 | T18 | Code Virtualization (VMProtect) | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T18-AX-KASP-W11 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T18-CS-KASP-S25 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T18-HV-KASP-S25 | T18 | Code Virtualization (VMProtect) | Havoc | Kaspersky | Server2025 | No | L1 |
| T18-AX-KASP-S25 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T18-CS-BITD-W11 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T18-HV-BITD-W11 | T18 | Code Virtualization (VMProtect) | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T18-AX-BITD-W11 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T18-CS-BITD-S25 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T18-HV-BITD-S25 | T18 | Code Virtualization (VMProtect) | Havoc | Bitdefender | Server2025 | No | L2 |
| T18-AX-BITD-S25 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T18-CS-ELAS-W11 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T18-HV-ELAS-W11 | T18 | Code Virtualization (VMProtect) | Havoc | Elastic | Win11Enterprise | No | L1 |
| T18-AX-ELAS-W11 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T18-CS-ELAS-S25 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Elastic | Server2025 | No | L1 |
| T18-HV-ELAS-S25 | T18 | Code Virtualization (VMProtect) | Havoc | Elastic | Server2025 | No | L1 |
| T18-AX-ELAS-S25 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T18-CS-HUOR-W11 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T18-HV-HUOR-W11 | T18 | Code Virtualization (VMProtect) | Havoc | Huorong | Win11Enterprise | No | L5 |
| T18-AX-HUOR-W11 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T18-CS-HUOR-S25 | T18 | Code Virtualization (VMProtect) | CobaltStrike | Huorong | Server2025 | No | L3 |
| T18-HV-HUOR-S25 | T18 | Code Virtualization (VMProtect) | Havoc | Huorong | Server2025 | No | L5 |
| T18-AX-HUOR-S25 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T18-CS-MDAV-W11 | T18 | Code Virtualization (VMProtect) | CobaltStrike | DefenderAV | Win11Enterprise | No | L1 |
| T18-HV-MDAV-W11 | T18 | Code Virtualization (VMProtect) | Havoc | DefenderAV | Win11Enterprise | No | L1 |
| T18-AX-MDAV-W11 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | DefenderAV | Win11Enterprise | No | L1 |
| T18-CS-MDAV-S25 | T18 | Code Virtualization (VMProtect) | CobaltStrike | DefenderAV | Server2025 | No | L1 |
| T18-HV-MDAV-S25 | T18 | Code Virtualization (VMProtect) | Havoc | DefenderAV | Server2025 | No | L2 |
| T18-AX-MDAV-S25 | T18 | Code Virtualization (VMProtect) | AdaptixC2 | DefenderAV | Server2025 | No | L2 |
| T19-CS-SOPH-W11 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T19-HV-SOPH-W11 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Sophos | Win11Enterprise | No | L2 |
| T19-AX-SOPH-W11 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T19-CS-SOPH-S25 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Sophos | Server2025 | No | L2 |
| T19-HV-SOPH-S25 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Sophos | Server2025 | No | L2 |
| T19-AX-SOPH-S25 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T19-CS-KASP-W11 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T19-HV-KASP-W11 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T19-AX-KASP-W11 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T19-CS-KASP-S25 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T19-HV-KASP-S25 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Kaspersky | Server2025 | No | L5 |
| T19-AX-KASP-S25 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Kaspersky | Server2025 | No | L2 |
| T19-CS-BITD-W11 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T19-HV-BITD-W11 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T19-AX-BITD-W11 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T19-CS-BITD-S25 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T19-HV-BITD-S25 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Bitdefender | Server2025 | No | L2 |
| T19-AX-BITD-S25 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T19-CS-ELAS-W11 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T19-HV-ELAS-W11 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Elastic | Win11Enterprise | No | L1 |
| T19-AX-ELAS-W11 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T19-CS-ELAS-S25 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Elastic | Server2025 | No | L1 |
| T19-HV-ELAS-S25 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Elastic | Server2025 | No | L1 |
| T19-AX-ELAS-S25 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T19-CS-HUOR-W11 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T19-HV-HUOR-W11 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Huorong | Win11Enterprise | No | L5 |
| T19-AX-HUOR-W11 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T19-CS-HUOR-S25 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | Huorong | Server2025 | No | L3 |
| T19-HV-HUOR-S25 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | Huorong | Server2025 | No | L5 |
| T19-AX-HUOR-S25 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T19-CS-MDAV-W11 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | DefenderAV | Win11Enterprise | No | L1 |
| T19-HV-MDAV-W11 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | DefenderAV | Win11Enterprise | No | L1 |
| T19-AX-MDAV-W11 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | DefenderAV | Win11Enterprise | No | L1 |
| T19-CS-MDAV-S25 | T19 | Compiler-level Obfuscation (OLLVM) | CobaltStrike | DefenderAV | Server2025 | No | L1 |
| T19-HV-MDAV-S25 | T19 | Compiler-level Obfuscation (OLLVM) | Havoc | DefenderAV | Server2025 | No | L1 |
| T19-AX-MDAV-S25 | T19 | Compiler-level Obfuscation (OLLVM) | AdaptixC2 | DefenderAV | Server2025 | No | L1 |
| T20-CS-SOPH-W11 | T20 | PE Resource Masquerading | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T20-HV-SOPH-W11 | T20 | PE Resource Masquerading | Havoc | Sophos | Win11Enterprise | No | L2 |
| T20-AX-SOPH-W11 | T20 | PE Resource Masquerading | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T20-CS-SOPH-S25 | T20 | PE Resource Masquerading | CobaltStrike | Sophos | Server2025 | No | L2 |
| T20-HV-SOPH-S25 | T20 | PE Resource Masquerading | Havoc | Sophos | Server2025 | No | L2 |
| T20-AX-SOPH-S25 | T20 | PE Resource Masquerading | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T20-CS-KASP-W11 | T20 | PE Resource Masquerading | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T20-HV-KASP-W11 | T20 | PE Resource Masquerading | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T20-AX-KASP-W11 | T20 | PE Resource Masquerading | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T20-CS-KASP-S25 | T20 | PE Resource Masquerading | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T20-HV-KASP-S25 | T20 | PE Resource Masquerading | Havoc | Kaspersky | Server2025 | No | L5 |
| T20-AX-KASP-S25 | T20 | PE Resource Masquerading | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T20-CS-BITD-W11 | T20 | PE Resource Masquerading | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T20-HV-BITD-W11 | T20 | PE Resource Masquerading | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T20-AX-BITD-W11 | T20 | PE Resource Masquerading | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T20-CS-BITD-S25 | T20 | PE Resource Masquerading | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T20-HV-BITD-S25 | T20 | PE Resource Masquerading | Havoc | Bitdefender | Server2025 | No | L2 |
| T20-AX-BITD-S25 | T20 | PE Resource Masquerading | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T20-CS-ELAS-W11 | T20 | PE Resource Masquerading | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T20-HV-ELAS-W11 | T20 | PE Resource Masquerading | Havoc | Elastic | Win11Enterprise | No | L1 |
| T20-AX-ELAS-W11 | T20 | PE Resource Masquerading | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T20-CS-ELAS-S25 | T20 | PE Resource Masquerading | CobaltStrike | Elastic | Server2025 | No | L1 |
| T20-HV-ELAS-S25 | T20 | PE Resource Masquerading | Havoc | Elastic | Server2025 | No | L1 |
| T20-AX-ELAS-S25 | T20 | PE Resource Masquerading | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T20-CS-HUOR-W11 | T20 | PE Resource Masquerading | CobaltStrike | Huorong | Win11Enterprise | No | L2 |
| T20-HV-HUOR-W11 | T20 | PE Resource Masquerading | Havoc | Huorong | Win11Enterprise | No | L5 |
| T20-AX-HUOR-W11 | T20 | PE Resource Masquerading | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T20-CS-HUOR-S25 | T20 | PE Resource Masquerading | CobaltStrike | Huorong | Server2025 | No | L2 |
| T20-HV-HUOR-S25 | T20 | PE Resource Masquerading | Havoc | Huorong | Server2025 | No | L5 |
| T20-AX-HUOR-S25 | T20 | PE Resource Masquerading | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T20-CS-MDAV-W11 | T20 | PE Resource Masquerading | CobaltStrike | DefenderAV | Win11Enterprise | No | L2 |
| T20-HV-MDAV-W11 | T20 | PE Resource Masquerading | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T20-AX-MDAV-W11 | T20 | PE Resource Masquerading | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T20-CS-MDAV-S25 | T20 | PE Resource Masquerading | CobaltStrike | DefenderAV | Server2025 | No | L2 |
| T20-HV-MDAV-S25 | T20 | PE Resource Masquerading | Havoc | DefenderAV | Server2025 | No | L5 |
| T20-AX-MDAV-S25 | T20 | PE Resource Masquerading | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T21-CS-SOPH-W11 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T21-HV-SOPH-W11 | T21 | API-level Behavioral Obfuscation | Havoc | Sophos | Win11Enterprise | No | L2 |
| T21-AX-SOPH-W11 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T21-CS-SOPH-S25 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Sophos | Server2025 | No | L2 |
| T21-HV-SOPH-S25 | T21 | API-level Behavioral Obfuscation | Havoc | Sophos | Server2025 | No | L2 |
| T21-AX-SOPH-S25 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T21-CS-KASP-W11 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Kaspersky | Win11Enterprise | No | L2 |
| T21-HV-KASP-W11 | T21 | API-level Behavioral Obfuscation | Havoc | Kaspersky | Win11Enterprise | No | L5 |
| T21-AX-KASP-W11 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Kaspersky | Win11Enterprise | No | L3 |
| T21-CS-KASP-S25 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Kaspersky | Server2025 | No | L2 |
| T21-HV-KASP-S25 | T21 | API-level Behavioral Obfuscation | Havoc | Kaspersky | Server2025 | No | L5 |
| T21-AX-KASP-S25 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Kaspersky | Server2025 | No | L3 |
| T21-CS-BITD-W11 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T21-HV-BITD-W11 | T21 | API-level Behavioral Obfuscation | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T21-AX-BITD-W11 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T21-CS-BITD-S25 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T21-HV-BITD-S25 | T21 | API-level Behavioral Obfuscation | Havoc | Bitdefender | Server2025 | No | L2 |
| T21-AX-BITD-S25 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T21-CS-ELAS-W11 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Elastic | Win11Enterprise | No | L2 |
| T21-HV-ELAS-W11 | T21 | API-level Behavioral Obfuscation | Havoc | Elastic | Win11Enterprise | No | L2 |
| T21-AX-ELAS-W11 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Elastic | Win11Enterprise | No | L2 |
| T21-CS-ELAS-S25 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Elastic | Server2025 | No | L2 |
| T21-HV-ELAS-S25 | T21 | API-level Behavioral Obfuscation | Havoc | Elastic | Server2025 | No | L2 |
| T21-AX-ELAS-S25 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Elastic | Server2025 | No | L2 |
| T21-CS-HUOR-W11 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Huorong | Win11Enterprise | No | L2 |
| T21-HV-HUOR-W11 | T21 | API-level Behavioral Obfuscation | Havoc | Huorong | Win11Enterprise | No | L5 |
| T21-AX-HUOR-W11 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T21-CS-HUOR-S25 | T21 | API-level Behavioral Obfuscation | CobaltStrike | Huorong | Server2025 | No | L2 |
| T21-HV-HUOR-S25 | T21 | API-level Behavioral Obfuscation | Havoc | Huorong | Server2025 | No | L5 |
| T21-AX-HUOR-S25 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T21-CS-MDAV-W11 | T21 | API-level Behavioral Obfuscation | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T21-HV-MDAV-W11 | T21 | API-level Behavioral Obfuscation | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T21-AX-MDAV-W11 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T21-CS-MDAV-S25 | T21 | API-level Behavioral Obfuscation | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T21-HV-MDAV-S25 | T21 | API-level Behavioral Obfuscation | Havoc | DefenderAV | Server2025 | No | L5 |
| T21-AX-MDAV-S25 | T21 | API-level Behavioral Obfuscation | AdaptixC2 | DefenderAV | Server2025 | No | L5 |
| T22-CS-SOPH-W11 | T22 | COM-based Process Creation | CobaltStrike | Sophos | Win11Enterprise | No | L2 |
| T22-HV-SOPH-W11 | T22 | COM-based Process Creation | Havoc | Sophos | Win11Enterprise | No | L2 |
| T22-AX-SOPH-W11 | T22 | COM-based Process Creation | AdaptixC2 | Sophos | Win11Enterprise | No | L2 |
| T22-CS-SOPH-S25 | T22 | COM-based Process Creation | CobaltStrike | Sophos | Server2025 | No | L2 |
| T22-HV-SOPH-S25 | T22 | COM-based Process Creation | Havoc | Sophos | Server2025 | No | L2 |
| T22-AX-SOPH-S25 | T22 | COM-based Process Creation | AdaptixC2 | Sophos | Server2025 | No | L2 |
| T22-CS-KASP-W11 | T22 | COM-based Process Creation | CobaltStrike | Kaspersky | Win11Enterprise | No | L1 |
| T22-HV-KASP-W11 | T22 | COM-based Process Creation | Havoc | Kaspersky | Win11Enterprise | No | L1 |
| T22-AX-KASP-W11 | T22 | COM-based Process Creation | AdaptixC2 | Kaspersky | Win11Enterprise | No | L1 |
| T22-CS-KASP-S25 | T22 | COM-based Process Creation | CobaltStrike | Kaspersky | Server2025 | No | L1 |
| T22-HV-KASP-S25 | T22 | COM-based Process Creation | Havoc | Kaspersky | Server2025 | No | L1 |
| T22-AX-KASP-S25 | T22 | COM-based Process Creation | AdaptixC2 | Kaspersky | Server2025 | No | L1 |
| T22-CS-BITD-W11 | T22 | COM-based Process Creation | CobaltStrike | Bitdefender | Win11Enterprise | No | L2 |
| T22-HV-BITD-W11 | T22 | COM-based Process Creation | Havoc | Bitdefender | Win11Enterprise | No | L2 |
| T22-AX-BITD-W11 | T22 | COM-based Process Creation | AdaptixC2 | Bitdefender | Win11Enterprise | No | L2 |
| T22-CS-BITD-S25 | T22 | COM-based Process Creation | CobaltStrike | Bitdefender | Server2025 | No | L2 |
| T22-HV-BITD-S25 | T22 | COM-based Process Creation | Havoc | Bitdefender | Server2025 | No | L2 |
| T22-AX-BITD-S25 | T22 | COM-based Process Creation | AdaptixC2 | Bitdefender | Server2025 | No | L2 |
| T22-CS-ELAS-W11 | T22 | COM-based Process Creation | CobaltStrike | Elastic | Win11Enterprise | No | L1 |
| T22-HV-ELAS-W11 | T22 | COM-based Process Creation | Havoc | Elastic | Win11Enterprise | No | L1 |
| T22-AX-ELAS-W11 | T22 | COM-based Process Creation | AdaptixC2 | Elastic | Win11Enterprise | No | L1 |
| T22-CS-ELAS-S25 | T22 | COM-based Process Creation | CobaltStrike | Elastic | Server2025 | No | L1 |
| T22-HV-ELAS-S25 | T22 | COM-based Process Creation | Havoc | Elastic | Server2025 | No | L1 |
| T22-AX-ELAS-S25 | T22 | COM-based Process Creation | AdaptixC2 | Elastic | Server2025 | No | L1 |
| T22-CS-HUOR-W11 | T22 | COM-based Process Creation | CobaltStrike | Huorong | Win11Enterprise | No | L3 |
| T22-HV-HUOR-W11 | T22 | COM-based Process Creation | Havoc | Huorong | Win11Enterprise | No | L5 |
| T22-AX-HUOR-W11 | T22 | COM-based Process Creation | AdaptixC2 | Huorong | Win11Enterprise | No | L5 |
| T22-CS-HUOR-S25 | T22 | COM-based Process Creation | CobaltStrike | Huorong | Server2025 | No | L3 |
| T22-HV-HUOR-S25 | T22 | COM-based Process Creation | Havoc | Huorong | Server2025 | No | L5 |
| T22-AX-HUOR-S25 | T22 | COM-based Process Creation | AdaptixC2 | Huorong | Server2025 | No | L5 |
| T22-CS-MDAV-W11 | T22 | COM-based Process Creation | CobaltStrike | DefenderAV | Win11Enterprise | No | L3 |
| T22-HV-MDAV-W11 | T22 | COM-based Process Creation | Havoc | DefenderAV | Win11Enterprise | No | L5 |
| T22-AX-MDAV-W11 | T22 | COM-based Process Creation | AdaptixC2 | DefenderAV | Win11Enterprise | No | L5 |
| T22-CS-MDAV-S25 | T22 | COM-based Process Creation | CobaltStrike | DefenderAV | Server2025 | No | L3 |
| T22-HV-MDAV-S25 | T22 | COM-based Process Creation | Havoc | DefenderAV | Server2025 | No | L5 |
| T22-AX-MDAV-S25 | T22 | COM-based Process Creation | AdaptixC2 | DefenderAV | Server2025 | No | L5 |

## Calculation and provenance

PSD normalizes level counts by the number of non-baseline cases for a product (132). BDD normalizes by the cases for an implementation (36) or a DET group (36 times its number of implementations). Percentages are rounded to one decimal place. Run `python framework/tools/export_results.py` and `python framework/metrics.py` from the repository root. The manuscript is the authority for the labels; original screenshots and full logs are retained internally. [PROVENANCE.json](PROVENANCE.json) records the source-table and dataset fingerprints.
