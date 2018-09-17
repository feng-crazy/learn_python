#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 18:44
# @Author  : hedengfeng
# @Site    : 
# @File    : paramiko_test.py
# @Software: learn_python
# @description:
import sys
import re
import paramiko


def connect_ssh(ip_addr):
    if judge_ip_addr(ip_addr) is not True:
        return

    ssh = paramiko.SSHClient()

    # 这行代码的作用是允许连接不在know_hosts文件中的主机。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_addr, username='pi', password='hdf654321')

    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.readlines())


def judge_ip_addr(ip_str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip_str):
        return True
    else:
        return False


def main():
    print(type(sys.argv))
    ip_addr_list = sys.argv[1:]
    print('ip_addr_list:', ip_addr_list)
    connect_ssh(ip_addr_list[0])
    # while True:
    #     data = input('please input scp id addr:')
    #     if data == 'q':
    #         break
    #     elif judge_ip_addr(data):
    #         scp_file([data])


if __name__ == '__main__':
    main()