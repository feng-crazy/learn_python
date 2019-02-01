#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 11:03
# @Author  : hedengfeng
# @Site    : 
# @File    : list_index_test.py
# @Software: learn_python
# @description: 


list1 = [1, 2, 3, 4, 5, 6, 7]

list2 = [3, 4, 5, 6, 7, 8, 9]

index = list1.index(list2[0])

for i in range(0, index):
    list1.pop(0)

print(list1)
print(list2)

