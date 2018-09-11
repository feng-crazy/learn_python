#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 15:24
# @Author  : hedengfeng
# @Site    : 
# @File    : zmq_req1.py
# @Software: LearnPython
import time

import zmq

context = zmq.Context()

zmq_point = "tcp://localhost:5559"


def connect():
    global socket
    socket = context.socket(zmq.REQ)
    socket.setsockopt(zmq.REQ_CORRELATE, 1)
    socket.setsockopt(zmq.REQ_RELAXED, 1)
    # socket.setsockopt(zmq.RCVTIMEO, 3000)
    socket.connect(zmq_point)


def reconnect():
    global socket
    socket.disconnect(zmq_point)
    socket.close(linger=0)
    connect()


request = 0

connect()

while True:
    if socket.poll(20, zmq.POLLOUT):
        try:
            request = request + 1
            print('send begin')
            socket.send_multipart(["Hello:{}".format(request).encode()])
            print("send req hello:", request)

            print('recv begin')
            message = socket.recv_string()
            print("Received reply: ", message)
        except zmq.error.Again as err:
            print('Exception: ', err)
            reconnect()
    time.sleep(1)
