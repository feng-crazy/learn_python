#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 16:06
# @Author  : hedengfeng
# @Site    : 
# @File    : object_scope.py
# @Software: LearnPython
# @description: 

class_list1 = []
class_list2 = []
class_map = {'haha': 2}

class test_class(object):
    def __init__(self):
        print('test class contruction')

    def __del__(self):
        print('test class discontruction')


def test_fun():
    test1 = test_class()
    class_list1.append(test1)
    class_map['test1'] = test1
    # class_list2.append(test1)


if __name__ == '__main__':
    test_fun()
    # class_list1.clear()
    # class_list1.pop()
    class_list1.remove(class_list1[0])
    # class_map.pop('test1')
    # class_map.clear()
    print(class_map)
    del class_map['test1']
    print(class_map)
    del class_map

    while True:
        pass
