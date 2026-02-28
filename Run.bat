@echo off
SETLOCAL EnableDelayedExpansion
title WhatsApp Forensic Suite - Launcher
color 0B

echo ====================================================
echo    WHATSAPP FORENSIC TOOL v2.0 (LAUNCHER)
echo ====================================================
echo.

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [!] ERROR: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/
    pause
    exit
)

:: 2. Check for Java (Required for ABE)
java -version >nul 2>&1
if %errorlevel% neq 0 (
    color 0E
    echo [!] WARNING: Java was not found. 
    echo Extraction from .ab files will fail without Java.
    echo.
)

:: 3. Check for ADB in bin folder
if not exist "bin\adb.exe" (
    color 0C
    echo [!] ERROR: bin\adb.exe not found!
    echo Please ensure adb.exe is inside the 'bin' folder.
    pause
    exit
)

:: 4. Start ADB Server
echo [*] Starting ADB Server...
bin\adb.exe start-server
echo [*] Waiting for Android device...
bin\adb.exe wait-for-device
echo [+] Device Detected!
echo.

:: 5. Run the Python Script
echo [*] Launching Python Forensic Script...
echo ----------------------------------------------------
python whatsapp_bypass.py
echo ----------------------------------------------------

echo.
echo [*] Process Finished. 
echo [*] Check 'extracted' folder for databases and photos.
echo.
pause