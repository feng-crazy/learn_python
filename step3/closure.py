#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:10
# @Author  : hedengfeng
# @Site    : 
# @File    : closure.py
# @Software: learn_python
# @description: 


def outer():
    x = 1
    y = 2

    def inner():
        print("x= %s" %x)
        print("y= %s" %y)

    print(inner.__closure__)
    return inner


func = outer()

func()