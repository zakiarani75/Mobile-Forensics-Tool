📊 Project Name: Android Forensic Data Exporter
Phase 1: Device Connection & Authorization
Physical Connection: Established a secure link between the Android device and Kali Linux using a USB cable.
Developer Mode: Enabled USB Debugging on the mobile device to allow terminal communication.
Device Audit: Verified the connection using the adb devices command.
Phase 2: Data Extraction (Terminal Operations)
SMS Acquisition: Extracted message databases using the command:
adb shell content query --uri content://sms/
Call Log Retrieval: Pulled call history records via:
adb shell content query --uri content://call_log/calls
Evidence Filtering: Applied the grep command to sort through raw system logs and isolate relevant forensic evidence.
Phase 3: Privacy & Data Security
Privacy Protection: Implemented a .gitignore file to ensure sensitive personal data (real phone numbers and messages) remains on the local machine and is never uploaded to the public repository.
Phase 4: Automated Reporting
Python Integration: Developed a script (export_excel.py) to parse the filtered terminal data.
Final Output: Successfully converted raw forensic data into a structured, professional Excel (.xlsx) report for easy analysis.
