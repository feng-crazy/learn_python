#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 16:38
# @Author  : hedengfeng
# @Site    : 
# @File    : python_sys_argv.py
# @Software: LearnPython
# @description:
import sys


def main():
    print(type(sys.argv), sys.argv)

    # if len(sys.argv) > 1:
    #     print(sys.argv[1])
    #     if sys.argv[1] == '-d':
    #         print('hahahhahah')

    argv_list = sys.argv[1:]
    if len(argv_list) > 0 and argv_list[0] == '-d':
        print(argv_list[0])
        print('hahahhahah')
    print('argv_list:', argv_list)


if __name__ == '__main__':
    main()