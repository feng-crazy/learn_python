#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 9:34
# @Author  : hedengfeng
# @Site    : 
# @File    : python_random.py
# @Software: LearnPython
# @description: 


import random


def genegate_ip():
    ip_addr_list = []
    for i in range(4):
        ip_addr_list.append(random.randint(0, 255))
    return '{}.{}.{}.{}'.format(ip_addr_list[0], ip_addr_list[1], ip_addr_list[2], ip_addr_list[3])


my_ip = genegate_ip()
print(my_ip)


def genegate_mac():
    mac_addr_list = []
    for i in range(6):
        mac_addr_list.append(random.randint(0, 255))
    return '{:x}-{:x}-{:x}-{:x}-{:x}-{:x}'.format(mac_addr_list[0], mac_addr_list[1], mac_addr_list[2],
                                                  mac_addr_list[3], mac_addr_list[4], mac_addr_list[5])


my_mac = genegate_mac()
print(my_mac)