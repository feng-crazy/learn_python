#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 15:06
# @Author  : hedengfeng
# @Site    : 
# @File    : threading_lock.py
# @Software: LearnPython
# @description:
import threading
import time


def foo():
    rlock.acquire()
    print('func foo ClockA lock')
    rlock.acquire()
    print('func foo ClockB lock')
    rlock.release()
    rlock.release()


def bar():
    rlock.acquire()
    print('func bar ClockB lock')
    time.sleep(2)
    rlock.acquire()
    print('func bar ClockA lock')
    rlock.release()
    rlock.release()


def run():
    foo()
    bar()


# RLock本身有一个计数器，如果碰到acquire，那么计数器+1
# 如果计数器大于0，那么其他线程无法查收，如果碰到release，计数器-1
rlock = threading.RLock()


for i in range(10):
    t=threading.Thread(target=run, args=())
    t.start()

# count = 0
# l = []
#
# def sub():
#     global count
#
#     '''线程的公共数据  下'''
#     temp = count
#     time.sleep(0.001)    #大量的io操作
#     count = temp+1
#     '''线程的公共数据  上'''
#
#     time.sleep(2)
#
#
# for i in range(100):
#     t = threading.Thread(target=sub, args=())
#     t.start()
#     l.append(t)
# for t in l:
#     t.join()
# print(count)