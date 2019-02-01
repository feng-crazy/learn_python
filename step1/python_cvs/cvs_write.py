#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 17:47
# @Author  : hedengfeng
# @Site    : 
# @File    : cvs_write.py
# @Software: learn_python
# @description: 


import csv

# 文件头，一般就是数据名
fileHeader = ["name", "score"]

# 假设我们要写入的是以下两行数据
d1 = ["Wang", "100"]
d2 = ["Li", "80"]

# 写入数据

csvFile = open("test_write.csv", "w")
writer = csv.writer(csvFile)

# 写入的内容都是以列表的形式传入函数
writer.writerow(fileHeader)
# writer.writeheader(fileHeader)
writer.writerow(d1)
writer.writerow(d2)

csvFile.close()
