import os
import subprocess
import tarfile
import time

def extract_key():
    print("====================================================")
    print("      WHATSAPP KEY EXTRACTOR (LEGACY METHOD)        ")
    print("====================================================")
    
    # Check if Legacy APK exists
    if not os.path.exists("bin/LegacyWhatsApp.apk"):
        print("[-] ERROR: bin/LegacyWhatsApp.apk not found!")
        print("[!] Please download WhatsApp v2.11.431 and place it in the bin folder.")
        return

    try:
        # 1. Check Device Connection
        print("[*] Checking for connected devices...")
        subprocess.check_output("bin\\adb.exe devices", shell=True)

        # 2. Downgrade WhatsApp
        print("[*] Downgrading WhatsApp... (Keeping Data)")
        print("[!] This might take a minute. Do not disconnect the phone.")
        # -d allows downgrade, -r keeps app data
        status = os.system("bin\\adb.exe install -r -d bin\\LegacyWhatsApp.apk")
        
        if status != 0:
            print("[-] Downgrade failed. Device might have 'Install via USB' disabled.")
            return

        print("[+] Downgrade Successful!")
        time.sleep(2)

        # 3. Trigger ADB Backup
        print("[*] Triggering Backup... CHECK PHONE SCREEN!")
        print("[!] DO NOT enter a password. Tap 'Back up my data'.")
        os.system("bin\\adb.exe backup -f tmp/key_backup.ab com.whatsapp")

        # 4. Unpack Backup
        if os.path.exists("tmp/key_backup.ab"):
            print("[*] Unpacking backup using ABE...")
            os.system("java -jar bin/abe.jar unpack tmp/key_backup.ab tmp/key_backup.tar")
            
            # 5. Extract Key from Tar
            if os.path.exists("tmp/key_backup.tar"):
                print("[*] Searching for Key file...")
                extracted = False
                with tarfile.open("tmp/key_backup.tar") as tar:
                    for member in tar.getmembers():
                        if "apps/com.whatsapp/f/key" in member.name:
                            content = tar.extractfile(member)
                            with open("extracted/key", "wb") as f:
                                f.write(content.read())
                            print(f"[SUCCESS] Key extracted to: {os.getcwd()}\\extracted\\key")
                            extracted = True
                
                if not extracted:
                    print("[-] Key file not found in backup. The app might not have initialized.")

        # 6. Prompt to Restore
        print("\n[*] Cleanup: Opening Play Store to update WhatsApp...")
        os.system("bin\\adb.exe shell am start -a android.intent.action.VIEW -d 'market://details?id=com.whatsapp'")
        print("[!] IMPORTANT: Update WhatsApp immediately to resume normal use.")

    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    extract_key()