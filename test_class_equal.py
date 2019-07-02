#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 16:04
# @Author  : hedengfeng
# @Site    : 
# @File    : test_class_equal.py
# @Software: learn_python
# @description: 


class TerminalProperty:
    host_name = "init"
    mac_addr = ""
    odom_input_option = 0

    def __init__(self, _host_name, _mac_addr, _odom_input_option):
        self.host_name = _host_name
        self.mac_addr = _mac_addr
        self.odom_input_option = _odom_input_option


term1 = TerminalProperty("term1", "7b", 0)
term1.ip = "192.168.0.168"

term2 = TerminalProperty("term1", "7b", 0)

if term1 == term2:
    print("haha")

print(term1.host_name)
print(term1.ip)
print(TerminalProperty.host_name)

tmp1_list = [1, 2, 3.02, 'jaja']

tmp2_list = [1, 2, 3.02, 'jaja']

if tmp2_list == tmp1_list:
    print("..................")

