# Two-Stage Validation Checklist — template

Stage 2 of the framework. Generate the machine-readable version with:

```bash
python framework/validate.py init      # writes results/validation.template.csv
```

Then copy it to `results/validation.csv`, fill it in, and run the gate:

```bash
python framework/validate.py check
```

---

## What the two checks are

**1. Evasion Logic Verification.** Confirm the sample's core evasion mechanism
reaches its predefined post-condition under the designated validation
configuration. For techniques that depend on product-specific security state,
confirm the required target state **exists before** the run and that the state
**changed after** it. The criterion for each technique is the one from Table
VII, and is pre-filled in the generated CSV.

**2. Payload Functionality Check.** Confirm the payload still works after the
bypass: the C2 beacon calls back within **60 seconds** and answers the test
commands `whoami`, `ipconfig`, `tasklist`, `upload`.

## Validation configuration

`validation_config` in the generated CSV is one of:

| Value | Meaning | Applies to |
| :--- | :--- | :--- |
| `clean-baseline` | Validated in a clean environment without active EDR enforcement | most techniques |
| `product-present` | Validated with the product installed and its target components active | T4, T6, T7, T8, T9 |

For `product-present` techniques, if an enforcement function would interrupt
the sample mid-execution, put it in audit mode or exclude it narrowly — and
record that you did, in `notes`. Table 7 of the paper and
`framework/schema/techniques.json` carry the same mapping.

## Status values

| Status | Meaning |
| :--- | :--- |
| `pass` | Criterion verified; evidence cited |
| `fail` | Criterion not met — record the point of failure in `notes` |
| `not_applicable` | Check does not apply to this technique |
| `pending` | Not yet run |

## The gate

A technique is admitted only when **every applicable row is `pass`**. A
technique with any `fail` is returned for revision, and the failure is logged
with its point of failure so that an implementation defect is not later scored
as product prevention. Techniques with any `pending` row are reported as
incomplete.

`python framework/validate.py check` exits non-zero unless every technique in
scope is admitted.

## Fields

| Column | Contents |
| :--- | :--- |
| `technique_id` | T1–T22 |
| `technique_name` | filled in |
| `stage` | `evasion_logic` or `payload_functionality` |
| `criterion` | the success criterion being checked |
| `expected_state` | what to confirm before/after the run |
| `validation_config` | `clean-baseline` or `product-present` |
| `status` | `pass` / `fail` / `not_applicable` / `pending` |
| `evidence_ref` | pointer to the artifact that shows the result |
| `reviewer` | who ran the check |
| `date` | when |
| `notes` | point of failure, or a note about a validation exclusion |

> The authors' original validation records are not published with this
> repository — see [../../REPRODUCIBILITY.md](../../REPRODUCIBILITY.md). The shipped
> checklist is a blank template for the evaluator's own run.
