import sys
import socket
from datetime import datetime

# ---------- Target Definition ----------
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Usage: python port_scanner.py <hostname>")
    sys.exit()

# ---------- Banner ----------
print("-" * 50)
print("PORT SCANNER")
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

# ---------- Port Scanning ----------
try:
    # Scan ports 1 to 65535
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))  # returns 0 if port is open
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program!")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved!")
    sys.exit()
except socket.error:
    print("\nServer not responding!")
    sys.exit()
