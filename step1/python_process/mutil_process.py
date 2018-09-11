#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 9:54
# @Author  : hedengfeng
# @Site    : 
# @File    : mutil_process.py
# @Software: LearnPython
# @description:
import os
import threading
import time
from multiprocessing import Process


def create_sub_process():
    count = 0
    while True:
        print('sub process count:', count)
        if count == 5:
            pass
            # os._exit(0)
        count += 1
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=create_sub_process, args=())
    # p = threading.Thread(target=create_sub_process, args=())
    p.start()

    print('sub process:', p.pid)

    count = 0
    while True:
        print('main process count:', count)
        if count == 5:
            p.terminate()
            print('os._exit')
        if count == 8:
            break
        count += 1
        time.sleep(1)
