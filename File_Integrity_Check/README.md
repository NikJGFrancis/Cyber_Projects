File Integrity Checker

A Python tool that monitors files in a folder and detects if they are **new, modified, or unchanged** by comparing their **SHA-256 hashes** against previous scans.

This script is useful for **security monitoring, file auditing, and data integrity verification**.

Features

* Computes **SHA-256 hashes** of all files in a target folder.
* Tracks whether files are:

  * **New** (not seen in previous scans)
  * **Modified** (hash changed since last scan)
  * **Unchanged** (hash same as before)
* Saves results into two JSON files:

  * `file_hashes.json` → Stores latest hashes.
  * `file_integrity_report.json` → Detailed scan report.
* Lightweight, no external dependencies.

Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/file-integrity-checker.git
   cd file-integrity-checker
   ```

2. Make sure you have **Python 3.x** installed.

3. Place the files you want to monitor inside the `files_to_check/` folder (or update the `folder_to_check` variable in the script).

4. Run the script:

   ```bash
   python3 integrity_checker.py
   ```

Example

First Run

```
✅ File integrity check completed. Report saved to 'file_integrity_report.json'.
```

`file_integrity_report.json`

```json
[
    {
        "File": "files_to_check/document.txt",
        "Hash": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae",
        "Status": "New",
        "Checked At": "2025-08-25T20:45:12.123456"
    }
]
```

Second Run (after modifying `document.txt`)

```json
[
    {
        "File": "files_to_check/document.txt",
        "Hash": "8a7c6f1b59dd95e03a7ecb0f23cfbc60a4f16e18cb1f3176f07c3c6baf98e5b2",
        "Status": "Modified",
        "Checked At": "2025-08-25T20:49:33.789012"
    }
]
```

Customization

Change the folder being monitored by updating:

  ```python
  folder_to_check = "files_to_check"
  ```
Use different hashing algorithms (e.g., MD5, SHA-1, SHA-512) by modifying `calculate_hash()`.
Extend the script to send alerts (email, Slack, etc.) when files are modified.

Disclaimer

This tool is for **educational and authorized use only**. Do not use it to monitor files you don’t own or have permission to check.

License

This project is licensed under the MIT License.
