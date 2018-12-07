#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:17
# @Author  : hedengfeng
# @Site    : 
# @File    : calc_radian.py
# @Software: learn_python
# @description:

import math

PI = 3.1415926


def angle_to_radian(angle):
    radian = (PI / 180.00) * angle
    print('radian:', radian)
    return radian


def calc_points_radian(x1, y1, x2, y2):
    radian = math.atan2((y2 - y1), (x2 - x1))
    if radian < 0.0:
        radian = PI - radian
    print('radian:', radian)
    return radian


angle_to_radian(90)
angle_to_radian(180)
angle_to_radian(270)

print('---------------------')

calc_points_radian(0, 0, 0, 1)
calc_points_radian(0, 0, -1, 0)
calc_points_radian(0, 0, 0, -1)
