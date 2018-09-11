#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 15:54
# @Author  : hedengfeng
# @Site    : 
# @File    : python_decode.py
# @Software: LearnPython
# @description:
import sys
import time

print(sys.maxsize)


b_tmp = b'\x08\x80\x01\x10\x01'

b_str = str(b_tmp)
print('b_str:', b_str)

b_ecode = b_str.encode()
print('b_ecode:', b_ecode)

b_null = str(time.time()).encode()
print(b_null)