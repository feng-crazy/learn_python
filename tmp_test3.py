#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 15:15
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_test3.py
# @Software: learn_python
# @description:
import math

bases_loc_info = [['100', ' 200'], ['300', ' 400'], ['250', ' 250']]


def calcCoverBaseCount(x, y):
    count = 0
    for tmp in bases_loc_info:
        x_len = float(tmp[0]) - x
        y_len = float(tmp[1]) - y
        d = math.sqrt((x_len ** 2) + (y_len ** 2))
        print(d)
        if d < 10.00:
            count += 1
    return count


calcCoverBaseCount(0, 0)