import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 52333)
server.bind(server_addr)
server.listen(5)
print('输入close退出真实的世界')
clients = list()
end = list()


def acceptuser():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print('真实的世界被{}连接,当前连接数：{}'.format(addr, len(clients)))

def receiveuser(client):
    while True:
        try:
            receivnews = client.recv(65535)
        except Exception:
            clients.remove(client)
            end.remove(client)
            print('真实的世界被断开,当前连接数：{}'.format(len(clients)))
            break
        print(receivnews.decode())
        for i in clients:
            if i != client:
                i.send(receivnews)

def saytoeveryone():
    while True:
        outdata = input('-->')
        if outdata == 'close':
            break
        print('to everyone:{}'.format(outdata))
        for client in clients:
            client.send('所有人听着:{}'.format(outdata).encode())

def addthread():
    while True:
        for i in clients:
            if i in end:
                continue
            index = Thread(target=receiveuser, args=(i,))
            index.start()
            end.append(i)


t1 = Thread(target=addthread)
t1.start()

t2 = Thread(target=acceptuser)
t2.start()

t3 = Thread(target=saytoeveryone)
t3.start()

t3.join()

for client in clients:
    client.close()
print('-*-' + '真实的世界已关门' + '-*-')




