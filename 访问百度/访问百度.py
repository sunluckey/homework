import socket

l1 = socket.socket()

addr = ('111.13.100.91', 80)

l1.connect(addr)

l1.send(b'are you ok')
print('ok')
res = b''
x = b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\n' \
    b'Upgrade-Insecure-Requests: 1\r\n' \
    b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    b'Chrome/73.0.3683.86 Safari/537.36\r\n' \
    b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,' \
    b'*/*;q=0.8,application/signed-exchange;v=b3\r\n' \
    b'Accept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
l1.send(x)
print('yes')
news = l1.recv(65535)
print('ok1')
res += news
print(res.decode())
