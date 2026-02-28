📱 WhatsApp Forensic Tool v2.0 (Legacy Bypass Suite)
📌 Overview
This suite is a specialized digital forensic tool designed to extract WhatsApp databases and encryption keys from non-rooted Android devices. It specifically addresses the security restrictions in Android 10, 11, and 12 (SDK 29+) where standard adb backup commands are blocked (allowBackup="false").

By utilizing a Legacy Downgrade Technique, the tool temporarily replaces the WhatsApp binary with an older version (v2.11.431) that permits data extraction, without compromising the user's chat history.

✨ Key Features
Key Extraction: Automatically pulls the whatsapp.key file required to decrypt msgstore.db.crypt14/15.

Database Carving: Extracts core databases: msgstore.db (Messages), wa.db (Contacts), and axolotl.db (Identity Keys).

Binary Image Recovery: Includes PowerShell scripts to recover profile pictures via hex-signature analysis.

SDK 29+ Support: Specifically designed to bypass modern Android security layers.

Automated Cleanup: Automatically triggers the restoration of the latest WhatsApp version via Play Store after extraction.

📁 Project Structure
Plaintext
├── whatsapp_extractor.py     # Main Python automation logic
├── requirements.txt          # Python dependencies
├── scripts/                  # Advanced Recovery Scripts
│   ├── force_image_carver.ps1   # Bulk file discovery
│   └── binary_image_carver.ps1  # Hex-based JPEG carving
├── bin/                      # Required Binaries (User provided)
│   ├── adb.exe               # Android Debug Bridge
│   ├── abe.jar               # Android Backup Extractor
│   └── LegacyWhatsApp.apk    # WhatsApp v2.11.431
├── tmp/                      # Staging area for .ab and .tar files
└── extracted/                # Final Forensic Output
🛠️ Installation & Requirements
1. Prerequisites
Java (JRE/JDK): Must be installed and added to your System Environment Variables (PATH).

Python 3.8+

ADB Drivers: Ensure your PC recognizes your Android device.

2. Setup
Clone the repository and install the necessary libraries:

Bash
git clone https://github.com/Jayasankha-dev/WhatsApp-Legacy-Bypass.git
cd WhatsApp-Legacy-Bypass
pip install -r requirements.txt
3. Binary Placement
Due to copyright restrictions, you must provide the following in the bin/ folder:

Place adb.exe and abe.jar in bin/.

Download WhatsApp v2.11.431 (Legacy) from a trusted source (like APKMirror) and rename it to LegacyWhatsApp.apk.

🚀 Usage Guide
Step 1: Prepare Device
Enable USB Debugging on the target device via Developer Options. Ensure "Install via USB" is allowed if prompted.

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
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

BadPaddingException: This occurs if you entered a password on the phone during backup but left it blank in the script (or vice versa).

⚖️ Legal Disclaimer
This software is intended for educational and authorized forensic purposes only. Unauthorized access to data is illegal. The developers assume no liability for misuse or data loss resulting from the use of this tool.

📄 License
Distributed under the MIT License. See LICENSE for more information.
