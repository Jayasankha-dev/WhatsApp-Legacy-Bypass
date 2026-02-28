# 📱 WhatsApp Forensic Tool v2.0 (Full Suite)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![Platform](https://img.shields.io/badge/platform-Android-orange.svg)

## 📌 Overview
This tool is designed for digital forensic investigators and security researchers to extract WhatsApp data from Android devices. It specializes in bypassing the "No-Backup" restriction introduced in Android 10+ (SDK 29) by utilizing a temporary legacy downgrade technique.



## ✨ Features
* **Key Extraction:** Pulls the `whatsapp.key` file required for database decryption.
* **Database Carving:** Extracts `msgstore.db`, `wa.db`, and `axolotl.db`.
* **Thumbnail Recovery:** Automatically carves profile pictures/thumbnails from `wa.db`.
* **Version Bypass:** Specifically handles Android 10/11+ security barriers using the Legacy Method.
* **Automated Workflow:** Clean temporary file management and automated ADB signaling.

## 📁 Project Structure
```text
├── whatsapp_extractor.py   # Main Python logic
├── bin/
│   ├── adb.exe             # Android Debug Bridge
│   ├── abe.jar             # Android Backup Extractor
│   └── LegacyWhatsApp.apk  # WhatsApp v2.11.431 (User provided)
├── tmp/                    # Temporary storage for .ab and .tar files
└── extracted/              # Final output folder for keys and databases
