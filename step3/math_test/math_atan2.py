#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-09 14:07
# @Author  : hedengfeng
# @Site    : 
# @File    : math_atan2.py
# @Software: learn_python
# @description:
import math

math.fabs()

print(8.432 // 2)
print(8.432 % 2)

print(-8.432 // -2)
print(-8.432 % -2)
print("/////////////////////")

PI = math.pi
print(math.degrees(math.atan2(0, 4)))
print("*******************")

print(math.degrees(math.atan2(4, 0)))
print("*******************")

print(math.degrees(math.atan2(0, -4)))
print("*******************")

print(math.degrees(PI-math.atan2(-4, 0)))
print(math.atan2(-4, 0))
print("*******************")

print("------------------------")
print(math.degrees(math.atan2(0, 0)))
print(math.atan2(0, 0))
print("++++++++++++++++++++")

print(math.atan2(4, 4))
print(math.degrees(math.atan2(4, 4)))

print("++++++++++++++++++++")
print(math.atan2(4, -4))
print(math.degrees(math.atan2(4,-4)))
print("++++++++++++++++++++")

print(math.atan2(-4, -4))
print(math.degrees(math.atan2(-4, -4)))
print(math.degrees(2*PI + math.atan2(-4, -4)))

print("++++++++++++++++++++")

print(math.atan2(-4, 4))
print(math.degrees(math.atan2(-4, 4)))
print(math.degrees(2*PI + math.atan2(-4, 4)))