#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 15:12
# @Author  : hedengfeng
# @Site    : 
# @File    : wrapper_class_test.py
# @Software: learn_python
# @description: 


class Cache:
    def __init__(self, func):
        print('Cache construct')
        self.func = func
        self.data = {}

    def __call__(self, *args, **kwargs):
        print('Cache __call__')
        func = self.func
        data = self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result


@Cache
def rectangle_area(length, width):
    print('A')
    return length * width


print('begin')
print(rectangle_area(2, 3))

print('again 1')
print(rectangle_area(2, 3))


print('again 2')
print(rectangle_area(2, 4))