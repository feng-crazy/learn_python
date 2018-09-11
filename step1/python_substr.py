# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""
import os

from configobj import ConfigObj

str_tmp = '9876543210'
sub_str = '654321'
print(str_tmp.find(sub_str))

sub_str = '654320'
print(str_tmp.find(sub_str))

sub_str = '987'
print(str_tmp.find(sub_str))

if -1:
    print('-1 is true')

ip_addr = '192.168.0.168'
mac_addr = 'b8:27:eb:dc:ad:36'
mac_addr = mac_addr.replace(':', '-')
print(mac_addr)
mac_addr1 = '00-E0-4C-41-12-84'
host_name = 'DESKTOP-VHLRTSP'

file_name = 'config/' + ip_addr + '_' + mac_addr1 + '_' + host_name
print(file_name)

if mac_addr1 in file_name:
    print('find: ', mac_addr1)


config = ConfigObj(file_name, encoding='UTF8')

config['bit_rate'] = 115200
config['data_bit'] = 8
config['check_bit'] = 2
config.write()

file_list = os.listdir('./config')
property_list = []
str_test = 1
for file_name in file_list:
    print(file_name)
    property_list = file_name.split('_')
    str_test = 2

print('property_list: ', property_list)
print('str_test: ', str_test)

test_str = '192.168.0.168'

test_str = "123456abc789"

tmp = test_str[6:9]
print(tmp)

sub_str = 'abc'
abc_index = test_str.find(sub_str)
print(abc_index)

tmp = test_str[abc_index:abc_index + len(sub_str)]
print(tmp)

tmp = test_str[6::2]
print(tmp)
