#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 18:57
# @Author  : hedengfeng
# @Site    : 
# @File    : configObj.py
# @Software: LearnPython
# @description:
import shutil

from configobj import ConfigObj
import os
config_obj = ConfigObj('termConfig', encoding='UTF8')
config_obj['TERM_NAME'] = 'hdf_123'
config_obj.write()
exit(0)
# if 'TERM_NAME' not in config_obj:
#     print('TERM_NAME not in config')
# else:
#     term_name = config_obj['TERM_NAME']
#     if term_name != '':
#         print('term_name !=:', term_name)
#     else:
#         print('term_name is null')
# exit(0)

report_ip_addr_list = config_obj['REMOTE_MONITOR_ADDR']
report_tcp_port_list = config_obj['REMOTE_MONITOR_PORT']

print('report_ip_addr_list: ', report_ip_addr_list)
print('report_tcp_port_list: ', report_tcp_port_list)

report_ip_addr_ = []
report_tcp_port_ = []

if type(report_ip_addr_list) == list:
    for report_ip_addr in report_ip_addr_list:
        report_ip_addr_.extend([report_ip_addr])
else:
    report_ip_addr_.extend([report_ip_addr_list])

if type(report_tcp_port_list) == list:
    for report_tcp_port in report_tcp_port_list:
        report_tcp_port_.extend([int(report_tcp_port)])
else:
    report_tcp_port_.extend([int(report_tcp_port_list)])

print('report_ip_addr: ', report_ip_addr_)
print('report_tcp_port: ', report_tcp_port_)

config_obj['REMOTE_MONITOR_ADDR'] = config_obj['REMOTE_MONITOR_ADDR']
config_obj['REMOTE_MONITOR_PORT'] = report_tcp_port_[0]

config_obj['REMOTE_MONITOR_PORT'] = 1
print(config_obj['REMOTE_MONITOR_PORT'])

config_obj.write()

exit(0)
try:
    config_obj = ConfigObj('termConfig', encoding='UTF8')

    config_obj['REMOTE_MONITOR_ADDR'] = ['169.158.15.29', '192.168.0.15']

    # report_ip_addr_list = config_obj['REMOTE_MONITOR_ADDR1']
    # print(report_ip_addr_list, type(report_ip_addr_list))

    config_obj.write()
except Exception as err:
    print('Exception', err)
except KeyError as err:
    print('KeyError', err)
exit(0)

config_file = ''
if config_file:
    print('config_file:', config_file)

with open('termConfig', 'r', encoding='utf-8') as f:
    config_file = f.read()
if config_file:
    print(config_file)

print('///////////////////////////')

report_ip_addr_list = config_obj['REMOTE_MONITOR_ADDR']
print(report_ip_addr_list, type(report_ip_addr_list))
report_tcp_port_list = config_obj['REMOTE_MONITOR_PORT']
print(report_tcp_port_list, type(report_tcp_port_list))

term_property_report_ip_addr = []
term_property_report_tcp_port = []

if type(report_ip_addr_list) == list:
    for report_ip_addr in report_ip_addr_list:
        term_property_report_ip_addr.extend([report_ip_addr])
else:
    term_property_report_ip_addr.extend([report_ip_addr_list])

if type(report_tcp_port_list) == list:
    for report_tcp_port in report_tcp_port_list:
        term_property_report_tcp_port.extend([int(report_tcp_port)])
else:
    term_property_report_tcp_port.extend([report_tcp_port_list])

print(term_property_report_ip_addr)
print(term_property_report_tcp_port)

exit(-1)

# chip_id = config_obj['CHIP_ID']
# host_name = config_obj['HOST_NAME']

bs_id = config_obj['BS_IDS']
frequency = config_obj['BS_FREQS']
ingroup_addr = config_obj['BS_INGROUP_ADDRS']
start_angle = config_obj['BS_START_ANGLES']
location = config_obj['BS_LOCATIONS']
print(location)
coordinates_x = float(location[0])
coordinates_y = float(location[1])
coordinates_z = float(location[2])
print(coordinates_x, coordinates_y, coordinates_z)
orientation = config_obj['BS_ORIENTATIONS']
orientation_pitch = float(orientation[0])
orientation_roll = float(orientation[1])
orientation_yaw = float(orientation[2])



# shutil.copyfile('config.txt', 'config_template.txt')


# with open('config.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# config = ConfigObj('config.txt', encoding='UTF8')
#
# print(type(config['bit_rate']))
# print(type(config['check_bit']))
#
# config['bit_rate'] = 115200
# config['data_bit'] = 8
# # config['check_bit'] = 2
#
# print(type(config['bit_rate']))
# print(type(config['check_bit']))
# config.write()
#
# # os.rename('config.txt', 'config1.txt')
#
# # os.remove('config1.txt')
# # if os.path.isfile('config3.txt'):
# #     print('os.remove(config3.txt)')
# #     os.remove('config3.txt')
#
# config = ConfigObj('config1.txt', encoding='UTF8')
# config['bit_rate'] = 115200
# config['data_bit'] = 8
# config['check_bit'] = 9
# config.write()
#
# config2 = ConfigObj('config2.txt', encoding='UTF8')
# config2['bit_rate'] = ['115200', '9600']
# config2['data_bit'] = '25, 26'
# config2['check_bit'] = 31.2354
# config2.write()
#
# config['bit_rate'] = config2['bit_rate']
# config['check_bit'] = config2['check_bit']
#
# def modify(config_arg):
#     config_arg['data_bit'] = [36, 37]
#
# modify(config)
# config.write()
#
# print(config['bit_rate'][0])
# print(config2['data_bit'])


