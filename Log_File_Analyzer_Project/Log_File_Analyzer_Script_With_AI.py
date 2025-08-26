import re
import csv
from collections import defaultdict

# ---------- Configuration ----------
log_file = "auth.log"       # path to your log file
report_file = "failed_logins.csv"  # output CSV

# Regex pattern to match failed login attempts
# Example Linux auth.log line:
# "Aug 24 23:50:12 server sshd[12345]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2"
FAILED_LOGIN_PATTERN = re.compile(
    r'Failed password.*from (\d+\.\d+\.\d+\.\d+)'
)

# Dictionary to count failed attempts per IP
failed_attempts = defaultdict(int)

# ---------- Process the log ----------
with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        match = FAILED_LOGIN_PATTERN.search(line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

# ---------- Generate CSV Report ----------
with open(report_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['IP Address', 'Failed Attempts'])
    for ip, count in failed_attempts.items():
        writer.writerow([ip, count])

print(f"Report generated: {report_file}")
