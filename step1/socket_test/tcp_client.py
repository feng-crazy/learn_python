#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 16:05
# @Author  : hedengfeng
# @Site    : 
# @File    : tcp_client.py
# @Software: learn_python
# @description: 


import socket
import time

hostname, sld, tld, port = 'www', 'integralist', 'co.uk', 80
target = '{}.{}.{}'.format(hostname, sld, tld)

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('192.168.0.149', 56635))

while True:
    # send some data (in this case a HTTP GET request)
    # receive the response data (4096 is recommended buffer size)
    request = client.recv(4096)

    print('request:', request, time.time())

    send_data = b'\xf1\xf2\xc2\x00\x02\xa5'
    ret = client.sendall(send_data)
    print('sendall bytes:', ret)

