# Contributing

This repository accompanies a published benchmark. The 22 technique
implementations define a fixed, versioned sample set: extension is welcome,
but it must not silently change what the released samples do.

## Reporting a problem

Please open an issue if you cannot follow a README to a working build or
execution. Include:

- the technique ID (for example `T16`);
- your OS version and build;
- your compiler/toolchain and version;
- the exact command you ran;
- the full error output.

If the problem is a security issue rather than a reproducibility one, follow
[SECURITY.md](SECURITY.md) instead of opening a public issue.

## Adding a technique

1. Place it under a new `T<n>_<Name>/` directory with its own `README.md`.
2. State its **DET classification** (Layer 1 stage and Layer 2 strategy) and
   its **required privilege**, matching Table 7 of the paper.
3. State the **success criterion** explicitly, so a reader can verify the
   evasion logic reached its post-condition.
4. Ship **placeholder** payload buffers only; do not commit payloads, keys,
   or C2 configuration.
5. If you vendor or adapt upstream code, add a row to
   [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) with its licence.
6. If you add a binary, record its size, SHA-256 and provenance in
   [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md).

## Changing an existing technique

Changes to evasion mechanism must be recorded in [CHANGELOG.md](CHANGELOG.md)
with the technique ID and a description of the behavioural difference,
because the released source is the artifact referenced by the paper.

Portability fixes that do not change behaviour (casting, error handling,
build configuration) are welcome and should be noted in the changelog.

## Style

Match the surrounding code: the samples are research proofs of concept, not
production utilities. Prefer minimal, readable implementations of one
evasion mechanism over general-purpose tooling.
