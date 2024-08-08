import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print("Received", repr(data))

conn.close()
