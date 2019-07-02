#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-19 10:12
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp.py
# @Software: learn_python
# @description:
import time

for i in range(0,9,3):
    print(i)
exit(0)

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

exit(0)

list_tmp = ['dfaa: ', 1, 2, 3.02, time.time()]
print("{}".format(list_tmp))
print(str(list_tmp))
exit(0)

tmp_tuple1 = [1, 1]
tmp_tuple2 = [2, 2]

tmp_tuple3 = [tmp_tuple1[0] + tmp_tuple2[0], tmp_tuple1[1] + tmp_tuple2[1]]
print(tmp_tuple3)

# for i in range(0, int(10)):
#     symbol = 1 if (i % 2) else -1
#     print(-symbol)

# symbol = -1
# for i in range(0, int(10)):
#     symbol *= -1
#     print(symbol)

