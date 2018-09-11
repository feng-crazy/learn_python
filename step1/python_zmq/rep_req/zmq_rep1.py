#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 15:24
# @Author  : hedengfeng
# @Site    : 
# @File    : zmq_rep1.py
# @Software: LearnPython

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.setsockopt(zmq.SNDTIMEO, 3000)
socket.bind("tcp://*:5559")
# socket.connect("tcp://localhost:5559")

while True:
    if socket.poll(20, zmq.POLLIN):
        print('recv begin')
        message = socket.recv_string()
        print("Received request: ", message)
        time.sleep(1)

        print('send begin')
        socket.send_multipart([("World1 {}".format(message)).encode()])
        print("send reply World1: ", message)
        time.sleep(1)

