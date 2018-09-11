#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 16:17
# @Author  : hedengfeng
# @Site    : 
# @File    : python_tmp_test.py
# @Software: LearnPython
# @description:
import time
import traceback

test_value = None
test_value1 = test_value

tmp_list = [0x55, 0x5a, 0x55, 0x04, 16, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0xfe, 0xff]
# print('{:x}'.format(tmp_list))

for i in tmp_list:
    print('{:02x}'.format(i), end=',')
print('')

for i in tmp_list:
    print(hex(i), end=',')
print('')

# tmp_str = hex(tmp_list[3])
tmp_str = '{:02x}'.format(tmp_list[3])
print('tmp_str:', tmp_str, type(tmp_str))
exit(0)


flag = True

tmp_value = 0


def funA():
    if flag is True:
        print('tmp_value:', tmp_value)
        # tmp_value = 1
        return None

    return ''


tmp = funA()
print('tmp:', tmp, type(tmp))

if tmp is None:
    print('tmp is None')

print('tmp_value:', tmp_value)

for i in range(0, 10):
    tmp_value += 1

print('tmp_value:', tmp_value)

while funA() is None:
    print('none')
    time.sleep(1)

exit(0)


def fooE():
    tmp = 1 / 0
    print(tmp)
    # traceback.print_stack()
    # print(type(traceback.extract_stack()))
    # print(type(traceback.format_stack()))


def fooD():
    fooE()


def fooC():
    fooD()


def fooB():
    fooC()


def fooA():
    try:
        fooB()
    except Exception as err:
        # traceback.print_stack()
        # print(err)
        # traceback.format_exc()
        print(traceback.format_exc())


fooA()
