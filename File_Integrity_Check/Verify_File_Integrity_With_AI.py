import os
import hashlib
import json
from datetime import datetime

# ----------------- CONFIG -----------------
folder_to_check = "files_to_check"  # Folder containing files to monitor
hash_record_file = "file_hashes.json"  # JSON file to store previous hashes
report_file = "file_integrity_report.json"  # JSON report of current scan

# ----------------- FUNCTION TO CALCULATE SHA-256 -----------------
def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# ----------------- LOAD PREVIOUS HASHES -----------------
if os.path.exists(hash_record_file):
    with open(hash_record_file, "r") as f:
        previous_hashes = json.load(f)
else:
    previous_hashes = {}

# ----------------- SCAN FILES -----------------
current_hashes = {}
report = []

for root, _, files in os.walk(folder_to_check):
    for file in files:
        file_path = os.path.join(root, file)
        file_hash = calculate_hash(file_path)
        current_hashes[file_path] = file_hash

        # Check if file has changed since last hash
        if file_path in previous_hashes:
            if previous_hashes[file_path] != file_hash:
                status = "Modified"
            else:
                status = "Unchanged"
        else:
            status = "New"

        report.append({
            "File": file_path,
            "Hash": file_hash,
            "Status": status,
            "Checked At": datetime.now().isoformat()
        })

# ----------------- SAVE CURRENT HASHES -----------------
with open(hash_record_file, "w") as f:
    json.dump(current_hashes, f, indent=4)

# ----------------- SAVE REPORT -----------------
with open(report_file, "w") as f:
    json.dump(report, f, indent=4)

print(f"✅ File integrity check completed. Report saved to '{report_file}'.")
