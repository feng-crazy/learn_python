# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""

# 首先获得Iterator对象:
import time
from typing import Iterator
from typing import Iterable


class it_obj(object):
    def __init__(self, value):
        self._value = value

    def print_obj_value(self):
        print(self._value)


obj1 = it_obj(1)
obj2 = it_obj(2)
obj3 = it_obj(3)
obj4 = it_obj(4)
obj5 = it_obj('嘿嘿嘿')
test_dict = {'A': obj1, 'B': obj2, 'C': obj3, 'D': obj4, 'E': obj5}
test_dict.__getitem__('E').print_obj_value()
# test_dict[4].print_obj_value()
# exit(0)
# print(isinstance(test_dict, Iterable))
# print(isinstance(test_dict, Iterator))
# print(isinstance(test_dict.values(), Iterable))
# print(isinstance(test_dict.values(), Iterator))

it = iter(test_dict.values())
# print(it[4])
while True:
    try:
        x = next(it)
        print(x.print_obj_value(), type(x))
        if x == obj5:
            print('.....................')
    except StopIteration:
        # 遇到StopIteration就退出循环
        it = iter(test_dict.values())
    except RuntimeError:
        it = iter(test_dict.values())

    time.sleep(1)

it = iter(test_dict.keys())
print(it)
while True:
    try:
        x = next(it)
        print(x, type(x))
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

test_dict['F'] = it_obj('哈哈哈')
exit(0)

print(isinstance([], Iterable))

it = iter([1, 2, 3, 4, 5])
print(isinstance(it, Iterator))
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(isinstance(x, int))
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
