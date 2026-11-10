# Bundled Binary Provenance

This repository ships a small number of binary files. This document records
what each one is, its hash, and its provenance, so that a reader can tell an
upstream tool from a placeholder and from an opaque component.

Hashes are SHA-256 of the files in this release.

## 1. Auxiliary upstream tools (unmodified third-party binaries)

### `T17_Code Packing/upx.exe`

| Field | Value |
| :--- | :--- |
| Size | 599,040 bytes |
| SHA-256 | `3638bfe45ee552b57dc8c5af39c5e0f317ff83748dbf6326a0cdcccb2fd52da4` |
| Identified as | UPX executable packer, amd64 build (embedded manifest: `name="UPX" type="win32"`, description "UPX executable packer") |
| Upstream | https://github.com/upx/upx/tree/v5.0.2 |
| Version | 5.0.2 |
| License | GPL-2.0-or-later (UPX); the bundled copy is unmodified |
| Role | Generic packer used by technique T17. Carries no payload. |

### `T20_PE Resource Masquerading/calc.res`

| Field | Value |
| :--- | :--- |
| Size | 17,980 bytes |
| SHA-256 | `f8ecb0997f8c51001e372410b3c841f981bd58479461655e8ef3f6d2eb48933a` |
| Identified as | A Windows `RES` resource blob (32-byte null header followed by resource directory data) |
| Role | Example resource input for technique T20. Carries no executable code. |

## 2. Kernel driver artifacts (opaque; source not included)

These two files are the reason the repository's "no binaries" statement is
worded as "no binaries that carry payload characteristics" rather than "no
binaries". Their behaviour cannot be audited from this repository.

### `T6_Kernel Callback Removal/echo_driver.sys`

| Field | Value |
| :--- | :--- |
| Size | 23,560 bytes |
| SHA-256 | `ea3c5569405ed02ec24298534a983bcb5de113c18bc3fd01a4dd0b5839cd17b9` |
| File type | PE kernel driver (KMDF — embedded WDF/KMDF import and error strings) |
| Identified as | The "Echo" driver, built from `D:\WACATACC\Projects\Programs\Echo\x64\Release\echo-driver.pdb` (PDB path embedded in the image) |
| Upstream | [RealBlindingEDR](https://github.com/myzxcg/RealBlindingEDR), cited in the manuscript |
| Source available? | **No.** No driver source or driver build project is included. |
| Role | Provides the kernel-memory read/write primitives that the user-mode controller (`RealBlindingEDR.cpp`) drives via `DeviceIoControl`. The callback-removal logic itself is not source-auditable from this repository. |

### `T8_EDR Process Termination/kEvP64.bin`

| Field | Value |
| :--- | :--- |
| Size | 177,816 bytes |
| SHA-256 | `1aaa9aef39cb3c0a854ecb4ca7d3b213458f302025e0ec5bfbdef973cca9111c` |
| File type | PE kernel driver |
| Identified as | PowerTool 64-bit kernel driver (embedded log prefix `[kEvP64]`, PDB path `d:\dev\dev\pt64\kevp64\`; version-specific offsets for Windows 7 / 8 / 8.1 / 10 are present in the image) |
| Upstream | [Killers](https://github.com/xalicex/Killers), cited in the manuscript |
| Source available? | **No.** |
| Role | Vulnerable signed driver abused by technique T8 to terminate protected EDR processes. |

## 3. Placeholder payload files (all-zero; contain no code)

The following files are **entirely zero-filled**. They are compile-time /
link-time placeholders of the correct size, not functional shellcode.

| File | Size | SHA-256 | Notes |
| :--- | ---: | :--- | :--- |
| `T12_COM-based Process Injection/com_inject/Shellcode/notepad.bin` | 272 | `e4d879a3407de578f579dfab4366fcea75a6649c683d9efe4f056f6505437574` | Regenerate by compiling and running `Shellcode/winexec.cpp`, which writes a benign `WinExec("notepad", SW_SHOW)` stub as `notepad.bin`. |
| `T13_Fiber-based Process Injection/ImmoralFiber/PhantomThreadPayload/c-shellcode-msgbox.bin` | 2,560 | `8ce8ba8e726ee8925e6560d86ac35be1097691d1cfac888e6bd20e804ea9eb15` | Referenced by `PoisonFiber.rc` as resource `IDR_SHELLCODE_BIN1`. |
| `T13_Fiber-based Process Injection/ImmoralFiber/PoisonFiber/c-shellcode-msgbox.bin` | 2,560 | `8ce8ba8e726ee8925e6560d86ac35be1097691d1cfac888e6bd20e804ea9eb15` | Identical file; same role. |
| `T13_Fiber-based Process Injection/ImmoralFiber/PhantomThreadPayload/payload_x64_3.bin` | 894 | `e9bde8946ac2f5377f07498a3afe07d98e91f986a3acf37a9d246b4a10dd1694` | Referenced by `PhantomThreadPayload.rc` as resource `IDR_SHELLCODE_BIN1`. |

All four are all-zero. They exist so that the resource-compilation steps in
the shipped Visual Studio projects succeed out of the box; they execute
nothing. Replace them with your own payload resource before functional
testing.

## 4. Not present

No built sample executables are committed. The `.exe` names that appear in
the technique READMEs (for example `PowerTool_killer.exe`,
`EDRSilencer.exe`, `RealBlindingEDR.exe`, `com_inject.exe`) are **build
outputs**: compile the corresponding source in the same folder to produce
them. See [BUILD.md](BUILD.md).
