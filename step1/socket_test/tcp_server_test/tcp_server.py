#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 9:20
# @Author  : hedengfeng
# @Site    : 
# @File    : tcp_server.py
# @Software: learn_python
# @description: 

from socketserver import BaseRequestHandler, TCPServer
from socketserver import ThreadingTCPServer
import threading


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address, threading.current_thread())
        while True:

            msg = self.request.recv(8192)
            if not msg:
                print('break')
                break

            print("recv msg: ", msg)
            self.request.send(msg)


if __name__ == '__main__':
    # serv = TCPServer(('', 20000), EchoHandler)
    # serv.serve_forever()
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


