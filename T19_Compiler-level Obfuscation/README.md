# T19: Compiler-level Obfuscation (OLLVM)

**DET classification:** Detection → Obfuscation

This technique utilizes the **Obfuscator-LLVM (OLLVM)** framework, a modified version of the LLVM compiler, to introduce substantial complexity into the compiled binary. OLLVM applies various compiler-level transformations to the malicious code's core logic *before* the final binary is produced.

The primary objective is to hinder static analysis, dynamic analysis, and signature-based detection by:

1.  **Control Flow Flattening (Flattening):** Eliminating structured control flow (like `if` statements and loops) and replacing them with complex state machines.
2.  **Instruction Substitution:** Replacing standard arithmetic operations with functionally equivalent, but less obvious, instruction sequences.
3.  **Bogus Control Flow:** Injecting deceptive and dead code paths to confuse decompilers and behavioral execution traces.

This obfuscation targets the EDR's ability to extract reliable signatures or analyze behavioral patterns based on expected code structures.

## 📊 Evaluation Results

> Aggregated over **36 test-case outcomes**: 3 payload families (Cobalt Strike, Havoc, AdaptixC2) × 6 products × 2 Windows environments (Windows 11 Enterprise, Windows Server 2025), each scored on the five-tiered prevention-stage model (L1–L5).

**Overall effectiveness.** The technique reached **L5 (Operational Success) in 16.7%** of its 36 outcomes.

**Bypass Depth Distribution (BDD).**

| L1 Pre-execution | L2 Pre-C2 | L3 Pre-command | L4 Command-stage | L5 Operational Success |
| :---: | :---: | :---: | :---: | :---: |
| 33.3% | 41.7% | 8.3% | 0.0% | **16.7%** |

**Payload sensitivity (L5 rate).**

| Cobalt Strike | Havoc | AdaptixC2 |
| :---: | :---: | :---: |
| 0.0% | 33.3% | 16.7% |

**Per-product L5 rate** (n=6 per product; Defender AV = Microsoft Defender Antivirus).

| Sophos | Kaspersky | Bitdefender | Elastic Security | Huorong | Defender AV |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0.0% | 33.3% | 0.0% | 0.0% | 66.7% | 0.0% |

**Interpretation.** Compiler-level control-flow transformations produced only limited evasion. Three-quarters of the outcomes were stopped at L1 (33.3%) or L2 (41.7%): Microsoft Defender Antivirus and Elastic Security prevented every execution at L1, Sophos and Bitdefender stopped all outcomes at L2. Operational success was reached against Huorong (L5 in 4 of 6 outcomes) and, partially, Kaspersky (2 of 6). The result is payload-dependent (0.0% with Cobalt Strike vs. 33.3% with Havoc), consistent with the paper's observation that obfuscation alters static structure while runtime behavior — the signal most products detect on — remains intact.

## ⚙️ Usage (Defensive Research)

The implementation requires a specific OLLVM-modified toolchain (like `clang-cl.exe`) to compile the source code for the payload or loader.

### Prerequisites

* **Source Code:** The source code for the evasion sample (e.g., `yourcode.cpp`) must be available.
* **Build Environment:** Visual Studio 2022 (with C++ Desktop Development workload) and CMake.

### Detailed Execution Steps

#### 1. Building the OLLVM Toolchain (LLVM 17 Patching)

Since pre-compiled binaries are often unavailable or version-specific, you must build the toolchain from the source.

1.  **Download Source:**
    * Download the official [LLVM 17.0.6 Source Code].
    * Extract the archive.

2.  **Apply OLLVM Patch:**
    * Download the OLLVM 17 project files (from the repository provided in your reference).
    * Copy and overwrite the OLLVM files into the extracted official LLVM source directory.

3.  **Modify Source Code (Crucial Step):**
    * You must modify `Function.h` to change the visibility of `getBasicBlockList` from private to public, otherwise the build will fail.
    * **File Path:** `...\llvm-project\llvm\include\llvm\IR\Function.h`
    * **Target Line (approx 722):** Find the `getBasicBlockList` function.
    * **Action:** Comment out the `private:` keyword or move the function to the `public:` section.

4.  **Generate Build Config (CMake):**
    * Open a terminal, navigate to the `llvm-project` directory, and run the following commands to generate the Visual Studio solution:
    ```bash
    cd llvm-project
    mkdir build_vs2022
    cd build_vs2022
    cmake -G "Visual Studio 17 2022" -DCMAKE_C_FLAGS=/utf-8 -DCMAKE_CXX_FLAGS=/utf-8 -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_EH=OFF -DLLVM_ENABLE_RTTI=OFF -DLLVM_ENABLE_ASSERTIONS=ON -DLLVM_ENABLE_PROJECTS="clang;lld" -A x64 ../llvm
    ```

5.  **Compile LLVM:**
    * Open the generated `LLVM.sln` in the `build_vs2022` folder.
    * Build the solution (Release mode recommended). This will produce `clang.exe` and `clang-cl.exe`.

#### 2. Compile Payload with Obfuscation

Once the toolchain is built, use the generated `clang` compiler to build your malicious payload.

* **Command Line Compilation:**
    Use the `-mllvm` flag to pass specific obfuscation arguments.
    ```bash
    # Example: Enable Flattening, Bogus Control Flow, and Instruction Substitution
    path\to\build\bin\clang-cl.exe -mllvm -fla -mllvm -bcf -mllvm -bcf_prob=80 -mllvm -sub -mllvm -sub_loop=3 yourcode.cpp -o obfuscated_payload.exe
    ```

* **Available Flags:**
    * `-fla`: Control Flow Flattening.
    * `-bcf`: Bogus Control Flow.
    * `-bcf_prob`: Probability of BCF (default 70).
    * `-sub`: Instruction Substitution.
    * `-sobf`: String Obfuscation (CLI only).
    * `-split`: Basic Block Split.

#### 3. Validation

* Run the resulting `obfuscated_payload.exe` to verify its functionality (it should behave exactly like the original).
* Use tools like IDA Pro or Ghidra to analyze the control flow graph. You should see a significant increase in graph complexity compared to a non-obfuscated build.

> **Warning:** Obfuscated binaries can sometimes be much larger or slower than their original counterparts. Always validate the functionality of the compiled output before using it in EDR testing.

---

## 📦 Repository Contents

| Item | Status |
| :--- | :--- |
| Source | `exeshellcode.cpp` (loader stub to be obfuscated) |
| Payload buffer / key | All-zero placeholders — supply your own |
| Toolchain | **Not included** — you build OLLVM yourself |
| Prebuilt executable | Not distributed — build from source ([BUILD.md](../BUILD.md)) |

`exeshellcode.cpp` compiles cleanly with MinGW-w64 gcc 14.2.0 (verified); see
[BUILD.md](../BUILD.md).

## 🧪 Validation Criteria (paper, Table 7)

- **Required privilege:** Standard User.
- **Evasion-logic criterion:** the obfuscated executable runs successfully,
  the payload executes despite the control-flow obfuscation, and the C2
  beacon is established.
- **Payload-functionality check:** beacon observed within 60 seconds, and the
  beacon answers test commands.

## ⚙️ Building the Obfuscating Toolchain

Prebuilt binaries are generally unavailable, so the toolchain is built from
source (see the steps in this README): LLVM 17.0.6 + the OLLVM 17 patch set
(paper reference [32]), plus the documented `Function.h` visibility edit,
then CMake + Visual Studio.


## 🧹 Cleanup / Recovery — none required

Obfuscation transforms a file; no system state is modified. Keep the
unobfuscated build for comparison.

## ⚠️ Known Limitations

- The toolchain build is long and version-sensitive; the `Function.h` edit is
  required or the build fails.
- Obfuscated binaries can be substantially larger and slower; always verify
  functionality before EDR testing.
- The technique changes static structure but not runtime behaviour, which is
  why the paper reports it as the least effective Layer 2 strategy.
