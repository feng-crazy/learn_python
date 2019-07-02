#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-13 20:06
# @Author  : hedengfeng
# @Site    : 
# @File    : format_output.py
# @Software: learn_python
# @description:
import csv

tmp_b = bytes(b'\x01\x0212')
data = [hex(x) for x in tmp_b]
print(data)
print(data[0], type(data[0]))
print(data[3], type(data[3]))
print(tmp_b[0], type(tmp_b[0]))
print(tmp_b[3], type(tmp_b[3]))

print('{:02x}'.format(tmp_b[3]))

str_tmp = ['{:02x}'.format(x) for x in tmp_b]
print(str_tmp)

cvs_tmp_list = ["csv:"]
cvs_tmp_list.extend(str_tmp)

cvs_tmp_list.append(68)
cvs_tmp_list.append('8 58 12 11')

file_ptr = open('format_test.csv', 'w')
writer = csv.writer(file_ptr)
writer.writerow(cvs_tmp_list)
file_ptr.close()

