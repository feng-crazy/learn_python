#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 9:16
# @Author  : hedengfeng
# @Site    : 
# @File    : python_class2.py
# @Software: LearnPython


class FooParent(object):
    foo = 1

    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print(message, 'from Parent')

    @classmethod
    def class_bar(cls, message):
        print(cls, message, 'from Parent')

    @staticmethod
    def static_bar(value):
        FooParent.foo = value


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


def test():
    FooParent.class_bar('1')
    FooParent.class_bar('2')


if __name__ == '__main__':

    test()

    parent_foo = FooParent()
    print(FooParent.foo, parent_foo.foo)
    FooParent.foo = 2
    print(FooParent.foo, parent_foo.foo)

    parent_foo.foo = 3
    print(FooParent.foo, parent_foo.foo)

    parent_foo.static_bar(4)
    print(FooParent.foo, parent_foo.foo)
    FooParent.static_bar(5)
    print(FooParent.foo, parent_foo.foo)
    FooParent.foo = 6
    print(FooParent.foo, parent_foo.foo)

    # parent_foo.foo = 3
    # print(FooParent.foo, parent_foo.foo)

    parent_foo.hdf = 9
    print(FooParent.foo, parent_foo.hdf)




