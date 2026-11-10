# Build Guide

This guide describes the source layout, toolchains and build commands for the EDR-EvadeBench release. All paths are relative to the repository root unless otherwise stated. Technique-specific documentation is linked in the project table below.

## Toolchains

| Component | Toolchain |
| --- | --- |
| Direct C/C++ compilation | MinGW-w64 GCC 14.2.0, target `x86_64-w64-mingw32` |
| Visual Studio solutions | Visual Studio 2022 C++ toolset `v143` and Windows SDK |
| Assembly inputs | Microsoft MASM for projects that include assembly files |
| Resource files | Windows SDK resource compiler |
| Python utilities | Python 3 |
| Result analysis | Python 3 standard library |

The Visual Studio projects declare Debug/Release and Win32/x64 configurations. Project-specific settings are stored in their `.vcxproj` files. Quote paths that contain spaces.

## Project layout

Paths in the source/project column are relative to the corresponding technique directory.

| ID | Source/project entry |
| :--: | --- |
| [T1](T1_Direct%20Syscall%20Invocation/README.md) | `test.c`, `syswhispers.py` |
| [T2](T2_ETW_AMSI%20Patching/README.md) | `amsi-etw-patch/amsi-etw-patch.cpp`, `lazy_importer.hpp` |
| [T3](T3_DLL%20Signature%20Restriction%20Bypass/README.md) | `PreventDll/PreventDll.cpp`, `lazy_importer.hpp` |
| [T4](T4_Hook%20Overwriting/README.md) | `Hook_Overwriting.cpp` |
| [T5](T5_NTDLL%20Hook%20Removal/README.md) | `unhook.cpp`, `lazy_importer.hpp` |
| [T6](T6_Kernel%20Callback%20Removal/README.md) | `RealBlindingEDR/RealBlindingEDR.sln`; one controller project; `echo_driver.sys` |
| [T7](T7_Symlink-based%20EDR%20Corruption/README.md) | `T7-Symlink-Corruption.bat` |
| [T8](T8_EDR%20Process%20Termination/README.md) | `PowerTool_killer.c`, `kEvP64.bin` |
| [T9](T9_EDRSilencer/README.md) | `EDRSilencer.c`, `utils.c`, `utils.h` |
| [T10](T10_COM%20Hijacking/README.md) | `COMProxy-master/COMProxyTesting.sln`; client and DLL projects; `hijack.template.reg` |
| [T11](T11_DLL%20Hijacking/README.md) | `AheadLibEx_libcurl/libcurl.sln`; `libcurl.cpp`, `libcurl_jump.asm` |
| [T12](T12_COM-based%20Process%20Injection/README.md) | `com_inject/com_inject.sln`; `com_inject`, `Shellcode`, `TestDll` projects |
| [T13](T13_Fiber-based%20Process%20Injection/README.md) | `ImmoralFiber/ImmoralFiber.sln`; four projects |
| [T14](T14_Thread%20Pool-based%20Injection/README.md) | `PoolParty.sln`; eight C++ sources and local headers; `packages.config` |
| [T15](T15_Process%20Hollowing/README.md) | `Source/Process Hollowing.sln`; `Process_Hollowing.cpp` |
| [T16](T16_Module%20Stomping/README.md) | `Module Stomping.sln`; C++ source and `lazy_importer.hpp` |
| [T17](T17_Code%20Packing/README.md) | `upx.exe` and README |
| [T18](T18_Code%20Virtualization/README.md) | README only |
| [T19](T19_Compiler-level%20Obfuscation/README.md) | `exeshellcode.cpp` |
| [T20](T20_PE%20Resource%20Masquerading/README.md) | `calc.res`, README; external Resource Hacker |
| [T21](T21_API-level%20Behavioral%20Obfuscation/README.md) | `main.c`, `easy.c` |
| [T22](T22_COM-based%20Process%20Creation/README.md) | `IHxHelpPaneServer.cpp` |

## Project dependencies

| ID | Dependencies and supplied components |
| :--: | --- |
| T1 | Python 3, SysWhispers generator data/templates, generated C/header/assembly files, Windows C/C++ toolchain and CNG (`bcrypt`) |
| T2 | Windows C++ headers, CNG and the supplied `lazy_importer.hpp` |
| T3 | Windows C++ headers, CNG and the supplied `lazy_importer.hpp` |
| T4 | Windows C++ headers and CNG |
| T5 | Windows C++ headers, CNG, process-status interfaces and the supplied `lazy_importer.hpp` |
| T6 | Visual Studio C++ project, Windows SDK and the supplied `echo_driver.sys` auxiliary driver |
| T7 | Windows command interpreter; batch script |
| T8 | Windows C toolchain and the supplied `kEvP64.bin` auxiliary driver |
| T9 | Windows Filtering Platform interfaces, `EDRSilencer.c`, `utils.c` and `utils.h` |
| T10 | Visual Studio C++ solution containing the client and DLL projects; supplied `Source.def` and registry template |
| T11 | Visual Studio C++ project, MASM input, CNG, Shlwapi and supplied helper header |
| T12 | MSVC solution containing `com_inject`, `Shellcode` and `TestDll`; Windows COM/RPC and related SDK libraries |
| T13 | MSVC solution containing `BasicFiber`, `PhantomThread`, `PoisonFiber` and `PhantomThreadPayload`; project-local headers and resource inputs |
| T14 | Visual Studio C++ project and Boost NuGet packages declared in `PoolParty/packages.config`, version `1.82.0` |
| T15 | Visual Studio C++ project or direct C++ compilation; the VS target name is `runpe` |
| T16 | Visual Studio C++ project or direct C++ compilation, CNG and supplied helper header |
| T17 | Supplied UPX auxiliary tool; file version `5.0.2` |
| T18 | VMProtect; see the technique README |
| T19 | C++ compiler; LLVM `17.0.6` and OLLVM 17 toolchain for the compiler-transformed variant described in the technique README |
| T20 | External Resource Hacker and supplied `calc.res`; reference tool FileVersion `5.1.7.343` |
| T21 | libcurl source tree, public/internal headers and a compatible Windows C/C++ toolchain |
| T22 | Windows C++ COM interfaces and libraries |

External toolchains and libraries are separate prerequisites. T14 package identifiers and versions are specified in `packages.config`. T1 generator data/templates and T21 library files belong to their respective upstream source distributions.

T6/T8 provide auxiliary driver binaries as dependencies of their user-mode components. T17 provides the UPX auxiliary tool; T20 uses an externally obtained resource editor. T18 documents a tool-based transformation. File hashes and component provenance are listed in [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md).

## Payload and resource inputs

Public payload buffers and designated binary resource inputs are placeholders. Payload preparation is described in manuscript Appendix B; the evaluation procedure is documented in [framework/TEST_PROTOCOL.md](framework/TEST_PROTOCOL.md). Actual payload binaries and keys are handled separately from the public source package.

Keep each project's source, helper headers and resource files in their supplied relative layout. For multi-project solutions, consult the corresponding technique README for the roles of the individual components.

## Direct-compilation examples

The following existing examples use MinGW-w64 and repository-root paths. Solution-based projects and external tool workflows are documented in their technique directories.

### T2 — ETW & AMSI Patching

```bash
x86_64-w64-mingw32-gcc "T2_ETW_AMSI Patching/amsi-etw-patch/amsi-etw-patch.cpp" \
  -lbcrypt -lstdc++ -I"T2_ETW_AMSI Patching/amsi-etw-patch" \
  -o amsi-etw-patch.exe
```

### T3 — DLL Signature Restriction

```bash
x86_64-w64-mingw32-gcc "T3_DLL Signature Restriction Bypass/PreventDll/PreventDll.cpp" \
  -lbcrypt -lstdc++ -I"T3_DLL Signature Restriction Bypass/PreventDll" \
  -o PreventDll.exe
```

### T4 — Hook Overwriting

```bash
x86_64-w64-mingw32-gcc "T4_Hook Overwriting/Hook_Overwriting.cpp" \
  -lbcrypt -lstdc++ -o Hook_Overwriting.exe
```

### T5 — NTDLL Hook Removal

```bash
x86_64-w64-mingw32-gcc "T5_NTDLL Hook Removal/unhook.cpp" \
  -lbcrypt -lstdc++ -I"T5_NTDLL Hook Removal" -o unhook.exe
```

### T8 — EDR Process Termination

```bash
x86_64-w64-mingw32-gcc -o PowerTool_killer.exe "T8_EDR Process Termination/PowerTool_killer.c"
```

### T9 — EDRSilencer

```bash
x86_64-w64-mingw32-gcc "T9_EDRSilencer/EDRSilencer.c" "T9_EDRSilencer/utils.c" \
  -o EDRSilencer.exe -lfwpuclnt
```

### T12 — Test DLL (benign demonstration)

```bash
x86_64-w64-mingw32-gcc -shared "T12_COM-based Process Injection/com_inject/TestDll/dllmain.cpp" \
  -luser32 -o TestDll.dll
```

### T15 — Process Hollowing

```bash
x86_64-w64-mingw32-gcc "T15_Process Hollowing/Source/Process Hollowing/Process_Hollowing.cpp" \
  -lstdc++ -o runpe.exe
```

### T16 — Module Stomping

```bash
x86_64-w64-mingw32-gcc "T16_Module Stomping/Module Stomping/Module Stomping.cpp" \
  -lbcrypt -lstdc++ -o "ModuleStomping.exe"
```

### T19 — Compiler-level Obfuscation (payload stub)

```bash
x86_64-w64-mingw32-gcc "T19_Compiler-level Obfuscation/exeshellcode.cpp" \
  -lbcrypt -lstdc++ -o exeshellcode.exe
```

### T22 — COM-based Process Creation

```bash
x86_64-w64-mingw32-gcc "T22_COM-based Process Creation/IHxHelpPaneServer.cpp" \
  -lole32 -loleaut32 -luuid -lstdc++ -municode -o IHxHelpPaneServer.exe
```

## Result-data checks

These checks validate the released labels and analysis framework:

```bash
python framework/tools/export_results.py --check
python framework/tools/build_results_from_readmes.py --check
python -m unittest discover -s framework/tests
```

The published results and data dictionary are in [results/](results/README.md). See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the artifact scope.

## Build support

For a build-related issue, provide the technique ID, compiler/version, selected configuration and error output as described in [CONTRIBUTING.md](CONTRIBUTING.md).
