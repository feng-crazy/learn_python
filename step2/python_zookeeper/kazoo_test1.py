#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-18 14:57
# @Author  : hedengfeng
# @Site    : 
# @File    : kazoo_test1.py
# @Software: learn_python
# @description: 
import logging
from time import sleep
from kazoo.client import KazooClient

# print log to console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

zk = KazooClient('127.0.0.1:2181')
zk.start()


def children_callback(children):
    print('****', children)


children = zk.get_children('/zookeeper', children_callback)

zk.create('/zookeeper/goodboy')
# zk.delete('/zookeeper/goodboy')

while True:
    sleep(1)

