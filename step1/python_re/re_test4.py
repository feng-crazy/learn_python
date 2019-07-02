#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-14 15:43
# @Author  : hedengfeng
# @Site    : 
# @File    : re_test4.py
# @Software: learn_python
# @description: 
import re

bases_addr_list = []

result = 'ls all\r\r\n\r\n# \r\n# \r\n|====================================================================================================================================\r\n| group :   3 , addr :  95 , chip id : 48 ff 6f 06 77 88 48 57 46 55 18 67 , leds status : off , motor status : on , bs name : bs-95 \r\n|\r\n| group :   0 , addr :  96 , chip id : 48 ff 6e 06 77 88 48 57 35 06 19 67 , leds status : off, motor status : on , bs name : bs-96 \r\n|\r\n| group :   0 , addr :  97 , chip id : 48 ff 6d 06 77 88 48 57 32 07 19 67 , leds status : off , motor status : on , bs name : bs-97 \r\n|\r\n| group :   0 , addr :  98 , chip id : 48 ff 67 06 77 88 48 57 39 54 18 67 , leds status : off , motor status : on , bs name : bs-98 \r\n|\r\n| group :   3 , addr :  99 , chip id : 48 ff 71 06 77 88 48 57 49 56 18 67 , leds status : off , motor status : on , bs name : bs-99 \r\n|\r\n| group :   0 , addr : 100 , chip id : 48 ff 69 06 77 88 48 57 50 55 18 67 , leds status : off , motor status : on , bs name : bs-100 \r\n|\r\n| group :   0 , addr : 101 , chip id : 48 ff 69 06 77 88 48 57 19 54 18 67 , leds status : off , motor status : on , bs name : bs-101 \r\n|\r\n| group :   0 , addr : 131 , chip id : 48 ff 6c 06 77 88 48 57 19 55 18 67 , leds status : off , motor status : on , bs name : bs-102 \r\n|\r\n|====================================================================================================================================\r\n'

str_len = len(result)
print(str_len)

# sub_str_len = str_len//2
# print(sub_str_len)

# result1 = result[0:sub_str_len]
# print(result1)
#
# result2 = result[sub_str_len:str_len]
# print(result2)

addr_list = re.findall(r"addr :  (\d+)", result, re.S)
for addr in addr_list:
    bases_addr_list.append(int(addr))
print('getBasesAddrList :', bases_addr_list)


addr_list = re.findall(r"addr : (\d+)", result, re.S)
for addr in addr_list:
    bases_addr_list.append(int(addr))
print('getBasesAddrList :', bases_addr_list)