#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 15:08
# @Author  : hedengfeng
# @Site    : 
# @File    : object_list.py
# @Software: learn_python
# @description: 


class TestObject(object):
    def __init__(self, age, height):
        self.age = age
        self.height = height


test1 = TestObject(21, 165)
test2 = TestObject(22, 166)
test3 = TestObject(23, 167)
test4 = TestObject(24, 168)

test_list = [test1, test2, test3, test4]

print(test_list[1].age, test_list[1].height)

test_object = None

for i in test_list:
    if i.age == 22:
        test_object = i

test_object.age = 18

print(test_list[1].age, test_list[1].height)


test_list = [1, 2, 2, 4]

for i in test_list.copy():
    if i == 2:
        test_list.remove(i)

print(test_list)

test_list = [1, 2, 2, 4]
it = iter(test_list)
while True:
    try:
        # 获得下一个值:
        x = next(it)
        if x == 2:
            test_list.remove(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

print(test_list)