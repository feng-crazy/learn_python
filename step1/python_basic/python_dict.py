#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 15:53
# @Author  : hedengfeng
# @Site    : 
# @File    : python_dict.py
# @Software: LearnPython
# @description: 

test_dict1 = {'E': 5}
if not test_dict1:
    print('test_dict1 not in {}')
else:
    print('test_dict1 is {}')

test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

dictMerged2 = dict(test_dict, **test_dict1)
print('dictMerged2:', dictMerged2)

test_dict.update(test_dict1)

# for key in test_dict.keys():
#     key = 'F'
# print(test_dict)
#
# for values in test_dict.values():
#     values = 1
# print(test_dict)
#
# for key in test_dict.keys():
#     test_dict[key] = 1
# print(test_dict)

# for key, value in test_dict.items():
    # if value == 4:
    #     test_dict.popitem()
    #     del test_dict[key]

p_key = test_dict.keys()
print(p_key, type(p_key))


p_list = list(test_dict.keys())
print(p_list, type(p_list))


for key in list(test_dict.keys()):
    test_dict[key] += 1
    if test_dict[key] == 4:
        del test_dict[key]

print(test_dict)


exit(0)


def funA():
    print('funA')


def funB():
    print('funB')


d_tmp = {'A': funA, 'B': funB}

d_tmp['A']()
d_tmp['B']()