#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 14:54
# @Author  : hedengfeng
# @Site    : 
# @File    : re_test1.py
# @Software: learn_python
# @description: 

import re
str1 = 'set addr 8'
str2 = 'set addr 9 10'
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall(str1)
print(result1[-1], type(result1[-1]))

if result1[-1] == '8':
    print('haha')

result2 = pattern.findall(str2)
print(result2[-1])
print(type(result2[-1]))


exit(0)

tmp_list = [1, 2, 3, 4]

tmp_str = 'set group '

for i in range(0, len(tmp_list)):
    print(str(tmp_list[i]))
    tmp_str = tmp_str + '{},'.format(tmp_list[i])

tmp_str = tmp_str[0:len(tmp_str)-1]
print(tmp_str)

print('{},{}'.format(tmp_list, 'haha'))
