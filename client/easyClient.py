from socket import socket

s = socket(socket.AF_NET,socket.SOCK_STREAM)
s.connect(("www.baidu.com",80))
