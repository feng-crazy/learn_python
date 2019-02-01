#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:54
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_test.py
# @Software: learn_python
# @description: 
import psutil


def judge_ip_network_segment(src_ip_list, dest_ip):
    dest_ip_char_list = dest_ip.split('.')
    for ip_item in src_ip_list:
        src_ip_char_list = ip_item.split('.')
        if src_ip_char_list[0] == dest_ip_char_list[0] and src_ip_char_list[1] == dest_ip_char_list[1] \
                and src_ip_char_list[2] == dest_ip_char_list[2]:
            return ip_item

    return False


def get_all_ip_addr():
    ip_addr_list = []
    net_all_info = psutil.net_if_addrs()
    for k, v in net_all_info.items():
        for item in v:
            if item[0] == 2:
                ip_addr_list.append(item[1])
    return ip_addr_list


local_ip_addr_list = get_all_ip_addr()
print('local_ip_addr_list:', local_ip_addr_list)

ret = judge_ip_network_segment(local_ip_addr_list, '192.168.1.1')
print('ret:', ret)




