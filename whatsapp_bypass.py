import os
import subprocess
import tarfile
import sqlite3
import sys
import time

# Colors for terminal (Optional but looks pro on GitHub)
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode().strip()

def attempt_bypass():
    print(f"{Colors.GREEN}====================================================")
    print("   ADVANCED WHATSAPP FORENSIC TOOL (FULL SUITE)     ")
    print(f"===================================================={Colors.END}")

    # Setup folders
    for folder in ['tmp', 'extracted', 'extracted/profile_pictures']:
        os.makedirs(folder, exist_ok=True)

    try:
        print("[*] Initializing ADB...")
        os.system("bin\\adb.exe start-server")
        os.system("bin\\adb.exe wait-for-device")
        sdk_ver = int(run_cmd("bin\\adb.exe shell getprop ro.build.version.sdk"))
        print(f"[+] Device Found (Android SDK {sdk_ver})")

        # --- SPECIAL LOGIC FOR ANDROID 10+ ---
        if sdk_ver >= 29:
            print(f"{Colors.YELLOW}[!] Android 10+ detected. Standard backup might fail.{Colors.END}")
            print("[?] Would you like to attempt the Legacy Downgrade method? (y/n)")
            choice = input("> ").lower()
            if choice == 'y':
                print("[*] Initiating Legacy Downgrade... (Ensure LegacyWhatsApp.apk is in bin/)")
                # Add downgrade command here: adb install -r -d bin/LegacyWhatsApp.apk
        # -------------------------------------

    except Exception as e:
        print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        return

    print("[*] Triggering Backup. ACTION REQUIRED ON PHONE!")
    print("[!] Tap 'Back up my data' (Leave password blank).")
    os.system("bin\\adb.exe backup -f tmp/whatsapp.ab -noapk com.whatsapp")

    if not os.path.exists("tmp/whatsapp.ab") or os.path.getsize("tmp/whatsapp.ab") < 10000:
        print(f"{Colors.RED}[-] Backup empty. This is likely due to Android 10+ security.{Colors.END}")
        return

    print("[+] Extracting data...")
    # Using ABE to unpack
    os.system("java -jar bin/abe.jar unpack tmp/whatsapp.ab tmp/whatsapp.tar")

    if os.path.exists("tmp/whatsapp.tar"):
        extract_from_tar("tmp/whatsapp.tar")

def extract_from_tar(tar_path):
    print("[*] Searching for databases...")
    with tarfile.open(tar_path) as tar:
        targets = {
            "apps/com.whatsapp/db/wa.db": "extracted/wa.db",
            "apps/com.whatsapp/f/key": "extracted/whatsapp.key",
            "apps/com.whatsapp/db/msgstore.db": "extracted/msgstore.db",
        }
        for member in tar.getmembers():
            if member.name in targets:
                content = tar.extractfile(member)
                with open(targets[member.name], "wb") as f:
                    f.write(content.read())
                print(f"[+] Extracted: {os.path.basename(member.name)}")

    if os.path.exists("extracted/wa.db"):
        extract_photos("extracted/wa.db")

def extract_photos(db_path):
    # (Your photo extraction code remains the same)
    print("[*] Carving profile pictures...")
    # ... logic here ...

if __name__ == "__main__":
    attempt_bypass()