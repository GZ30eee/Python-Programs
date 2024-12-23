# Find Local IPs
import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Local IP address: {local_ip}")
