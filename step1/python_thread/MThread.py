#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 19:41
# @Author  : hedengfeng
# @Site    : 
# @File    : MThread.py
# @Software: LearnPython

import threading
import time


class MThread:

    def __init__(self, child_thread):
        print(child_thread)
        self.run_flag = False
        self.thread = threading.Thread(target=self.thread_run, args=(child_thread, ), name='LoopThread')
        self.thread.start()

    @classmethod
    def handle_message(cls):
        print('handle_message')

    def thread_run(self, child_thread):
        child_thread.setup_thread()
        while True:
            print('thread_run', self.run_flag, threading.current_thread())
            self.handle_message()
            if self.run_flag is True:
                child_thread.main_loop()
            else:
                pass
            time.sleep(1)

    def start(self):
        print('start')
        if self.run_flag is not True:
            self.run_flag = True

    def stop(self):
        if self.run_flag is True:
            self.run_flag = False


class ThreadA(MThread):
    def __init__(self):
        super(ThreadA, self).__init__(self)
        self.thread_name = 'ThreadA'

    def main_loop(self):
        print('main_loog ThreadA')

    def setup_thread(self):
        print('setup_thread...........')


if __name__ == '__main__':
    thread_a = ThreadA()
    thread_a.start()

    # time.sleep(5)
    # thread_a.stop()
    #
    # time.sleep(5)
    # thread_a.start()

    while True:
        print('main threading', threading.current_thread())
        time.sleep(1)
        pass

