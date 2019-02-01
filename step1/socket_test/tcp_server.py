#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 16:06
# @Author  : hedengfeng
# @Site    : 
# @File    : tcp_server.py
# @Software: learn_python
# @description: 
import socket
import threading

bind_ip = ''
bind_port = 56635

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection(client_socket):
    while True:
        try:
            request = client_socket.recv(1024)
            print('Received {}'.format(request.decode()))
            client_socket.send('server ACK!'.encode() + request)
        except Exception as err:
            print('Exception :', err)
            break
    client_socket.close()


while True:
    client_sock, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()