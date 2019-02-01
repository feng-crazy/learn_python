#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 17:09
# @Author  : hedengfeng
# @Site    : 
# @File    : inner _class_test.py
# @Software: learn_python
# @description: 


class Circle(object):
    def __init__(self):
        """"""

    class Draw(object):
        def __init__(self):
            """"""
            self.value = 100


tmp = Circle.Draw()
print(tmp.value)