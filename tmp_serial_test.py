#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 16:57
# @Author  : hedengfeng
# @Site    : 
# @File    : tmp_serial_test.py
# @Software: learn_python
# @description:
import time

import serial


ser = serial.Serial("COM5", 115200, timeout=0.5)
time.sleep(1)
# ser.write('\r\n\r\n\r\n'.encode())
# serial_data = ser.readline()
# print('serial_data:', serial_data)

write_cnt = ser.write('get mode\r\n'.encode())
print('write_cnt:', write_cnt)
time.sleep(0.5)
ready_bytes = ser.inWaiting()
print('ready_bytes:', ready_bytes)
serial_data = ser.read(ready_bytes)
print('serial_data:', serial_data)

ser.close()