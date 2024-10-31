import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Misol uchun 127.0.0.1 IP manzilidagi portlarni skanerlaymiz
ip_address = "127.0.0.1"
start_port = 1
end_port = 1024

open_ports = scan_ports(ip_address, start_port, end_port)
if open_ports:
    print(f"Ochiq portlar: {open_ports}")
else:
    print("Ochiq portlar topilmadi.")
