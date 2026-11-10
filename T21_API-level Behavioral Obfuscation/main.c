#include <stdio.h>
#include <windows.h> 
#include "include/curl/curl.h"

int main() {
    CURL *curl; // Declare a CURL pointer

    printf("try curl_easy_init...\n");

    // Call the curl_easy_init function
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