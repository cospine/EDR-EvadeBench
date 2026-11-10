# T21: API-level Behavioral Obfuscation

**DET classification:** Detection → Logic Bypass

This technique implements **API-level behavioral obfuscation** by embedding malicious execution flow within a massive, trusted, and widely-used open-source library (in this PoC: **libcurl**), combined with misleading API call sequences that distort behavior-based classifiers.

The core evasion logic relies on the "Needle in a Haystack" principle:
1.  **Dilution of Malicious Artifacts:** By inserting a small shellcode loader into a large codebase (tens of thousands of lines of code), the malicious signature is diluted, making static analysis more difficult.
2.  **Exploiting Trusted Execution Paths:** The malicious logic is placed inside a frequently used, legitimate API function (e.g., `curl_easy_init`). When the EDR analyzes the process, it sees a legitimate library call sequence.
3.  **Behavioral Distortion:** The execution of the payload is preceded and followed by complex, legitimate initialization routines, distorting the behavioral sequence that EDR heuristics typically monitor.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 27.8%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 0.0% | 61.1% | 11.1% | 0.0% | **27.8%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 50.0% | 33.3% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 33.3% | 0.0% | 0.0% | 66.7% | 66.7% |

**Interpretation.** The paper highlights this technique as one of the most strongly payload-dependent in the benchmark: 0.0% L5 with Cobalt Strike versus 50.0% with Havoc and 33.3% with AdaptixC2, while the core evasion mechanism was held constant. Operational success was reached against Microsoft Defender Antivirus and Huorong (each L5 in 4 of 6 outcomes) and, partially, Kaspersky (2 of 6); Sophos, Bitdefender, and Elastic Security produced no L5 outcomes. No execution was prevented at L1 across all 36 outcomes — consistent with a technique whose entire purpose is to blend into a benign-looking API call sequence — but the majority of outcomes (61.1%) were still stopped at L2, before C2 establishment.

## ⚙️ Usage (Defensive Research)

The implementation involves modifying the source code of a target open-source library (`libcurl`), recompiling it, and then linking a simple loader application against this tampered library.

### Prerequisites

* **libcurl Source Code:** The full source code tree for the `libcurl` library.
* **C/C++ Compiler:** Visual Studio (MSVC) or MinGW is required to recompile the library and the loader.
* **Encrypted Shellcode:** Your own (AES-encrypted) shellcode payload; the shipped source contains a placeholder buffer only.

### Detailed Execution Steps

1.  **Modify the Target Library (libcurl):**
    * Navigate to the `libcurl` source directory.
    * Locate the source file containing the `curl_easy_init` function (typically in `lib/easy.c`).
    * Insert the shellcode loading logic **at the beginning** of the `curl_easy_init` function.
    * *Implementation Note:* The added code should perform the following actions before the legitimate initialization code runs:
        1.  Allocate memory (`VirtualAlloc`).
        2.  Decrypt the embedded (AES-)encrypted shellcode into the allocated memory.
        3.  Execute the shellcode in a new thread (`CreateThread`).
        4.  Wait for the thread to complete (`WaitForSingleObject`) or let it run asynchronously, then proceed with the original `libcurl` initialization.

2.  **Compile the Tampered Library:**
    * Compile the modified `libcurl` source code to generate the static library (`.lib`) or dynamic link library (`.dll`).
    * Ensure the compilation is successful and no errors are generated due to the injected code.

3.  **Compile the Trigger Executable:**
    * Create a simple C/C++ application (`main.c`) that references the modified library.
    * The code simply needs to call the modified API function:
        ```c
        #include <stdio.h>
        #include <windows.h> 
        #include "include/curl/curl.h"

        int main() {
            CURL *curl; 

            printf("try curl_easy_init...\n");

            curl = curl_easy_init();

            if (curl) {
                printf("successfully curl_easy_init\n");
                curl_easy_cleanup(curl);
                printf("curl_easy_cleanup \n");
            } else {
                printf(" curl_easy_init fail！\n");
            }

            printf("end\n");
            return 0;
        }
        ```
    * Compile this executable, linking it against your tampered `libcurl`.

4.  **Execute the PoC:**
    * Run the compiled loader executable.
    * **Observation:** The application should seemingly perform a benign curl initialization, but the injected shellcode will execute in the background (or block execution depending on your wait logic), establishing the C2 session.

5.  **Cleanup:**
    * Remove the compiled binaries and restore the original `libcurl` source code after testing.

> **Warning:** This technique involves modifying and recompiling third-party open-source software. Ensure you comply with the license agreements of the library you are modifying. Execute this PoC **only** in isolated VM environments.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Loader | `main.c` — calls `curl_easy_init()` |
| Modified library file | `easy.c` — a partial upstream libcurl file |
| libcurl source tree | **Not included** — supply it yourself |
| Headers | **Not included** — `main.c` includes `include/curl/curl.h` |
| Payload buffer / key | All-zero placeholders in the modified `easy.c` — supply your own |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

## ⚠️ What Is Missing, and How to Complete It

This is one of two techniques that cannot be built from the repository as-is
(the other is T1). `main.c` includes `include/curl/curl.h`, and the
modification is described as an edit to libcurl's `lib/easy.c`. Neither the
libcurl tree nor the headers are vendored, and the `easy.c` in this folder is
a partial file, not a standalone one.

Recommended workflow:

1. Obtain the external libcurl source tree required by the library build.
2. Locate `lib/easy.c` in that tree and insert the payload-loading logic at
   the **beginning of `curl_easy_init`** (allocate, AES-decrypt, execute on a
   new thread, then continue with normal initialisation).
3. Build libcurl, then build `main.c` against it.


## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** a sequence of irrelevant API calls executes
  before the malicious activity, the C2 beacon is established, and the
  behavioural trace contains a misleading call pattern.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## 🧹 Cleanup / Recovery — none required

The technique modifies and recompiles a third-party library. Restore the
library source and rebuild if you need the original.

## ⚠️ Known Limitations

- Not buildable from the repository alone (see above).
- This technique is strongly payload-dependent in the paper's results
  (0.0% L5 with Cobalt Strike versus 50.0% with Havoc), which the paper uses
  as an example of insufficient generalisation across payloads.
- Modifying and redistributing libcurl is subject to libcurl's own licence.
