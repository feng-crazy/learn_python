#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 17:34
# @Author  : hedengfeng
# @Site    : 
# @File    : python_quyu.py
# @Software: LearnPython
# @description:
import time

monitor_count = 0
while True:
    if monitor_count % 5 != 0:  # 5秒监视一次
        print('monitor_count:', monitor_count)
    else:
        print('success count ')
    monitor_count += 1
    time.sleep(0.1)