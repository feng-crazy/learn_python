#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 15:23
# @Author  : hedengfeng
# @Site    : 
# @File    : wrapper_test1.py
# @Software: learn_python
# @description: 


def cache(func):
    data = {}
    print('1')

    def wrapper(*args, **kwargs):
        print('2')
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        print(f'{func.__name__}-{str(args)}-{str(kwargs)})')
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result

    print('3')
    return wrapper


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @cache
    def area(self):
        return self.length * self.width


print('begin')
print(Rectangle(2, 3).area())

print('again 1')
print(Rectangle(2, 3).area())


print('again 2')
print(Rectangle(2, 4).area())