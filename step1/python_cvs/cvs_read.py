#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 17:47
# @Author  : hedengfeng
# @Site    : 
# @File    : cvs_read.py
# @Software: learn_python
# @description: 

import csv


csvFile = open("test_write.csv", "r")
reader = csv.reader(csvFile)

print(reader)

# for item in reader:
#     print(item)

# 建立空字典
result = {}
for item in reader:
    print(item, type(item))
    # # 忽略第一行
    if reader.line_num == 1:
        continue
    if len(item) >= 2:
        result[item[0]] = item[1]


print('result:', result)
csvFile.close()

print('--------------------------')
# csvFile = open("test_wirte1.csv", "r")
csvFile = open("test_write.csv", "r")
dict_reader = csv.DictReader(csvFile)

for row in dict_reader:
    print(row)
    print(row['name'], row['score'])

csvFile.close()

