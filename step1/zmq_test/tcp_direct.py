#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 13:54
# @Author  : hedengfeng
# @Site    : 
# @File    : tcp_client.py
# @Software: learn_python
# @description: 
import socket, select


address = ('127.0.0.1', 49999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
#
# p = select.poll()
# p.register(s)

while True:
    data = b'123456'
    s.send(b'')
    s.send(data)

    data = s.recv(512)
    print('the data received is:', data)




s.close()