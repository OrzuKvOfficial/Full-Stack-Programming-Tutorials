import socket

# Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established.")

client_socket.send(bytes("Hello from server", "utf-8"))
client_socket.close()

# Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('your_server_ip', 8080))
message = client_socket.recv(1024)
print(message.decode("utf-8"))
client_socket.close()
