#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 14:58
# @Author  : hedengfeng
# @Site    : 
# @File    : wrapper_test.py
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


@cache
def rectangle_area(length, width):
    print('A')
    return length * width


print('begin')
print(rectangle_area(2, 3))

print('again 1')
print(rectangle_area(2, 3))


print('again 2')
print(rectangle_area(2, 4))