#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 14:57
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_test1.py
# @Software: learn_python
# @description:


bases_data = [0xAA, 0xF6, 0x02, 0xFF, 0x64, 0x65, 0x7E]


def judgeCheckSum(data):
    check_sum = data[-2]
    calc_check_sum = 0
    for i in range(2, 3 + data[2]):
        calc_check_sum += data[i]
        print(data[i])
    calc_check_sum = calc_check_sum & 0xff
    if check_sum != calc_check_sum:
        return False
    return True


print(judgeCheckSum(bases_data))

exit(0)

check_sum = 0x123456789abcdef

result = check_sum & 0xffff

print('{:02x}'.format(result))


data_list = [0xff, 0xfd, 0xfb, 0xf8, 0xf4, 0xf2]

tmp = data_list[-3:-2][0]
print('{:02x}'.format(tmp))

data_list.clear()
print(data_list, len(data_list))