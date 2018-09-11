#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import socket, sys
from socket import *
import time, threading
import sys
import signal

HOST = ''
PORT = 57825
BUFSIZE = 1024

ADDR = (HOST, PORT)
dest = ('<broadcast>', PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

over_flag = False
scan = 'scan'

try:
    while True:
        data = 'my is client'
        udpCliSock.sendto(data.encode(), dest)
        data, addr = udpCliSock.recvfrom(BUFSIZE)
        print('recvfrom:', data, addr)
        time.sleep(2)

except Exception as e:
    print(str(e))

udpCliSock.close()
