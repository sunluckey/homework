import os
import socket

text = os.path.dirname(__file__)
text1 = os.path.join(text, '15236.jpg')
with open(text1, 'rb') as f:
    text3 = f.read()

l1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('192.168.0.107', 52333)

l1.connect(addr)

l1.sendall(text3)

l1.close()
