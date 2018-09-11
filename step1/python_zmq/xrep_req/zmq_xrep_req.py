#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 18:39
# @Author  : hedengfeng
# @Site    : 
# @File    : zmq_xrep_req.py
# @Software: LearnPython

import zmq


def main():
    context = zmq.Context(1)

    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5559")

    while True:
        message = socket.recv_multipart()
        print("xrep Received request: ")
        for part in message:
            print(part)
        print("end")

        send_data = "xrep" + " rep msg:"
        socket.send_string(send_data)

    socket.close()
    context.term()


if __name__ == "__main__":
    main()