Multi-threaded Port Scanner

A lightweight Python tool that scans a target host (IP or hostname) for **open TCP ports** using multithreading.
It’s designed to be **fast, simple, and educational**, making it a great project for those learning about networking, sockets, and concurrency.

Features

* Scans ports **20–1024** (default, can be modified).
* Uses **multithreading** for faster scans.
* Detects and prints open ports in real time.
* Works with both **IP addresses** and **hostnames**.
* Minimal dependencies — just Python’s standard library.

Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/port-scanner.git
   cd port-scanner
   ```

2. Make sure you have **Python 3.x** installed.

3. Run the script:

   ```bash
   python3 port_scanner.py
   ```

4. Enter the target host when prompted:

   ```
   Enter target host (IP or hostname): scanme.nmap.org
   ```

Example Output

Example 1 — Scanning a hostname

```
Enter target host (IP or hostname): scanme.nmap.org
Port 22 is open
Port 80 is open

Scanning complete. Open ports: [22, 80]
```

Example 2 — Scanning an IP

```
Enter target host (IP or hostname): 192.168.1.10
Port 21 is open
Port 443 is open

Scanning complete. Open ports: [21, 443]
```

Disclaimer

This tool is intended for **educational and authorized security testing only.
Do not use it to scan systems without explicit permission — unauthorized scanning may be illegal.

Customization

Change the scan range by editing:

  ```python
  start_port = 1
  end_port = 65535
  ```
Adjust threading by modifying:

  ```python
  max_threads = 200
  ```
Add banner grabbing or service detection for advanced use cases.

License

This project is licensed under the MIT License.
