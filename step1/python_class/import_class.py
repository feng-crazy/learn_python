#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 10:49
# @Author  : hedengfeng
# @Site    : 
# @File    : import_class.py
# @Software: LearnPython
# @description:
import time

tmp = 0
while True:
    tmp += 1
    print('tmp',  tmp)
    time.sleep(0.5)
    if tmp == 50:
        break


class ImportClass(object):
    def __init__(self):
        print('ImportClass init')

