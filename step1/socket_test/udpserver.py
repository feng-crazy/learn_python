#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
import time
from socket import *
from time import ctime

HOST = ''
PORT = 57825
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
udpSerSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# udpSerSock.settimeout(3)
udpSerSock.bind(ADDR)

while True:
    try:
        print('wating for message...', time.ctime())
        data, addr = udpSerSock.recvfrom(BUFSIZE)
        print('recvfrom:', data, addr, type(addr), addr[0], type(addr[0]))
        udpSerSock.sendto(b'my is server', addr)
        # print('...received from and retuned to:', addr)
    except timeout as err:
        print("exception:", err, time.ctime())


udpSerSock.close()
