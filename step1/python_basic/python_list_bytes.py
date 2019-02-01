#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 14:22
# @Author  : hedengfeng
# @Site    : 
# @File    : python_list_bytes.py
# @Software: learn_python
# @description:

# my_list = [0xf1, 0xf2]
# my_bytes = bytes(my_list)
# print(my_bytes[0])
# print('my_bytes[0:2]:', my_bytes[0:2])
#
# print(list(my_bytes[0:2])==my_list)
# print(my_bytes[0]==0xf1)
# my_bytes.pop(0)
# print(my_bytes)

tmp_list = [i for i in range(0, 16)]
tmp_str = 'abc\0'
tmp_str_list = list(map(ord, tmp_str))
# print('tmp_str_list:', list(tmp_str_list))
tmp_list += tmp_str_list
print('tmp_list:', tmp_list)

tmp_bytes = bytes(tmp_list)
print('tmp_bytes:', tmp_bytes, len(tmp_bytes), list(tmp_bytes))

tmp_list = tmp_bytes[:-4]
print('tmp_list:', tmp_list)
print('tmp_list:', list(tmp_list))
print(tmp_bytes[-2])

tmp_name = tmp_bytes[-4:]
print('tmp_name:', tmp_name)
print('tmp_name:', tmp_name.decode())