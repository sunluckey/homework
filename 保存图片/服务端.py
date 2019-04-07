import socket
import os
l1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text = os.path.dirname(__file__)
text1 = os.path.join(text, '88888.jpg')
addr = ('192.168.0.107', 52333)
l1.bind(addr)

l1.listen()

conn, addr = l1.accept()
l2 = b''
while 1:
    news = conn.recv(65535)
    if not news:
        break
    l2 += news
with open(text1, 'wb') as f:
    f.write(l2)

conn.close()
l1.close()