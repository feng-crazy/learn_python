#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-05 15:02
# @Author  : hedengfeng
# @Site    : 
# @File    : decimal_test.py
# @Software: learn_python
# @description:

from decimal import *

tmp_value = Decimal(2.2)*Decimal(3)
print(tmp_value)
print(Decimal(tmp_value))