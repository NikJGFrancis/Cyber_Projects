import socket
import threading
from queue import Queue

# ---------- Configuration ----------
target = input("Enter target host (IP or hostname): ")
start_port = 20
end_port = 1024
max_threads = 100  # Number of threads

# ---------- Thread-safe queue to manage ports ----------
port_queue = Queue()
open_ports = []  # Stores open ports

# ---------- Worker function ----------
def scan_port():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
            s.close()
        except socket.error:
            pass
        port_queue.task_done()

# ---------- Add ports to the queue ----------
for port in range(start_port, end_port + 1):
    port_queue.put(port)

# ---------- Start threads ----------
threads = []
for _ in range(max_threads):
    t = threading.Thread(target=scan_port)
    t.start()
    threads.append(t)

# ---------- Wait for all threads to finish ----------
for t in threads:
    t.join()

print(f"\nScanning complete. Open ports: {open_ports}")
