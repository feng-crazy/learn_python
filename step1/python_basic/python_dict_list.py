#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 15:46
# @Author  : hedengfeng
# @Site    : 
# @File    : python_dict_list.py
# @Software: LearnPython
import time

test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': [1, 2, 3]}
print(test_dict)
test_list = list(test_dict.values())
print(test_list)

list_index = 0
while True:
    if list_index < len(test_list):
        print(test_list[list_index], list_index)
        list_index += 1

    else:
        list_index = 0
    time.sleep(0.5)
exit(0)

d_list = {}

print(len(d_list))


d_list['1'] = []
d_list['1'].append(1)
d_list['1'].append(1)
print(d_list)

print('2' in d_list)
print('1' in d_list)

print(len(d_list))
