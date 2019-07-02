#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.txt', 'w', encoding='gbk') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))
    f.truncate(0)

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

