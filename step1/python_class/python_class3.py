#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 18:26
# @Author  : hedengfeng
# @Site    : 
# @File    : python_class3.py
# @Software: LearnPython
import os


class arg_test(object):
     def __init__(self):
         self.arg1 = 1


def modify_arg(arg):
    arg.arg1 = 2

test = arg_test()
modify_arg(test)
print(test.arg1)

print('os.getcwd()=', os.getcwd())
print(os.path.realpath('.'))








# import python_class2
#
#
# python_class2.test()
# python_class2.FooParent.class_bar('2')