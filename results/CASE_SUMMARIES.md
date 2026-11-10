# Test Case Summaries

These descriptions state the final outcomes of the completed experiments using the manuscript L1-L5 criteria. All 828 labels match [outcomes_scored.csv](outcomes_scored.csv) and [FINAL_RESULTS.md](FINAL_RESULTS.md). Original screenshots, full logs and infrastructure identifiers are not included. See [the test protocol](../framework/TEST_PROTOCOL.md).

## T0. AES-protected Baseline Payload (no additional evasion logic)

### T0: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-SOPH-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-SOPH-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-SOPH-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-SOPH-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-SOPH-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-SOPH-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-KASP-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-KASP-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-BITD-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-BITD-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-BITD-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-BITD-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-BITD-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-BITD-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-HUOR-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-HUOR-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-HUOR-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-HUOR-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-HUOR-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-HUOR-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-MDAV-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-MDAV-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-MDAV-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T0: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T0-CS-MDAV-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T0-HV-MDAV-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T0-AX-MDAV-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

## T1. Direct Syscall Invocation

### T1: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T1: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T1: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T1-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T1: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T1-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T1: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T1: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T1-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T1: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T1-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T1-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T1: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T1-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T1-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T1: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T1-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T1-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T1: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T1-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T1-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T1: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T1-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T1-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T1: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T1-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T1-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T1-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T2. ETW & AMSI Patching

### T2: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T2: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T2: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T2-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T2: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T2-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T2: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T2: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T2-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T2: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T2-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T2-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T2: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T2-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T2-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T2: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T2-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T2-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T2: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T2-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T2-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T2: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T2-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T2-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T2: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T2-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T2-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T2-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T3. DLL Signature Restriction

### T3: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T3: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T3: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-HV-KASP-W11 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T3-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T3: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-HV-KASP-S25 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T3-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T3: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T3: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T3-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T3: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T3-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T3-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T3: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T3-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T3-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T3: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-HUOR-W11 | CobaltStrike | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T3-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T3-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T3: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-HUOR-S25 | CobaltStrike | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T3-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T3-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T3: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T3-HV-MDAV-W11 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T3-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T3: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T3-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T3-HV-MDAV-S25 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T3-AX-MDAV-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

## T4. Hook Overwriting

### T4: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-KASP-W11 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T4-AX-KASP-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-KASP-S25 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T4-AX-KASP-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T4-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T4-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T4: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T4-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T4-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T4: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-HUOR-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T4-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T4-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T4: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-HUOR-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T4-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T4-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T4: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-MDAV-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T4-AX-MDAV-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T4: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T4-CS-MDAV-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T4-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T4-AX-MDAV-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

## T5. NTDLL Hook Removal

### T5: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T5: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T5: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T5-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T5: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T5-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T5: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T5: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T5-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T5: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T5-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T5-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T5: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T5-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T5-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T5: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-HUOR-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T5-HV-HUOR-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T5-AX-HUOR-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T5: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-HUOR-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T5-HV-HUOR-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T5-AX-HUOR-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T5: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T5-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T5-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T5: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T5-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T5-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T5-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T6. Kernel Callback Removal

### T6: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T6: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T6: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-HV-KASP-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-AX-KASP-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T6: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-HV-KASP-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-AX-KASP-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T6: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-BITD-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T6-HV-BITD-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T6-AX-BITD-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T6: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-BITD-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T6-HV-BITD-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T6-AX-BITD-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T6: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-ELAS-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-HV-ELAS-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-AX-ELAS-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T6: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-ELAS-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-HV-ELAS-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T6-AX-ELAS-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T6: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-HUOR-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T6-HV-HUOR-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T6-AX-HUOR-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T6: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-HUOR-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T6-HV-HUOR-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T6-AX-HUOR-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T6: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-MDAV-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T6-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T6-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T6: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T6-CS-MDAV-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T6-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T6-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T7. Symlink-based EDR Corruption

### T7: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-SOPH-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-HV-SOPH-W11 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-AX-SOPH-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T7: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-SOPH-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-HV-SOPH-S25 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-AX-SOPH-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T7: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-KASP-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-KASP-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-KASP-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-KASP-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-BITD-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-HV-BITD-W11 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-AX-BITD-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T7: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-BITD-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-HV-BITD-S25 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T7-AX-BITD-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T7: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-ELAS-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-ELAS-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-ELAS-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-ELAS-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-ELAS-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-ELAS-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-HUOR-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-HUOR-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-MDAV-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T7: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T7-CS-MDAV-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T7-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T8. EDR Process Termination

### T8: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-SOPH-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-SOPH-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-SOPH-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-SOPH-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-SOPH-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-SOPH-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T8-HV-KASP-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T8-AX-KASP-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T8: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T8-HV-KASP-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T8-AX-KASP-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T8: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-BITD-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-BITD-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-BITD-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-BITD-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-BITD-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-BITD-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-HUOR-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-HUOR-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-HUOR-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-HUOR-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T8-HV-HUOR-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T8-AX-HUOR-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T8: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-MDAV-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T8-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T8-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T8: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T8-CS-MDAV-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T8-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T8-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T9. EDRSilencer

### T9: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T9: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T9: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-KASP-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T9-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T9-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T9: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-KASP-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T9-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T9-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T9: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T9: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T9-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T9: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-ELAS-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-HV-ELAS-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-AX-ELAS-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T9: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-ELAS-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-HV-ELAS-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-AX-ELAS-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T9: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-HUOR-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T9: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-HUOR-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T9-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T9: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-MDAV-W11 | CobaltStrike | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T9-HV-MDAV-W11 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T9-AX-MDAV-W11 | AdaptixC2 | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |

### T9: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T9-CS-MDAV-S25 | CobaltStrike | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T9-HV-MDAV-S25 | Havoc | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T9-AX-MDAV-S25 | AdaptixC2 | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |

## T10. COM Hijacking

### T10: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T10: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T10: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T10-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T10: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T10-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T10: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T10: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T10: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-ELAS-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-ELAS-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-AX-ELAS-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T10: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-ELAS-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-HV-ELAS-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T10-AX-ELAS-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T10: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T10-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T10-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T10: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T10-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T10-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T10: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T10-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T10-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T10: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T10-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T10-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T10-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T11. DLL Hijacking

### T11: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T11: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T11: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-AX-KASP-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T11: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-AX-KASP-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T11: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T11: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T11: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-ELAS-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T11-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T11-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T11: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-ELAS-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T11-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T11-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T11: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-HUOR-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T11: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-HUOR-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T11-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T11: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-MDAV-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T11: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T11-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T11-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T11-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T12. COM-based Process Injection

### T12: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T12: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T12: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-KASP-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-AX-KASP-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T12: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-KASP-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-AX-KASP-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T12: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T12: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T12: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-ELAS-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T12-HV-ELAS-W11 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T12-AX-ELAS-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T12: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-ELAS-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T12-HV-ELAS-S25 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T12-AX-ELAS-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T12: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-HUOR-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T12-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T12-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T12: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-HUOR-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T12-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T12-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T12: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T12-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T12-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T12: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T12-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T12-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T12-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T13. Fiber-based Process Injection

### T13: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-SOPH-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T13-HV-SOPH-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T13-AX-SOPH-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T13: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-SOPH-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T13-HV-SOPH-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T13-AX-SOPH-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T13: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T13-HV-KASP-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T13-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T13: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T13-HV-KASP-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T13-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T13: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-BITD-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T13-HV-BITD-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T13-AX-BITD-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T13: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-BITD-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T13-HV-BITD-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T13-AX-BITD-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T13: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-ELAS-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T13-HV-ELAS-W11 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T13-AX-ELAS-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T13: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-ELAS-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T13-HV-ELAS-S25 | Havoc | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T13-AX-ELAS-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T13: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-HUOR-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T13-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T13-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T13: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-HUOR-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T13-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T13-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T13: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T13-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T13-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T13: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T13-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T13-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T13-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T14. Thread Pool-based Injection (PoolParty)

### T14: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-SOPH-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-SOPH-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-SOPH-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-SOPH-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-SOPH-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-SOPH-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-KASP-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-KASP-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T14-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T14-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T14: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T14-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T14-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T14: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-HUOR-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-HUOR-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-HUOR-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-HUOR-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-HUOR-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-HUOR-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-MDAV-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-MDAV-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-MDAV-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T14: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T14-CS-MDAV-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T14-HV-MDAV-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T14-AX-MDAV-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

## T15. Process Hollowing

### T15: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T15: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T15: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-KASP-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T15-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T15-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T15: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-KASP-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T15-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T15-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T15: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T15: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T15: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T15-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T15-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T15: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T15-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T15-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T15: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-HUOR-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-HV-HUOR-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-AX-HUOR-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T15: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-HUOR-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-HV-HUOR-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T15-AX-HUOR-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T15: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-MDAV-W11 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T15-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T15-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T15: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T15-CS-MDAV-S25 | CobaltStrike | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T15-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T15-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T16. Module Stomping

### T16: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T16: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T16: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-HV-KASP-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-AX-KASP-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T16: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-HV-KASP-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-AX-KASP-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T16: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T16: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T16-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T16: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T16-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T16-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T16: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T16-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T16-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T16: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-HUOR-W11 | CobaltStrike | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T16-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T16-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T16: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-HUOR-S25 | CobaltStrike | L4 | Commands were sent but did not complete successfully, or the session was terminated within the command-stage observation window. |
| T16-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T16-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T16: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T16-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T16-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T16: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T16-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T16-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T16-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T17. Code Packing (UPX)

### T17: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T17: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T17: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T17-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T17: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T17-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T17: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T17: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T17-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T17: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T17-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T17-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T17: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T17-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T17-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T17: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T17-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T17-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T17: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T17-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T17-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T17: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-MDAV-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T17-HV-MDAV-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T17-AX-MDAV-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T17: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T17-CS-MDAV-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T17-HV-MDAV-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T17-AX-MDAV-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

## T18. Code Virtualization (VMProtect)

### T18: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-SOPH-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T18-HV-SOPH-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-SOPH-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-SOPH-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T18-HV-SOPH-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-SOPH-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T18: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T18: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T18-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T18-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T18-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T18-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T18: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T18-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T18-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T18: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-MDAV-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T18-HV-MDAV-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T18-AX-MDAV-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T18: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T18-CS-MDAV-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T18-HV-MDAV-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T18-AX-MDAV-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

## T19. Compiler-level Obfuscation (OLLVM)

### T19: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T19: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T19: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T19-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T19: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T19-AX-KASP-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T19: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T19: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T19-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T19: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T19-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T19-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T19: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T19-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T19-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T19: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T19-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T19-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T19: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T19-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T19-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T19: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-MDAV-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T19-HV-MDAV-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T19-AX-MDAV-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T19: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T19-CS-MDAV-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T19-HV-MDAV-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T19-AX-MDAV-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

## T20. PE Resource Masquerading

### T20: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T20: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T20: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T20-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T20: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T20-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T20: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T20: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T20: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T20-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T20-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T20: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T20-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T20-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T20: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-HUOR-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T20-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T20: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-HUOR-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T20-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T20: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-MDAV-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T20-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T20: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T20-CS-MDAV-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T20-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T20-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T21. API-level Behavioral Obfuscation

### T21: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T21: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T21: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-KASP-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-KASP-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T21-AX-KASP-W11 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T21: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-KASP-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-KASP-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T21-AX-KASP-S25 | AdaptixC2 | L3 | C2 was established, but the product terminated the session before any command was sent. |

### T21: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T21: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T21: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-ELAS-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-ELAS-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-AX-ELAS-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T21: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-ELAS-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-ELAS-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-AX-ELAS-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T21: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-HUOR-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T21-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T21: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-HUOR-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T21-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T21-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T21: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T21-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T21-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T21: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T21-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T21-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T21-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

## T22. COM-based Process Creation

### T22: Sophos / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-SOPH-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-HV-SOPH-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-AX-SOPH-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T22: Sophos / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-SOPH-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-HV-SOPH-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-AX-SOPH-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T22: Kaspersky / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-KASP-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T22-HV-KASP-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T22-AX-KASP-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T22: Kaspersky / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-KASP-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T22-HV-KASP-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T22-AX-KASP-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T22: Bitdefender / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-BITD-W11 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-HV-BITD-W11 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-AX-BITD-W11 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T22: Bitdefender / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-BITD-S25 | CobaltStrike | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-HV-BITD-S25 | Havoc | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |
| T22-AX-BITD-S25 | AdaptixC2 | L2 | The process ran, but the product terminated it before C2 establishment within the 60-second timeout. |

### T22: Elastic / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-ELAS-W11 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T22-HV-ELAS-W11 | Havoc | L1 | The product blocked the sample before process creation. |
| T22-AX-ELAS-W11 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T22: Elastic / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-ELAS-S25 | CobaltStrike | L1 | The product blocked the sample before process creation. |
| T22-HV-ELAS-S25 | Havoc | L1 | The product blocked the sample before process creation. |
| T22-AX-ELAS-S25 | AdaptixC2 | L1 | The product blocked the sample before process creation. |

### T22: Huorong / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-HUOR-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T22-HV-HUOR-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T22-AX-HUOR-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T22: Huorong / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-HUOR-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T22-HV-HUOR-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T22-AX-HUOR-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T22: DefenderAV / Win11Enterprise

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-MDAV-W11 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T22-HV-MDAV-W11 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T22-AX-MDAV-W11 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |

### T22: DefenderAV / Server2025

| Case ID | Payload | Final level | Reported final outcome |
| --- | --- | --- | --- |
| T22-CS-MDAV-S25 | CobaltStrike | L3 | C2 was established, but the product terminated the session before any command was sent. |
| T22-HV-MDAV-S25 | Havoc | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
| T22-AX-MDAV-S25 | AdaptixC2 | L5 | The prescribed commands completed successfully and the session remained alive throughout the post-command observation window. |
