#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-13 10:23
# @Author  : hedengfeng
# @Site    : 
# @File    : condition_test.py
# @Software: learn_python
# @description:

print(-20/50)
print(20/50)

a, b, c = 1, 2, 3
# 1.常规

if a > b:
    c = a
else:
    c = b

print(c)

# 2.表达式
c = a if a > b else b  # 先执行中间的if，如果返回True，就是左边，False是右边。
print(c)
# 3.二维列表
c = [b, a][a < b]  # 实际是[b,a][False]，因为False被转换为0，所以是[1,2][0]，也就是[1],False返回第一个，True 返回第二个。
print(c)
# 4
c = (a > b and [a] or [b])[0]
print(c)
# 这个比较好玩，False and [1] or [2]，因为and的优先级高于or，先算and
# False和[1] and之后还是False，和[2]or之后却成了[2]
# True 和[1] and之后是[1]，[1]和[2]or结果是[1]
# 也就是False和True在和别人做boolean运算的时候，根据and还是or，F和T在前在后有不一样的数据转换规则。
