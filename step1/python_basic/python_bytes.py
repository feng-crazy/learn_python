#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 14:26
# @Author  : hedengfeng
# @Site    : 
# @File    : python_bytes.py
# @Software: LearnPython
# @description:

status = False
print(status)
cmd_data = [0x00 for x in range(0, 22)]
cmd_data[0:3] = [0, 1, 3]
cmd_data = bytes(cmd_data)
print(len(cmd_data), cmd_data, type(cmd_data))

exit(0)


b = bytes([0, 1, 2, 3, 4, 5, 6, 7])
print(b)
str1 = '1234566'
print(bytes(str1, encoding='utf-8'))
# b = bytes(b'0xf80xf40xf2')
b = bytes([0xf8, 0xf4, 0xf2])
print(b)
print(bytes(b))

# b = bytes(b'0123456')
print(len(b))
print(b[0])

print('0x{:x}'.format(b[0]))

print(str(b))

b = bytes([1, 2, 255])
print(len(b))

print(b)

b = bytes([0xf8, 0xf4, 0x11])
print(len(b))

print(b)

type = 0x11

if b[2] == type:
    print('hahahha')

type = type & 0x0f
print('%02x' % type)
print('%04X' % 0xFF)

