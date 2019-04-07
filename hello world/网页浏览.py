import socket

ss = socket.socket()

addr = ('0.0.0.0', 52338)

ss.bind(addr)

ss.listen()
text = """
HTTP/1.1 200 OK
"""

text1 = "\r\n"
text2 = 'hello world'
text3 = text + text1 + text2
while 1:
    coon, addr = ss.accept()
    msg = coon.recv(65535)
    print(msg.decode())
    coon.send(text3.encode())