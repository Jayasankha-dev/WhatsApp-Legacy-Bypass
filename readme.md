# 📱 WhatsApp Forensic Tool v2.0 (Legacy Bypass Suite)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-Android-orange.svg)

## 📌 Overview
[cite_start]This suite is a specialized digital forensic tool designed to extract WhatsApp databases and encryption keys from non-rooted Android devices[cite: 1, 3]. [cite_start]It specifically addresses the security restrictions in **Android 10, 11, and 12 (SDK 29+)** where standard `adb backup` commands are blocked via the `allowBackup="false"` attribute.

[cite_start]By utilizing a **Legacy Downgrade Technique**, the tool temporarily replaces the WhatsApp binary with an older version (v2.11.431) that permits data extraction without compromising the user's chat history.



---

## ✨ Key Features
* [cite_start]**Key Extraction:** Automatically pulls the `whatsapp.key` file required to decrypt `msgstore.db.crypt14/15`[cite: 5].
* [cite_start]**Database Carving:** Extracts core databases including `msgstore.db` (Messages), `wa.db` (Contacts), and `axolotl.db` (Identity Keys)[cite: 5].
* **Binary Image Recovery:** Includes PowerShell scripts to recover profile pictures via hex-signature analysis.
* [cite_start]**SDK 29+ Support:** Specifically designed to bypass modern Android security layers.
* [cite_start]**Automated Cleanup:** Automatically triggers the restoration of the latest WhatsApp version via Play Store after extraction[cite: 5].

---

## 📁 Project Structure
```text
[cite_start]├── whatsapp_extractor.py     # Main Python automation logic 
[cite_start]├── requirements.txt          # Python dependencies 
├── scripts/                  # Advanced Recovery Scripts
│   ├── force_image_carver.ps1   # Bulk file discovery
│   └── binary_image_carver.ps1  # Hex-based JPEG carving
[cite_start]├── bin/                      # Required Binaries (User provided) 
[cite_start]│   ├── adb.exe               # Android Debug Bridge [cite: 2, 8]
[cite_start]│   ├── abe.jar               # Android Backup Extractor [cite: 2, 7]
[cite_start]│   └── LegacyWhatsApp.apk    # WhatsApp v2.11.431 
[cite_start]├── tmp/                      # Staging area for .ab and .tar files 
[cite_start]└── extracted/                # Final Forensic Output 
🛠️ Installation & Requirements
1. Prerequisites

Java (JRE/JDK): Must be installed and added to your System Environment Variables (PATH).
+1


Python 3.8+.
+1


ADB Drivers: Ensure your PC recognizes your Android device.
+1

2. Setup
Clone the repository and install the necessary libraries:

Bash
git clone [https://github.com/Jayasankha-dev/WhatsApp-Legacy-Bypass.git](https://github.com/Jayasankha-dev/WhatsApp-Legacy-Bypass.git)
cd WhatsApp-Legacy-Bypass
pip install -r requirements.txt
3. Binary Placement
Due to copyright restrictions, you must provide the following in the bin/ folder:
+1

Place adb.exe and abe.jar in bin/.
+1

Download WhatsApp v2.11.431 (Legacy) and rename it to LegacyWhatsApp.apk in the tmp/ or bin/ folder as per script requirements.
+1

🚀 Usage Guide
Step 1: Prepare Device
Enable USB Debugging on the target device via Developer Options. Ensure "Install via USB" is allowed if prompted.
+1

Step 2: Run Extractor
Launch the main script:

Bash
python whatsapp_extractor.py

Important: When the phone prompts for a backup, leave the password field blank and tap "Back up my data".

Step 3: Advanced Media Recovery (Optional)
If the database is truncated or profile pictures are missing, use the provided PowerShell tools:

Open PowerShell in the scripts/ folder.

Run .\force_image_carver.ps1 to identify potential image files.

Run .\binary_image_carver.ps1 to reconstruct JPEGs using hex-headers (0xFFD8).

⚠️ Troubleshooting
1024 Bytes Error: If the backup file is only 1KB, the downgrade did not apply correctly. Ensure LegacyWhatsApp.apk is the correct version.

Execution Policy Error: If PowerShell scripts won't run, execute this command first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process.


BadPaddingException: This occurs if you entered a password on the phone during backup but left it blank in the script (or vice versa).

⚖️ Legal Disclaimer
This software is intended for educational and authorized forensic purposes only. Unauthorized access to data is illegal. The developers assume no liability for misuse or data loss resulting from the use of this tool.

📄 License
Distributed under the MIT License. See LICENSE for more information.
