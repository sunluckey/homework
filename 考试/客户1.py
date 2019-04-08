import socket
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
executor = ThreadPoolExecutor(max_workers=2)
while True:
    print('welcome to real world')
    name = input('请输入个人昵称，不得少于一个字，不得超过10个字：')
    if 0 < len(name) <= 10:
        break
server_addr = ('127.0.0.1', 52333)
client.connect(server_addr)
print('恭喜你' + '-' * 5 + '>' + '已通过我们的考验(* ￣3)(ε￣ *)')
print('✿✿ヽ(°▽°)ノ✿' + '欢迎来到真实的世界' + '✿✿ヽ(°▽°)ノ✿')
print('-*-' * 5 + '输入close关闭与真实世界的连接' + '-*-' * 5)
def saysomething():
    while True:
        say = input('')
        if say == 'close':
            break
        client.send('{}说：{}'.format(name, say).encode())
        print('{}说：{}'.format(name, say))

def receivenews():
    while True:
        receive = client.recv(65535)
        print(receive.decode())


pools_list = list()


l1 = [saysomething, receivenews]
for i in l1:
    pools_list.append(executor.submit(i))
#
for i in as_completed(pools_list):
    i.result()
#
# t1 = Thread(target=receivenews)
#
# t2 = Thread(target=saysomething)
#
# t1.start()
# t2.start()
#
# t2.join()

print('-*-' * 5 + '真实的世界断开连接' + '-*-' * 5)
client.close()
