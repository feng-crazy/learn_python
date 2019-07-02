#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 17:03
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_test2.py
# @Software: learn_python
# @description:


tmp_bytes = b'\x02\xffde~\xaa\xf7\x03'
tmp_bytes_list = list(tmp_bytes)
print('tmp_bytes_list:', tmp_bytes_list, type(tmp_bytes_list[2]))
# print('{:02x}'.format(tmp_bytes_list))

tmp_list = [0x01, 0x02, 0x03, 0x04, 0xff] + [0xf8, 0xf4, 0xf2, 0xf0]
print(tmp_list)
print(str(tmp_list))

tmp_byte = bytes(tmp_list)
print(tmp_byte)

tmp2_list = list(tmp_byte)
print('tmp2_list:', tmp2_list)
print('tmp2_list index :', type(tmp2_list[4]))


tmp_str = '5678'
print(tmp_str.encode())
# print(bytes(tmp_str))
tmp3_list = list(tmp_str)
print(tmp3_list)

exit(0)

array_tmp = b'fff8f4f2'
print('array_tmp:', len(array_tmp), list(array_tmp), array_tmp[-1])
de_tmp = array_tmp.decode()
print(de_tmp, type(de_tmp))

exit(0)

x = ['a', 'b', 'c', 'd']
y = ['b', 'c']
for i in x:
    print('i', i)
    if i in y:
        x.remove(i)
        print(x)
print(x)

