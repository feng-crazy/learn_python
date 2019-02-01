#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 11:30
# @Author  : hedengfeng
# @Site    : 
# @File    : socket_direct.py
# @Software: learn_python
# @description: 
import time
from random import choice
from random import randrange

import zmq

if __name__ == "__main__":
    stock_symbols = ['RAX', 'EMC', 'GOOG', 'AAPL', 'RHAT', 'AMZN']

    context = zmq.Context()
    socket = context.socket(zmq.STREAM)
    socket.setsockopt(zmq.STREAM_NOTIFY, 1)
    socket.setsockopt(zmq.LINGER, 0)
    socket.bind("tcp://127.0.0.1:49999")

    my_id = socket.getsockopt(zmq.IDENTITY)
    hwm = socket.getsockopt(zmq.SNDHWM)
    print("my_id:", my_id)
    print('hwm:', hwm)

    # def my_recv():
    #     data = socket.recv()
    #     return data
    #
    def my_send(data):
        # socket.send(my_id, zmq.SNDMORE)
        socket.send(data)

    while True:
        time.sleep(1)

        if socket.poll(1000, zmq.POLLIN):
            data = socket.recv()
            print("Recving Message:}", data)

            # pick a random stock symbol
            stock_symbol = choice(stock_symbols)
            # set a random stock price
            stock_price = randrange(1, 100)

            # compose the message
            msg = "{0} {1}".format(stock_symbol, stock_price)

            print("Sending Message: {0}".format(msg))
            my_send(msg.encode())
            # socket.send(msg.encode())

