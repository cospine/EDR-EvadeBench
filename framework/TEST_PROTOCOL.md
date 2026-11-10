# EDR-EvadeBench: Test Protocol

## 1. Scope and version

The reported evaluation used the first adapted version of each of 22 implementations, without code revisions during the evaluation. All implementations were adapted from public code. The case matrix combines T0-T22, three payload families, six products, and two Windows environments. T0 is reported separately and excluded from PSD and BDD. Implementation projects and their build instructions are in the repository technique directories; see [BUILD.md](../BUILD.md). Payload binaries are not included.

## 2. Test environment

| Item | Configuration |
| --- | --- |
| Virtualization | VMware Workstation 17 Pro, build 17.6.1-24319023 |
| Host CPU | Intel Core i7-13700; 16 cores / 24 threads; base frequency 3.40 GHz |
| Host RAM | 32.0 GB DDR5 4800 MT/s |
| Windows VM resources | 8 GB RAM and 80 GB NVMe virtual disk per VM |
| Windows 11 | Enterprise Evaluation, 10.0.26200, build 26200 |
| Windows Server | Server 2025 Standard Evaluation, 10.0.26100, build 26100 |
| Installation and updates | Clean official Microsoft ISO installations, patched through August 2026 |
| Product protection | Default protection configurations; see the manuscript environment table for individual features |
| Defender scope | Microsoft Defender Antivirus, without onboarding to Microsoft Defender for Endpoint |
| Network | Isolated private virtual network; NAT access for product services; C2 restricted to the private network |
| C2 hosts | Researcher-controlled Ubuntu VM; separate snapshots for the three frameworks |
| Sample submission | Disabled for all evaluated products |

| Product | Tested version |
| --- | --- |
| Sophos | Agent 2026.2.1.3.0 |
| Kaspersky Endpoint Security | 14.0.0.504 |
| Bitdefender Endpoint Security Tools | 8.26.7.647; security content 7.101269 |
| Elastic Security | 9.4.3; rule set 1.0.1969+2026-07-16-daily |
| Huorong Endpoint Security | EDR edition, client V2.0.19.6 |
| Microsoft Defender Antivirus | AM engine 1.1.26070.7; product 4.18.26070.9; signatures 1.457.11.0 |

The public description identifies machine roles rather than disclosing the original network addresses, user accounts, host identifiers, or management-instance addresses.

## 3. Payload preparation and implementation validation

The payload families are Cobalt Strike 4.8, Havoc 0.7, and AdaptixC2 1.2. Framework sources and preparation settings are described in manuscript Appendix B. All base payloads use the same AES-256-CBC encryption and runtime decryption with PKCS#7 padding. Each encryption generates a random 16-byte IV; the stored buffer contains the IV followed by the ciphertext. T0 has no additional evasion mechanism; T1-T22 integrate the base payload with the selected implementation.

Before evaluation, samples undergo mechanism-specific evasion-logic verification and payload-functionality checks. Product-dependent validation retains the required target components. Any validation exclusions are removed for formal execution. Each implementation runs with the privilege stated in the manuscript validation checklist. Initial access and privilege escalation are outside the evaluated threat model.

## 4. Execution and final-label procedure

1. Restore both the target Windows VM and the corresponding Ubuntu C2 server to their baseline snapshots before each execution.
2. Execute the selected implementation-payload variant with its required privilege and the product's default protection configuration.
3. Allow up to 60 seconds after process creation for C2 establishment.
4. After C2 establishment, observe the session for five minutes before sending commands.
5. If the session survives, execute the prescribed reconnaissance and file-transfer commands, including the activities described in the manuscript, then observe for another five minutes.
6. Determine the execution outcome using endpoint process/network state, C2 records, and product alerts or local protection logs, following the L1-L5 definitions in [results/FINAL_RESULTS.md](../results/FINAL_RESULTS.md).
7. Repeat until five consecutive executions produce the same outcome and record that outcome as the final case label. In the reported experiments, no case required more than eight runs.
8. Power off the VMs after the test and restore snapshots before the next execution.

The public dataset contains one final label per case. Repetition counts, precise event timestamps, and individual-run traces are not columns in this dataset. [results/CASE_SUMMARIES.md](../results/CASE_SUMMARIES.md) describes the final outcomes of the completed experiments.

## 5. Analysis and scope of reuse

Run `python framework/tools/export_results.py` and `python framework/metrics.py` from the repository root. Both use `results/outcomes_scored.csv`: the exporter produces readable results and case summaries; the metrics command produces PSD/BDD and other tables in `results/metrics/`. T0 is excluded from those distributions. Displayed percentages use one decimal place.

The supplied labels and script support checking the manuscript tables and recalculating their statistics. Source code and this protocol support conducting further evaluations, but exact rerun outcomes can change with payload details, product versions, configurations, and cloud services. Original screenshots and full logs contain sensitive experimental-environment information and are retained internally rather than publicly distributed.
