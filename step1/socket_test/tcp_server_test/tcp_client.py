#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 9:21
# @Author  : hedengfeng
# @Site    : 
# @File    : tcp_client.py
# @Software: learn_python
# @description:
import time
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)

ret = s.connect(('localhost', 20000))
print("ret:", ret)


while True:
    ret = s.send(b'World')
    print("ret:", ret)

    ret = s.recv(8192)
    print("ret:", ret)

    time.sleep(1)