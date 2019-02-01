#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 16:00
# @Author  : hedengfeng
# @Site    : 
# @File    : list_class_test.py
# @Software: learn_python
# @description: 


class MyTest(object):
    def __init__(self, age, size):
        self.age = age
        self.size = size


tmp_list = []

test1 = MyTest(18, 18)
tmp_list.append(test1)
test2 = MyTest(19, 19)
tmp_list.append(test2)
print(tmp_list[1].size, tmp_list[1].age)

test3 = tmp_list[1]
test3.age = 20
test3.size = 20
print(tmp_list[1].size, tmp_list[1].age)


tmp_list1 = [1, 2]
print(tmp_list1)
test_v = tmp_list[1]
test_v = 3
print(tmp_list1)


