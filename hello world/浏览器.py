import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 52333)
client.connect(server_addr)
msg = client.recv(65535)
print(msg.decode())
client.close()


