#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 15:30
# @Author  : hedengfeng
# @Site    : 
# @File    : python_print.py
# @Software: LearnPython
# @description: 


test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B']

test_str = '{}'.format(test_dict)
print(test_str)

test_str = '%s' % test_dict
print(test_str)

test_str = '{}'.format(test_list)
print(test_str)

test_str = '%s' % test_list
print(test_str)

