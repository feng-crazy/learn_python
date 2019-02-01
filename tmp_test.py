#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 13:57
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_test.py
# @Software: learn_python
# @description:


d = 56.103564949118876
if d < 13.00:
    print(d)

exit(0)

for i in range(7, 2):
    print(i)


exit(0)

data_list = [0xff, 0xfd, 0xfb, 0xf8, 0xf4, 0xf2]


for i in range(0, len(data_list)-2):
    print('0x{:02x}'.format(data_list[i]))

print('-------------------')

print('0x{:02x}'.format(data_list[-1]))
print('0x{:02x}'.format(data_list[-2]))

data_list.pop(0)

print('data_list:', ['{:02x}'.format(i) for i in data_list], len(data_list))


data_list.pop(1)

print('data_list:', ['0x{:02x}'.format(i) for i in data_list], len(data_list))

ftype = 0x0f >> 4

print('0x{:02x}'.format(ftype))

len = (0xf3 << 8) + 0xf1
print('0x{:02x}'.format(len))




