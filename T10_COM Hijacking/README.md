# T10: COM Hijacking

**DET classification:** Detection → Memory Concealment

This technique exploits the Windows **Component Object Model (COM) registration** process to achieve code execution within a trusted host process. COM is fundamental to many legitimate Windows applications, and when an application attempts to instantiate a COM object, the system consults the registry to find the path to the implementing DLL.

The hijacking process involves:

1.  **Registry Modification:** Creating specific registry keys (typically under `HKEY_CURRENT_USER\Software\Classes\CLSID`) that point a known, legitimate COM Class ID (CLSID) to the path of a malicious proxy DLL (`TestCOMServer.dll`).
2.  **Execution:** When a victim application (e.g., `TestCOMClient.exe` or a system process) calls the function to instantiate the COM object, the system loads the malicious DLL instead.
3.  **Proxying:** The malicious DLL executes the embedded payload and then optionally forwards the call to the original, legitimate DLL to prevent application crashes (hence the name "COMProxy").

This method is highly effective for hiding execution because the system records the legitimate application loading a seemingly legitimate DLL (via the hijacked path).

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 22.2%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 11.1% | 55.6% | 11.1% | 0.0% | **22.2%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 33.3% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 0.0% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** COM hijacking reached operational success against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes), while Sophos, Kaspersky, Bitdefender, and Elastic Security produced no L5 outcomes — most executions were stopped at L2, consistent with registry-modification monitoring and unsigned-DLL-in-trusted-process heuristics. The result is payload-dependent (0.0% with Cobalt Strike vs. 33.3% with Havoc and AdaptixC2), showing that the hijacked execution context alone does not guarantee evasion; payload artifacts still influence the outcome.

## ⚙️ Usage (Defensive Research)

The implementation requires a client executable, a compiled proxy DLL (`TestCOMServer.dll`) containing the payload, and a `.reg` file to implement the registry changes.

### Prerequisites

* The source code for the COM client and server/proxy DLL (e.g., `TestCOMClient.exe` and `TestCOMServer.dll`) is required.
* A prepared `.reg` file to import the hijacking path into the current user's registry hive.

### Detailed Execution Steps

1.  **Prepare Payload and Compile:**
    * Integrate your own (AES-encrypted) EDR-EvadeBench payload into the `TestCOMServer.dll` source code; the shipped source contains a placeholder buffer only.
    * Compile the entire project to produce the client (`TestCOMClient.exe`) and the malicious proxy DLL (`TestCOMServer.dll`).

2.  **Apply Registry Hijacking:**
    * **WARNING:** Modifying the registry takes immediate effect.
    * A template is provided as `hijack.template.reg` in this folder. It is a **template, not a ready-to-run file**: copy it to `hijack.reg` and replace the placeholder DLL path with the full path of your compiled `TestCOMServer.dll` before importing. Its content is:

    ```reg
    Windows Registry Editor Version 5.00

    [HKEY_CURRENT_USER\Software\Classes\CLSID\{72C24DD5-D70A-438B-8A42-98424B88AFB8}]
    @="Test Hijack"

    [HKEY_CURRENT_USER\Software\Classes\CLSID\{72C24DD5-D70A-438B-8A42-98424B88AFB8}\InprocServer32]
    @="C:\\Path\\To\\Your\\Payload.dll"
    "ThreadingModel"="Apartment"
    ```
    * Import the edited copy:
        ```bash
        reg import hijack.reg
        ```
    * **The shipped `hijack.template.reg` must not be imported as-is** — its DLL path is a placeholder, so the hijack would point nowhere.

3.  **Execute the Client:**
    * Run the client executable. This will attempt to instantiate the COM object, but due to the registry changes, it will load and execute the payload from `TestCOMServer.dll` first.
        ```bash
        TestCOMClient.exe
        ```

4.  **Cleanup (Crucial):**
    * After testing, you **must** remove the hijacking entry to restore system stability. Delete the entire CLSID key from `HKEY_CURRENT_USER\Software\Classes\CLSID`:
        ```bash
        reg delete HKEY_CURRENT_USER\Software\Classes\CLSID\{72C24DD5-D70A-438B-8A42-98424B88AFB8} /f
        ```

> **Warning:** Registry tampering is highly visible to EDRs. Execute this PoC **only** in isolated VM environments with careful cleanup to prevent persistence.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Client source | `COMProxy-master/TestCOMClient/TestCOMClient.cpp` |
| Proxy DLL source | `COMProxy-master/TestCOMServer/dllmain.cpp` |
| Build projects | `COMProxy-master/COMProxyTesting.sln` (+ two `.vcxproj`, toolset `v143`) |
| Registry template | `hijack.template.reg` — **template; it must not be imported as-is** |
| Prebuilt executables | Not distributed — `TestCOMClient.exe` / `TestCOMServer.dll` are **build outputs** ([BUILD.md](../BUILD.md)) |

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a malicious COM object is registered under a
  hijacked CLSID, and the payload executes when the target application
  instantiates that COM object.
- **Payload-functionality check:** C2 beacon observed within 60 seconds, and
  the beacon answers test commands.

## 📝 Using the Registry Template

`hijack.template.reg` is a template, not a ready-to-run file. Before
importing it you must:

1. replace `C:\\Path\\To\\Your\\Payload.dll` with the full path of your
   compiled proxy DLL (`TestCOMServer.dll`);
2. confirm the CLSID is the one you intend to hijack.

> The shipped `TestCOMServer` `DllMain` only displays a MessageBox. It is a
> benign demonstration of the loading path; integrate your payload (and the
> AES key) before any functional test.

## 🧹 Cleanup / Recovery — required

Remove the hijack immediately after testing:

```bat
reg delete "HKEY_CURRENT_USER\Software\Classes\CLSID\{72C24DD5-D70A-438B-8A42-98424B88AFB8}" /f
```

A leftover `HKCU\Software\Classes\CLSID` entry is per-user persistence and
will keep loading your DLL.

## ⚠️ Known Limitations

- Registry tampering under `HKCU\Software\Classes\CLSID` is highly visible to
  EDRs, consistent with the reported outcomes.
- The proxy DLL must still forward calls to the genuine COM server, or the
  host application will misbehave.
