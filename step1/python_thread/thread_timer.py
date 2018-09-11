#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 16:21
# @Author  : hedengfeng
# @Site    : 
# @File    : thread_timer.py
# @Software: LearnPython

import threading
import time
import sched

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
# import time
#
# try:
#     import asyncio
# except ImportError:
#     import trollius as asyncio
#
# # scheduler = BackgroundScheduler()
# # scheduler = AsyncIOScheduler()
# scheduler = BlockingScheduler()
#
#
# def job1(arg):
#     print('job1  threading: ', threading.get_ident(), threading.current_thread())
#     # print("job1 %s: 执行任务 %s" % (time.asctime(), arg))
#
#
# def job2(arg):
#     print('job2  threading: ', threading.get_ident(), threading.current_thread())
#     # print("job2%s: 执行任务 %s" % (time.asctime(), arg))
#
#
# scheduler.add_job(job1, 'interval', seconds=0.5, args=('haha', ))
# scheduler.add_job(job2, 'interval', seconds=1, args=('hehe', ))
# scheduler.start()
#
# try:
#     asyncio.get_event_loop().run_forever()
# except (KeyboardInterrupt, SystemExit):
#     pass
#
# while True:
#     print('main  threading: ', threading.get_ident(), threading.current_thread())
#     # print(time.time())
#     time.sleep(2)


class client(object):
    """dada"""

    def __del__(self):
        """"""

    def handle(self):
        print('client handle...', self)


# 被调度触发的函数
def main_task_handle(msg):
    print(threading.current_thread())
    print("Current Time:", time.time(), 'msg:', type(msg))
    msg.handle()
    s = sched.scheduler(time.time, time.sleep)  # scheduler的两个参数用法复杂,可以不做任何更改
    s.enter(1, 2, main_task_handle, (msg,))
    s.run(blocking=True)


if __name__ == "__main__":
    print(threading.current_thread(), time.time())
    msg = 'haha start'
    client1 = client()
    print(client1)
    main_task_handle(client1)
    while True:
        a = 1
        print(a, ':0000000000000000000000000000000000')
        time.sleep(1)


# def hello(name):
#     print("hello %s\n" % name)
#     print(threading.current_thread())
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()
#
#
# if __name__ == "__main__":
#     print(threading.current_thread())
#     timer = threading.Timer(2.0, hello, ["Hawk"])
#     timer.start()