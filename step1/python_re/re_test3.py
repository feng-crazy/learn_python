#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 11:02
# @Author  : hedengfeng
# @Site    : 
# @File    : re_test3.py
# @Software: learn_python
# @description: 

import re

str = "cdac = 23b  addr = 34"

print(re.findall(r"ac = (\d+)b", str))
print(re.findall(r"addr = (\d+)", str))

# print(re.findall(r"a(\d+)", str, re.M))


tmp_str = "[683937]<V> ExtractAddrFromString : addr = 10\n================================= cmd line : get bs info =================================\ngroup : 0 , addr : 10 \nchip id : 0x48 0xff 0x71 0x6 0x77 0x88 0x48 0x57 0x47 0x56 0x18 0x67 \nname : bs-32 n \nled status : on \nmotor status : on \n"
print(re.findall(r'addr = (\d+)', tmp_str))

print(re.findall(r"\d+", tmp_str))
print(re.findall(r"addr = (\d+.)", tmp_str))
print(re.findall(r"group : (\d+)", tmp_str))