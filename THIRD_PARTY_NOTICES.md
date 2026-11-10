# Third-Party Notices

EDR-EvadeBench includes implementations adapted from the sources cited in the companion paper, together with third-party helper headers and auxiliary tools. Copyright and license rights in those materials remain with their respective owners. The repository's [LICENSE](LICENSE) applies to the authors' own contributions and does not replace third-party terms or restrict rights already granted by an upstream license.

The source mapping below follows the paper's bibliography. BibTeX citation keys are used instead of numeric reference labels because reference numbers change when the manuscript is revised. License information was checked against upstream license texts, published terms and retained source headers on **November 10, 2026**.

An attribution identifies a source; it does not itself grant redistribution rights. Where the cited source provides no explicit license, or the original license cannot be verified from that source, this is stated directly. Such entries are not represented as MIT, Apache, public-domain material or newly licensed benchmark code.

## Sources cited for T1-T22

| ID | Cited source / author | Paper citation key | License or published terms | Material in this repository |
| :--: | --- | --- | --- | --- |
| T1 | [SysWhispers3 - klezVirus](https://github.com/klezVirus/SysWhispers3) | `syswhispers3` | **Apache-2.0**; [license copy](LICENSES/SysWhispers3-Apache-2.0.txt) | Adapted test source and generator script |
| T2 | [AMSI-ETW-Patch - Mr-Un1k0d3r](https://github.com/Mr-Un1k0d3r/AMSI-ETW-Patch) | `amsi-etw-patch` | No explicit license identified in the cited project; upstream copyright retained | Adapted C++ implementation; helper header licensed separately below |
| T3 | [Preventing 3rd Party DLLs from Injecting into Your Processes - ired.team / Red Team Notes](https://www.ired.team/offensive-security/defense-evasion/preventing-3rd-party-dlls-from-injecting-into-your-processes) | `ired_team_2020` | Cited publication; no separate open-source license grant verified for its code examples | Adapted implementation; helper header licensed separately below |
| T4 | [Silencing Cylance: A Case Study in Modern EDRs - MDSec](https://www.mdsec.co.uk/2019/03/silencing-cylance-a-case-study-in-modern-edrs/) | `mdsec2019_silencing_cylance` | Cited publication; no separate open-source license grant verified | Adapted implementation |
| T5 | [Ntdll-Unhook - EvilBytecode](https://github.com/EvilBytecode/Ntdll-Unhook) | `ntdll-unhook` | License not verified from the accessible original source; upstream copyright retained | Adapted implementation; helper header licensed separately below |
| T6 | [RealBlindingEDR - myzxcg](https://github.com/myzxcg/RealBlindingEDR) | `realblindingedr` | **MIT** for the upstream project code; [license copy](LICENSES/RealBlindingEDR-MIT.txt). See the separate driver notice below | Adapted controller project and auxiliary driver binary |
| T7 | [BYOVD to the Next Level: Blind EDR with Windows Symbolic Link - Zero Salarium](https://www.zerosalarium.com/2025/01/byovd%20next%20level%20blind%20EDR%20windows%20symbolic%20link.html) | `zerosalarium-byovd-2025` | Cited publication; no separate open-source license grant identified | Benchmark batch-script implementation based on the cited material |
| T8 | [Killers - xalicex](https://github.com/xalicex/Killers) | `killers_xalicex` | No explicit license identified in the cited project; the auxiliary driver has separate publisher rights | Adapted C client and auxiliary driver binary |
| T9 | [EDRSilencer - Chris Au / netero1010](https://github.com/netero1010/EDRSilencer) | `EDRSilencer` | **MIT**; [license copy](LICENSES/EDRSilencer-MIT.txt) | Adapted C implementation and local utilities |
| T10 | [COMProxy - Leo Loobeek](https://github.com/leoloobeek/COMProxy) | `comproxy` | **BSD-3-Clause**; [license copy](LICENSES/COMProxy-BSD-3-Clause.txt) | Adapted client/server solution and related files |
| T11 | [Exploiting DLL Hijacking by DLL Proxying Super Easily - tothi](https://github.com/tothi/dll-hijack-by-proxying) | `tothi_dll_hijack` | No explicit license identified in the cited project; generator attribution and helper-header terms are recorded separately below | Adapted proxy project; AheadLibEx attribution retained in generated source/assembly |
| T12 | [com_inject - MDSec ActiveBreach](https://github.com/mdsecactivebreach/com_inject) | `mdsecactivebreach_com_inject` | License not verified from the accessible original source; upstream copyright retained | Adapted solution with injector and demonstration components |
| T13 | [ImmoralFiber - Daniel Jary / JanielDary](https://github.com/JanielDary/ImmoralFiber) | `janiel_dary_immoralfiber` | **MIT**; [license copy](LICENSES/ImmoralFiber-MIT.txt). Helper headers retain their own licenses | Adapted multi-project solution, retained upstream documentation and helper headers |
| T14 | [PoolParty - SafeBreach Labs](https://github.com/SafeBreach-Labs/PoolParty) | `safebreach_poolparty_2023` | **BSD-3-Clause**; [license copy](LICENSES/PoolParty-BSD-3-Clause.txt) | Adapted C++ project; Boost is a separate dependency |
| T15 | [Process-Hollowing - m0n0ph1](https://github.com/m0n0ph1/Process-Hollowing) | `m0n0ph1_process_hollowing_2023` | License not verified from the accessible original source; upstream copyright retained | Adapted C++ source/project |
| T16 | [ModuleStomping - WithSecure Labs](https://github.com/WithSecureLabs/ModuleStomping) | `withsecure_modulestomping_2019` | No explicit license identified in the cited project; helper header licensed separately below | Adapted C++ project |
| T17 | [UPX - the UPX authors](https://github.com/upx/upx) | `upx_upx_2025` | **GPL-2.0-or-later with the UPX special exception**; [UPX terms](LICENSES/UPX-5.0.2-LICENSE.txt) and [GPL text](LICENSES/UPX-5.0.2-COPYING.txt) | Unmodified auxiliary executable, file version 5.0.2 |
| T18 | [VMProtect 3: Virtualization-Based Software Obfuscation Pt. 2 - Mitchell Zakocs](https://www.mitchellzakocs.com/blog/vmprotect3) | `zakocs_vmprotect3_2021` | Article copyright remains with its author; VMProtect is a separate proprietary product governed by its publisher's terms | Documentation referencing the article and external tool |
| T19 | [ollvm17 - DreamSoule](https://github.com/DreamSoule/ollvm17) | `dreamsoule_ollvm17_2024` | LLVM 17 base: **Apache-2.0 WITH LLVM-exception**; a separate license grant for the cited OLLVM patch material was not verified | Benchmark C++ source and references to an external compiler; no compiler distribution |
| T20 | [resource_hacker - Seabreg](https://github.com/Seabreg/resource_hacker); tool author **Angus Johnson** | `seabreg_resource_hacker_2019` | Resource Hacker binary: **author's freeware terms**, not an assumed GPL grant from a mirror. See the binary notice below | Example resource file and preparation instructions; Resource Hacker is obtained separately from its publisher |
| T21 | [curl / libcurl - Daniel Stenberg and contributors](https://github.com/curl/curl) | `curl_curl_2025` | **curl** license; [license copy](LICENSES/curl-COPYING.txt) | Adapted `easy.c` and benchmark `main.c`; the `easy.c` copyright/SPDX header is retained |
| T22 | [IHxHelpPaneServer - mabangde](https://github.com/mabangde/IHxHelpPaneServer) | `mabangde_ihxhelppane_2023` | No explicit license identified in the cited project; upstream copyright retained | Adapted C++ implementation |

The repository incorporates benchmark-specific integration and public-release preparation, including AES-related integration, payload placeholders and project/documentation changes as applicable. These adaptations do not transfer ownership of upstream material or remove its original terms. File-level copyright and license notices continue to apply.

## Helper headers and generated-file attribution

### lazy_importer.hpp

- **Author:** Justas Masiulis.
- **Copyright retained in the supplied headers:** Copyright 2018-2022 Justas Masiulis.
- **Source:** [JustasMasiulis/lazy_importer](https://github.com/JustasMasiulis/lazy_importer).
- **License:** Apache-2.0; [upstream license](https://github.com/JustasMasiulis/lazy_importer/blob/master/LICENSE), [included copy](LICENSES/lazy_importer-Apache-2.0.txt).
- **Locations:** T2 `amsi-etw-patch/`, T3 `PreventDll/`, T5 root, T11 `AheadLibEx_libcurl/`, T13 `ImmoralFiber/PhantomThreadPayload/`, and T16 `Module Stomping/`.

Each supplied header retains its original copyright and Apache license notice. The upstream author is Justas Masiulis; the earlier attribution to a different account name is superseded by this notice.

### oxorany.h

- **Source:** [llxiaoyuan/oxorany](https://github.com/llxiaoyuan/oxorany).
- **Attribution retained in the file:** `@author llxiaoyuan`; Copyright (c) 2021 Chase.
- **License:** MIT; [upstream license](https://github.com/llxiaoyuan/oxorany/blob/main/LICENSE), [included copy](LICENSES/oxorany-MIT.txt).
- **Location:** `T13_Fiber-based Process Injection/ImmoralFiber/PhantomThreadPayload/oxorany.h`.

The MIT notice is retained in the header. This file is attributed to oxorany, rather than to UPX.

### AheadLibEx

T11's `libcurl.cpp` and `libcurl_jump.asm` retain generator attribution to **i1tao / AheadLibEx**, including the [project URL](https://github.com/i1tao/AheadLibEx) and author blog reference. This attribution is additional to the paper's tothi reference. A generator's current license is not assumed to establish the license of an older generated template or of third-party DLL material. No separate license grant for the retained generated-template version is asserted here.

Technical-reference comments in the T13 source also credit their original sources, including Geoff Chappell, Wine and Process Hacker documentation. Those references and any applicable file-level notices are retained; the ImmoralFiber project-level license does not replace separate third-party rights.

## Auxiliary binary and resource notices

### UPX

The bundled `T17_Code Packing/upx.exe` reports file version **5.0.2**. UPX is credited to Markus F. X. J. Oberhumer, Laszlo Molnar, John F. Reiser and other contributors, with individual notices governed by the upstream distribution.

Its terms are [GPL-2.0-or-later plus the UPX special exception](https://github.com/upx/upx/blob/v5.0.2/LICENSE). The exception concerns compressed executables; it does not remove the license obligations for distributing UPX itself. Copies of the upstream `LICENSE` and `COPYING` are included in `LICENSES/`. The corresponding upstream release source is available at [UPX v5.0.2](https://github.com/upx/upx/tree/v5.0.2). The repository's non-commercial terms do not restrict the rights granted by the UPX license.

### Resource Hacker

The paper cites the [Seabreg resource_hacker mirror](https://github.com/Seabreg/resource_hacker). The Resource Hacker program is authored by **Angus Johnson**, whose [official product page and license terms](https://www.angusj.com/resourcehacker/) identify it as freeware. The reference executable reports **FileVersion 5.1.7.343** and **ProductVersion 5.0.0.0**. Resource Hacker is not redistributed in this release; obtain it from the publisher.

The mirror contains a GPL v3 license text, but that is not treated as evidence that Angus Johnson licensed the original executable under GPL. The author's published terms require prior written approval for redistribution via websites or other media. The executable is excluded from this release; these terms continue to govern copies obtained separately.

The example `calc.res` is a resource artifact. Rights in embedded icons, strings, product metadata or other resource content remain with the original content owners; a resource editor's license does not grant rights to that content.

### Auxiliary drivers

- `T6_Kernel Callback Removal/echo_driver.sys` is attributed through the paper's [RealBlindingEDR source](https://github.com/myzxcg/RealBlindingEDR).
- `T8_EDR Process Termination/kEvP64.bin` is attributed through the paper's [Killers source](https://github.com/xalicex/Killers), which identifies its PowerTool component.

These are third-party driver binaries. Rights remain with the original driver publishers. A license on a controller or a repository citing the driver is not asserted as an independent license grant for third-party driver binaries. This notice does not claim a verified standalone redistribution license for either driver. File identities and hashes are recorded in [BINARY_PROVENANCE.md](BINARY_PROVENANCE.md).

## External dependencies and referenced frameworks

| Component | Author/source | Applicable terms | Relationship to this package |
| --- | --- | --- | --- |
| Boost | [Boost contributors](https://www.boost.org/) | [Boost Software License 1.0 (`BSL-1.0`)](https://www.boost.org/LICENSE_1_0.txt) | T14 dependency declared in `packages.config`; external package |
| LLVM 17.0.6 | [LLVM Project](https://github.com/llvm/llvm-project/tree/llvmorg-17.0.6) | [Apache-2.0 WITH LLVM-exception](https://github.com/llvm/llvm-project/blob/llvmorg-17.0.6/llvm/LICENSE.TXT) | External base compiler referenced for T19; this does not establish the terms of every OLLVM addition |
| VMProtect | [VMProtect Software](https://vmpsoft.com/) | Proprietary publisher terms | External tool referenced for T18 |
| Cobalt Strike | [Fortra](https://www.cobaltstrike.com/product) | Proprietary publisher terms | Payload framework described in the paper; no framework distribution or generated payload included |
| Havoc | [HavocFramework/Havoc](https://github.com/HavocFramework/Havoc) | [GNU GPL v3](https://github.com/HavocFramework/Havoc/blob/main/LICENSE); generated artifacts retain applicable terms | External payload framework; not redistributed in this package |
| AdaptixC2 | [Adaptix-Framework/AdaptixC2](https://github.com/Adaptix-Framework/AdaptixC2) | [GNU GPL v3](https://github.com/Adaptix-Framework/AdaptixC2/blob/main/LICENSE) for the framework, subject to separate component notices | External payload framework; not redistributed in this package |

Framework citations identify sources and preparation context. They do not imply that proprietary software, generated payloads, credentials or encryption keys are distributed with this repository.

## Retention of notices

The license copies below preserve the retrieved upstream texts, including their copyright notices and disclaimers. Existing source-file notices must remain with the relevant files. For material without a verified explicit grant, attribution in this document is not a substitute for permission from the relevant rights holder. Project names and trademarks are used for attribution, without implying endorsement.

| Included license file | Upstream text |
| --- | --- |
| [LICENSES/SysWhispers3-Apache-2.0.txt](LICENSES/SysWhispers3-Apache-2.0.txt) | [Original license text](https://raw.githubusercontent.com/klezVirus/SysWhispers3/master/LICENSE) |
| [LICENSES/lazy_importer-Apache-2.0.txt](LICENSES/lazy_importer-Apache-2.0.txt) | [Original license text](https://raw.githubusercontent.com/JustasMasiulis/lazy_importer/master/LICENSE) |
| [LICENSES/RealBlindingEDR-MIT.txt](LICENSES/RealBlindingEDR-MIT.txt) | [Original license text](https://raw.githubusercontent.com/myzxcg/RealBlindingEDR/main/LICENSE) |
| [LICENSES/EDRSilencer-MIT.txt](LICENSES/EDRSilencer-MIT.txt) | [Original license text](https://raw.githubusercontent.com/netero1010/EDRSilencer/main/LICENSE) |
| [LICENSES/COMProxy-BSD-3-Clause.txt](LICENSES/COMProxy-BSD-3-Clause.txt) | [Original license text](https://raw.githubusercontent.com/leoloobeek/COMProxy/master/LICENSE) |
| [LICENSES/ImmoralFiber-MIT.txt](LICENSES/ImmoralFiber-MIT.txt) | [Original license text](https://raw.githubusercontent.com/JanielDary/ImmoralFiber/master/LICENSE) |
| [LICENSES/PoolParty-BSD-3-Clause.txt](LICENSES/PoolParty-BSD-3-Clause.txt) | [Original license text](https://raw.githubusercontent.com/SafeBreach-Labs/PoolParty/main/LICENSE) |
| [LICENSES/oxorany-MIT.txt](LICENSES/oxorany-MIT.txt) | [Original license text](https://raw.githubusercontent.com/llxiaoyuan/oxorany/main/LICENSE) |
| [LICENSES/curl-COPYING.txt](LICENSES/curl-COPYING.txt) | [Original license text](https://raw.githubusercontent.com/curl/curl/master/COPYING) |
| [LICENSES/UPX-5.0.2-LICENSE.txt](LICENSES/UPX-5.0.2-LICENSE.txt) | [Original license text](https://raw.githubusercontent.com/upx/upx/v5.0.2/LICENSE) |
| [LICENSES/UPX-5.0.2-COPYING.txt](LICENSES/UPX-5.0.2-COPYING.txt) | [Original license text](https://raw.githubusercontent.com/upx/upx/v5.0.2/COPYING) |
