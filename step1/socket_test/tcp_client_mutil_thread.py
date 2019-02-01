#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 11:18
# @Author  : hedengfeng
# @Site    : 
# @File    : tcp_client_mutil_thread.py
# @Software: learn_python
# @description: 
import socket
import threading
import time

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 9999))

def thread1_run(client):
    while True:
        # send some data (in this case a HTTP GET request)
        send_data = ('my is client1: {}'.format(time.time())).encode()
        client.sendall(send_data)

        # receive the response data (4096 is recommended buffer size)
        response = client.recv(4096)

        print('client1', response)

        time.sleep(1)


def thread2_run(client):
    while True:
        # send some data (in this case a HTTP GET request)
        send_data = ('my is client2: {}'.format(time.time())).encode()
        client.sendall(send_data)

        # receive the response data (4096 is recommended buffer size)
        response = client.recv(4096)

        print('client2', response)

        time.sleep(1)


thread1 = threading.Thread(target=thread1_run, args=(client,), name='thread1')
thread2 = threading.Thread(target=thread2_run, args=(client,), name='thread2')

thread1.start()
thread2.start()

while True:
    pass


