import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 52333)
server.bind(server_addr)
server.listen(10)
print('机甲一号启动')
conn, conn_addr = server.accept()
ra = 'hello world'
conn.send(ra.encode())
server.close()
