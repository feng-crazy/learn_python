#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 14:17
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_list_dict.py
# @Software: learn_python
# @description: 


tmp_map = {}
tmp_map['id'] = '1231354'
print(tmp_map)

exit(0)

tmp_list = [1, 2, 3, 4, 5, 6, 7, 8]
# tmp_list = []
# tmp_list.insert(0, 9)
# print(tmp_list)
# exit(0)
# for item in tmp_list:
#     print(item)
#     if item == 2:
#         tmp_list.remove(item)
# print(tmp_list)

tmp_dict = {}

for i in tmp_list:
    tmp_dict[i] = 1

print(tmp_dict)

for i in tmp_list:
    tmp_dict[i] += 1

print(tmp_dict)

exit(0)

for key in list(tmp_dict.keys()):
    # print(key, value)
    if tmp_dict[key]==0:
        tmp_dict.pop(key)
        tmp_list.remove(key)

# for item in tmp_dict:
#     print(item)
#     if tmp_dict[item]==0:
#         tmp_dict.pop(item)
#         tmp_list.remove(item)

print(tmp_list)
print(tmp_dict)

tmp_list.insert(3, 5)
tmp_dict[5] = 1
print(tmp_list)
print(tmp_dict)

key_list = list(tmp_dict.keys())
print('key_list:', key_list)
key_list.sort()
print('key_list:', key_list)



