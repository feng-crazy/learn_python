#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 14:19
# @Author  : hedengfeng
# @Site    : 
# @File    : python_file_op.py
# @Software: LearnPython
# @description:
import os
# from python_class import python_class3

print('os.getcwd()=', os.getcwd())
print(os.path.realpath('.'))

# rootdir = os.path.realpath('.')
rootdir = '.'
files = []
file_list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
print(file_list)

for i in range(0, len(file_list)):
    path = os.path.join(rootdir, file_list[i])
    if os.path.isfile(path):
        # 你想对文件的操作
        files.append(path)
print(files)
exit(0)

for file in file_list:
    print(file, type(file))
    files.append(file)

print(files)

for i in range(0, len(file_list)):
    path = os.path.join(rootdir, file_list[i])
    if os.path.isfile(path):
        # 你想对文件的操作
        files.append(path)

