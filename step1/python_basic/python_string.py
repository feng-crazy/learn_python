#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 9:54
# @Author  : hedengfeng
# @Site    : 
# @File    : python_string.py
# @Software: LearnPython
# @description:

str_tmp = '1,2,3,4,5, 6,  7'
str_list = str_tmp.split(',')
print(str_list)
str_tmp = ','.join(str_list)
print(str_tmp)

exit(0)
str_list = ['1', '2', '3']


a = 2.2356
b = 3.25649

str0 = '%lf,%lf,'%(a, b)
print(str0)

str1 = '{},{}'.format(a, b)
print(str1)

str2 = str(b)
print(str2)

str1 = 'you are sb'
print(str1, type(str1))
str2 = 'you are sb'
print(str2, type(str2))

if str1 == str2:
    print('sb is eq')


str_tmp = ''

if not str_tmp:
    print('str_tmp is null')

str_tmp = ' '
if str_tmp:
    print('str_tmp is kong')