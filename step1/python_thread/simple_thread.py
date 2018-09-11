#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 19:38
# @Author  : hedengfeng
# @Site    : 
# @File    : simple_thread.py
# @Software: LearnPython

import threading
import time

if __name__ == '__main__':
    def thread_loop():
        while True:
            print('thread_loop', threading.current_thread(),threading.get_ident())
            time.sleep(0.1)


    print(threading.get_ident())
    my_thread = threading.Thread(target=thread_loop, name='LoopThread')
    my_thread.start()
    while True:
        print('main thread',threading.current_thread())
        time.sleep(0.2)
        pass

