#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 10:49
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_class.py
# @Software: LearnPython
# @description: 

from import_class import ImportClass

class parent:
    name = 'parent'

    def getName(self):
        print(self.name)

    class child:
        def getName(self):
            return parent.name


if __name__ == '__main__':
    child = parent.child()
    ret = child.getName()
    print(ret)

