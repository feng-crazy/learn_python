#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 10:03
# @Author  : hedengfeng
# @Site    : 
# @File    : re_test2.py
# @Software: learn_python
# @description:

import re

str_tmp = "|==========================================================================\n| group : 10 , addr : 1 \n| chip id : 48 ff 6c 06 77 88 48 57 28 57 18 67 \n| bs name : bs-1 \n| leds status : on \n| motor status : on \n|========================================================================== \n|==========================================================================\n| group : 10 , addr : 2 \n| chip id : 48 ff 6b 06 77 88 48 57 36 06 19 67 \n| bs name : bsname-2 \n| leds status : on \n| motor status : on \n|========================================================================== \n|==========================================================================\n| group : 10 , addr : 3 \n| chip id : 48 ff 73 06 77 88 48 57 59 34 18 67 \n| bs name : host-3 \n| leds status : on \n| motor status : on \n|========================================================================== "


print(re.findall(r'addr : (\d+)', str_tmp, re.M))
print(re.findall(r"addr : (\d+)", str_tmp, re.S))
print(re.findall(r"addr : (\d+)", str_tmp))
