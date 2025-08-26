Log File Analyzer

A lightweight Python script that parses Linux authentication logs (`/var/log/auth.log`) to detect **failed SSH login attempts** and generate a CSV report summarizing the number of failures per IP address.

This is useful for **system administrators, cybersecurity analysts, and hobbyists** who want to quickly identify brute-force attempts and potential malicious activity on their servers.

Features

* Parses `auth.log` to detect failed SSH login attempts.
* Extracts attacker IP addresses and counts their failed attempts.
* Exports results into a clean CSV report.
* Simple, fast, and no external dependencies.

Example Log Line

From a typical `auth.log`:

```
Aug 24 23:50:12 server sshd[12345]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
```

The script will detect the IP (`192.168.1.10`) and increment its failed attempt count.

Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/failed-ssh-login-analyzer.git
   cd failed-ssh-login-analyzer
   ```

2. Make sure you have Python 3.x installed.

3. Place your system’s `auth.log` file in the project directory (or adjust the `log_file` path in the script).

4. Run the script:

   ```bash
   python3 failed_logins.py
   ```

5. The report will be saved as:

   ```
   failed_logins.csv
   ```

# Output:

CSV Report (`failed_logins.csv`)

| IP Address   | Failed Attempts |
| ------------ | --------------- |
| 192.168.1.10 | 12              |
| 203.0.113.25 | 5               |
| 10.0.0.45    | 3               |

Use Cases

* Detecting brute force SSH attacks.
* Identifying suspicious IP addresses.
* Feeding data into firewall rules (e.g., block frequent offenders).
