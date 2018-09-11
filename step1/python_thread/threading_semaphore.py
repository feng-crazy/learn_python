#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 15:17
# @Author  : hedengfeng
# @Site    : 
# @File    : threading_semaphore.py
# @Software: LearnPython
# @description: 

import threading
import time
sem = threading.Semaphore(2)


def foo():
    sem.acquire()
    time.sleep(1)
    print('ok')
    sem.release()


for i in range(15):
    t = threading.Thread(target=foo, args=())
    t.start()


