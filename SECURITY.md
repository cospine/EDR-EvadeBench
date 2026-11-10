# Security and Responsible Use

## Intended use

`EDR-EvadeBench` is published **strictly for academic, defensive, and
product-hardening research**. The techniques it contains disable or evade
endpoint-security controls; several load kernel drivers, terminate security
processes, corrupt security-product files, or modify system-wide networking
configuration.

**Every sample must be exercised only inside an isolated virtual machine
that you own and control, with no route to production systems, corporate
networks, or hosts you do not own.** See the ethical-considerations section
of the companion paper.

## What this repository deliberately omits

So that the material supports evaluation without functioning as a turnkey
weapon, this repository does **not** include:

- working payloads, AES keys, or raw shellcode;
- active C2 infrastructure, infrastructure identifiers, or credentials;
- vendor-specific configuration or licence material;
- turnkey deployment instructions aimed at production endpoints.

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the full statement.

## No warranty

The material is provided "as is", without warranty of any kind. Some
techniques can render a system unbootable or destroy security-product
installations. Always snapshot before use and verify recovery. See
[LICENSE](LICENSE).

## Reporting a security issue in this repository

If you find a problem that affects users of this artifact — for example a
sample that results in unintended system damage, an unsafe default in one of
the scripts, or an accidentally committed credential — please report it
privately rather than opening a public issue:

[xiansongyu02@hust.edu.cn](mailto:xiansongyu02@hust.edu.cn).

Please include the technique ID, the affected file, and a description of the
impact.

## Coordinated disclosure of product findings

Per the companion paper, product-specific weaknesses identified by this
framework were reported to the affected vendors before publication. If you
use this framework and identify a new product weakness, follow coordinated
disclosure: report to the vendor first, and allow a reasonable remediation
window before publishing.
