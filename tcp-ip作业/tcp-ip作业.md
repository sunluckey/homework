# TCP/IP作业

### 1.Http与Https的区别。

1-https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。
2-http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。

3-http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

4-http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。 

### 2.URI和URL的区别。

URI 表示请求服务器的路径，定义这么一个资源。而URL同时说明要如何访问这个资源（http://）。

### 3.HTTPS工作原理。

通过SSL协议对使用HTTP协议传输的内容进行加密。

首先客户端请求HTTP链接，然后服务器端返回证书（公钥），客户端产生随机秘钥，然后用公钥对秘钥加密发送给服务器端，服务器端通过私钥解除公钥的加密，获得秘钥，然后发送使用秘钥加密的信息，完成信息的加密传输。

### 4.一次完整的HTTP请求所经历的7个步骤

1. 建立TCP连接
2.  Web浏览器向Web服务器发送请求命令 
3.  Web浏览器发送请求头信息
4.  Web服务器应答
5.  Web服务器发送应答头信息
6.   Web服务器向浏览器发送数据 
7.   Web服务器关闭TCP连接

### 5.常见的HTTP相应状态码

200：请求浏览成功

201：添加成功

204：删除成功

301：永久移除

302：已找到

404：GG

504：服务器错误

1xx：请求正在处理

### 6.TCP协议和UDP协议的区别是什么

TCP 是面向连接的、可靠的流协议。流就是指不间断的数据结构，当应用程序采用 TCP 发送消息时，虽然可以保证发送的顺序，但还是犹如没有任何间隔的数据流发送给接收端。TCP 为提供可靠性传输，实行“顺序控制”或“重发控制”机制。此外还具备“流控制（流量控制）”、“拥塞控制”、提高网络利用率等众多功能。

UDP 是不具有可靠性的数据报协议。细微的处理它会交给上层的应用去完成。在 UDP 的情况下，虽然可以确保发送消息的大小，却不能保证消息一定会到达。因此，应用有时会根据自己的需要进行重发处理。

### 7.TCP建立连接的过程采用三次握手，已知第三次握手报文的发送序列号为555，确认序列号为6666，请问第二次握手报文的发送序列号和确认序列号分别为？

6665和555

### 8.简述tcp ip四层模型

应用层，决定向用户提供应用服务时通信的活动

传输层，提供处于网络连接中两台计算机的数据传输，著名的TCP/UDP协议都在这一层

网络层，处理流动的网络数据包，规定数据包经什么路径从出发点到达目的地

链路层，处理网络连接相关硬件工作

### 9.简述 osi七层模型

第7层：应用层

第6层：表示层

第5层：会话层

第4层：传输层

第3层：网络层

第2层：数据链路层

第1层：物理层

### 10.dns是什么 dns是哪一层协议

dns是将我们平时访问网站输入的字符串转换为IP地址的功能
DNS是应用层协议

### 11.arp是哪一层协议

arp是网络层协议

### 12.wifi是哪一层协议

wifi是物理层和数据链路层

### 13.简述cdn作用

加速用户访问速度，减少源站中心负载压力。

### 14.服务器发生close wait是在什么时候

在服务器端收到客户端请求关闭的时候，服务器端会发送回答给客户端说我收到关闭的请求了，但是数据还没发送完成，所以你等一下，当服务器端确定数据发完后，就进入准备关闭连接的状态，这两个之间就是close wait的状态。

### 15.简述syn洪攻击

SYN攻击利用的是TCP的三次握手机制，攻击端利用伪造的IP地址向被攻击端发出请求，而被攻击端发出的响应 报文将永远发送不到目的地，那么被攻击端在等待关闭这个连接的过程中消耗了资源，如果有成千上万的这种连接，主机资源将被耗尽，从而达到攻击的目的。

### 16.156.123.32.13 是哪一类ip地址

B类

### 17.主机ip地址为 193.32.5.22 掩码为 255.255.255.192 网络地址为多少,广播地址为多少

网络地址：193.32.5.0
广播地址：193.32.5.63

### 18.icmp是哪一层协议

是网络层协议

### 19.get方法和post方法的不同

区别在于一个修改资源和获取资源
get可以用于保存收藏连接地址
post请求可以把请求的内容放在报文里面

### 20.简述DOS攻击 和DDOS攻击

DoS：是Denial of Service的简称，即拒绝服务，造成DoS的攻击行为被称为DoS攻击，其目的是使计算机或网络无法提供正常的服务。最常见的DoS攻击有计算机网络带宽攻击和连通性攻击。

DDOS：分布式拒绝服务(DDoS:Distributed Denial of Service) 攻击 指借助于客 户/服务器技术，将多个计算机联合起来作为攻击平台，对一个或多个目标发动DDoS攻击，从而成倍地提高拒绝服务攻击的威力。

### 21.tcp报文头中,首部长度的作用是什么?首部长度是多少位?首部的位数为二进制表现方式,那么首部表现成十进制的最大数字是多少?tcp首部最大长度是多少,他和首都长度段有什么联系?tcp首部可选数据字段是多长?

首部长度的作用是：就是表示TCP报文段中数据部分在整个TCP报文段中的位置；32位，即4个字节。

十进制的最大数字是15

最大长度是80字节

### 22.tcp最大端口号是多少?为什么?linux系统能开启多少个端口，为什么？linux操作系统端口号和进程号的关系是什么?

65535，因为最多只有65535个。

65535个，因为0号端口无意义

### 23.tcp三次握手中 第三次握手首部中syn值是多少 为什么

0，因为ack可以携带数据段，所以不在需要消耗syn

### 24.tcp协议中 ISN是什么意思?ISN的值一定是1吗?BSD使用的ISN值的方案是什么?不同的连接ISN一样吗,如果不一样如何确定?（参考RFC 793）

是序列号，不一定是1，

### 25.tcp协议中 序列号是如何增长的,是每次加1还是随机增长还是其他方式增长?第三次握手时 ack序列号是否增加 为什么?第一次握手响应时ack序列号加多少 为什么?

每次加1，第三次握手时增加，因为第三次加1表示收到了第二次握手时的确认；第一次不加，第一次握手时时产生的随机序列号。

### 26.mss是什么?mss在什么时候确定?tcp报文最大长度理论上是多少 为什么?实际上面是多少 为什么?

mss是最大报文长度，在建立连接的时候确认，最大长度理论是65535字节，实际是65495，因为要减去IP首部20和TCP首部20.

### 27.tcp最大长度是多少,为什么?

最大长度一般是1460，因为MTU减去20-20得出1460

### 28.tcp窗口/mss大小如何确定,在什么时候,什么位置确定窗口/mss大小?

### 29.如何理解tcp的半关闭(half-close)？什么是全双工?

半关闭是指服务器还没有处理完成数据传输，所以保持连接，但是已经准备关闭。

全双工是指数据在两个方向上能同时传递，可理解为两个方向相反的独立通道

### 30.为什么握手需要三次?为什么关闭连接需要四次?

因为A对B建立连接，首先A问B可以连接吗，B说可以，然后A收到可以，知道B可以连接了，然后对B说我知道你可以连接了，这时候连接开始。

四次挥手是因为中间B回应A的关闭请求的时候，表示你等我处理完才能关，中间多了这样一个步骤，所以是4次挥手。

### 31.GBN的定时器有几个 SR的定时器有几个

GBN只有一个定时器，SR每个分组都有定时器

### 32.为什么说tcp协议是面向连接的?

因为TCP协议每一次传输需要确认，可以保证每次都传送到

### 33.GBN协议中,接收方窗口大小是多少

是不定的

### 34.GBN协议中,需要对大于当前期望收到的分组序号的序号做确认吗?SR中需要确认吗?

不需要；sr需要

### 35.TCP/IP的中文解释是什么?

传输控制协议/因特网互联协议

### 36.假设链路层MTU为 1600 那么MSS最大为多少

为1560

### 37.MSS指的是什么的大小

指最大报文段长度

### 38.计算机的端口为什么最大是65535

因为这个是由TCP/IP协议栈中的第四层运输层UDP/TCP协议决定的，在UDP/TCP协议中源端口和目的端口都只有16位，也就是说端口的取值范围为0~65535，2^16 - 1 = 65535。

### 39.a. 假定你有下列2个字节: 01011100和01100101。者两个字节之和的反码是什么?b.假定你有下列2个字节: 11011010和01100101这两个的反码和是多少?c. 1bit的差错将可能检测不出来吗?2bit呢?

是01011100和01100101

10100101和01100101

能检测出来