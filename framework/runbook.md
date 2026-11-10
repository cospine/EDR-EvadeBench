# Evaluation Runbook

The operational procedure for new evaluations using the four-stage workflow. The common protocol and published configuration are in [TEST_PROTOCOL.md](TEST_PROTOCOL.md). Parameter values are
taken from `schema/testbed.json`, which encodes Table 8 and Section 3 of
the paper; nothing here is invented.

---

## Stage 1 — Sample Generation

**Goal.** Produce, for each technique and each payload family, a build that
carries the evasion logic and an encrypted payload.

1. **Prepare the payload.** Encrypt your payload with the procedure the
   samples expect — payload buffer format `[16-byte IV] + AES-256-CBC
   ciphertext` — using the same key you will place in the sample's `AES_KEY`
   array. Every released sample ships an all-zero placeholder; see
   [../BINARY_PROVENANCE.md](../BINARY_PROVENANCE.md).
2. **Build the sample.** Follow the technique's own README and
   [../BUILD.md](../BUILD.md). Note which techniques need generated files
   (T1: SysWhispers3), external trees (T21: libcurl) or package restore
   (T14: Boost 1.82.0).
3. **Enumerate the cases.**

   ```bash
   python framework/cases.py --out results/cases.csv
   ```

   This yields the 792 non-baseline cases. The 36 baseline cases (no evasion
   logic) come from `--baseline`.

**Exit criteria.** One buildable sample per technique × payload family, and a
case list with stable case ids.

---

## Stage 2 — Function Validation

**Goal.** Make sure a failure to detect is not actually a failure to run.

1. Generate the checklist:

   ```bash
   python framework/validate.py init
   ```

   Two rows per technique: *evasion logic* and *payload functionality*. The
   evasion-logic criterion is the one from Table 7.

2. **Run the checks under the right configuration.** `validation_config` in
   the checklist is `clean-baseline` for most techniques and
   `product-present` for T4 and T6–T9, which manipulate EDR hooks, callbacks,
   agent resources, protected processes, or telemetry channels. For those,
   install the product and keep the target components active; where an
   enforcement function would interrupt the sample mid-run, put it in audit
   mode or exclude it narrowly, and record that you did.

3. **Evasion-logic check.** Confirm the post-condition. For state-dependent
   techniques, confirm the target state exists *before* the run and the change
   after — for example, an EDR hook present before and absent after.

4. **Payload-functionality check.** Confirm a C2 session is established within
   **60 seconds** and answers the test commands `whoami`, `ipconfig`,
   `tasklist`, `upload`.

5. **Run the gate.**

   ```bash
   python framework/validate.py check
   ```

   A failing sample is recorded with its point of failure and returned for
   revision. **Do not proceed to Stage 3 with a sample that fails either
   check** — the gate exists so that implementation defects are not scored as
   product prevention.

**Exit criteria.** Every technique in scope admitted by the gate.

---

## Stage 3 — Sample Execution

**Goal.** Observe each case against a real product under controlled,
reproducible conditions.

**Configuration.** Use the product's default protection configuration, as in the reported evaluation, with automatic sample submission disabled. Record product/version and content/update level. See [TEST_PROTOCOL.md](TEST_PROTOCOL.md) and the manuscript environment table for the tested settings.

**Per-case procedure.**

1. **Reset.** Revert *both* the target VM and the C2 server VM to their clean
   snapshots. Verify the target product is running and its protection
   components are active.
2. **Execute** the sample.
3. **Beacon window.** Observe for up to **60 seconds** for an active C2 session in the
   server console.
4. **Pre-command window.** If a session is established, observe for
   **5 minutes** without sending anything, to see whether the product
   terminates the session before any command is issued.
5. **Command window.** If the session survives, send the command set —
   `whoami`, `ipconfig`, `tasklist`, `upload` — then observe for a further
   **5 minutes**.
6. **Record evidence** from all three sources:
   - endpoint process and network state,
   - C2 server logs,
   - product alerts or local protection logs.

   Use `framework/templates/case_evidence.md` (or the CSV produced by
   `score.py template`) and cite an artifact for every field.
7. **Repeat.** Re-run the case until **five consecutive executions yield the
   same outcome**; record that outcome as final. In the paper no case needed
   more than eight runs.
8. **Power down** both VMs before the next case; retain no endpoint or C2
   runtime state.

**Controls.** C2 traffic stays on RFC 1918 addresses inside the isolated
virtual network, with no public listener or domain. Automatic sample
submission is disabled for every product.

**Exit criteria.** For new evaluations, record the final outcome using the evidence sources above and retain the underlying records internally. Public release of raw screenshots or full logs is not required by this runbook. The authors' published results use one final label per case; original evidence remains internal.

---

## Stage 4 — Effectiveness Evaluation

**Goal.** Turn evidence into labels, labels into metrics.

1. **Score.**

   ```bash
   python framework/score.py run --in results/evidence.local.csv --out results/outcomes_scored.local.csv
   ```

   `score.py` applies the paper's decision procedure:

   | Evidence | Level |
   | :--- | :--- |
   | no process created | **L1** Pre-execution Prevention |
   | process ran, terminated, no beacon | **L2** Pre-C2 Prevention |
   | beacon up, terminated before any command | **L3** Pre-command Prevention |
   | commands sent but incomplete, or session ended | **L4** Command-stage Prevention |
   | all commands completed, session alive | **L5** Operational Success |

   Anything else is **refused** and returned for review. In particular, "no
   beacon and no product termination" indicates a sample defect rather than
   prevention — it should have been caught in Stage 2.

2. **Measure.**

   ```bash
   python framework/metrics.py --outcomes results/outcomes_scored.local.csv --outdir results/metrics/local
   ```

   Produces `results/metrics/local/`: BDD per technique, per Layer 1 stage and per
   Layer 2 strategy; PSD per product; L5 by payload family.

3. **Plot.**

   ```bash
   python framework/figures.py --metrics results/metrics/local --outdir results/figures/generated/local
   ```

**Exit criteria.** An evaluator-named scored outcome file with no ambiguous
rows, and a metrics set ready for reporting.

---

## Sanity checks before you report anything

```bash
python framework/validate.py check            # all samples admitted
python framework/tests/test_metrics.py        # framework self-checks
```

If you compare against the paper's numbers, remember that the paper's results
come from the paper's payloads and product versions. Your own run reproduces
the **methodology**; matching numbers are not expected, and the paper says so
in Section V-A.
