import socket
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 52333)
server.bind(server_addr)
server.listen(5)
print('输入close退出真实的世界')
clients = list()
end = list()
executor = ThreadPoolExecutor(max_workers=5)

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
            print('一位同胞因为意外断开,当前剩余清醒人数：{}'.format(len(clients)))
            break
        print(receivnews.decode())
        for i in clients:
            if i != client:
                i.send(receivnews)

def saytoeveryone():
    while True:
        inputnews = input('-->')
        if inputnews == 'close':
            continue
        print('to everyone:{}'.format(inputnews))
        for client in clients:
            client.send('所有人听着:{}'.format(inputnews).encode())

def addthread():
    while True:
        for i in clients:
            if i in end:
                continue
            index = Thread(target=receiveuser, args=(i,))
            index.start()
            end.append(i)
pools_list = list()


l1 = [addthread, acceptuser, saytoeveryone]
for i in l1:
    pools_list.append(executor.submit(i))
#
for i in as_completed(pools_list):
    i.result()
# t1 = Thread(target=addthread)
# t1.start()
#
# t2 = Thread(target=acceptuser)
# t2.start()
#
# t3 = Thread(target=saytoeveryone)
# t3.start()
#
# t3.join()

for client in clients:
    client.close()
print('-*-' + '真实的世界已关门' + '-*-')
