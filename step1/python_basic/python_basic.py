#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 18:24
# @Author  : hedengfeng
# @Site    : 
# @File    : python_basic.py
# @Software: LearnPython

i = 0
loop_len = 10

while i < loop_len:
    print(i)
    # i += 1


for i in range(0, 10):
    if i % 3 == 0:
        print(0)
    elif i % 3 == 1:
        print(1)
    elif i % 3 == 2:
        print(2)

exit(0)

A = 0
B = 8
C = [0]

def func():
    global A
    A = 1
    A = B
    C[0] += 1
    C[0] = 4
    C.append(2)
    print(B)

print(A)
print(C)
func()
print(A)
print(C)


X = '1'
Y = '2'
Z = '3'
J = '2'
if X != Y and X != Z:
    print('&')


