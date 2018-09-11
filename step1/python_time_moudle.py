#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 18:41
# @Author  : hedengfeng
# @Site    : 
# @File    : python_time_moudle.py
# @Software: LearnPython
# @description: 

import time

print(time.time())

print(time.asctime())

print((time.clock()))

print(time.ctime())

print(time.localtime())

print(time.localtime(1531997055.291098))

# Thu Jul 19 18:44:15 2018
# time.struct_time(tm_year=2018, tm_mon=7, tm_mday=19, tm_hour=18, tm_min=44, tm_sec=15, tm_wday=3, tm_yday=200, tm_isdst=0)
