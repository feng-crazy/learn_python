#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 19:56
# @Author  : hedengfeng
# @Site    : 
# @File    : python_list.py
# @Software: LearnPython


list_test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_test2)

list_test3 = list_test2
list_test3[5] = 15
print(list_test2)
exit(0)
for i in list_test2:
    if i % 2 == 0:
        list_test2.remove(i)

print(list_test2)

exit(0)

pack_init_data = [i for i in range(0, 10)]

list_tmp = [[99, 109, 100, 58, 2], [65, 100, 100, 114, 101, 115, 115, 58, 34], [115, 116, 97, 116, 117, 115, 58, 79, 75]]
print(list_tmp)
print(bytes([0x00 for i in list_tmp]))
print([x * x for x in range(1, 11)])
list_test1 = []
# list_test1.extend(list_tmp[0])
print(list_test1)
list_test = [bytes(i) for i in list_tmp]
print(list_test1)
print(list_test)

print(['{:02x}'.format(i) for i in list_test1])

exit(0)

map_list = [{'first': 1}, {'second': 2}]
map_list2 = [{'first': 1}, {'second': 2}]
if map_list == map_list2:
    print('map_list == map_list2')
for list_elem in map_list:
    if 'first' in list_elem:
        print(list_elem['first'])
    elif 'second' in list_elem:
        print(list_elem['second'])

cmd_data = [0x00 for x in range(0, 22)]
print(cmd_data.index(0x00))
cmd_tmp = [0x01, 0x02, 0x03]
cmd_data += cmd_tmp

print(cmd_data.index(0x01))


print(cmd_data.count(0), cmd_data.count(1))


print(len(cmd_data), cmd_data, cmd_data[23])
exit(0)

# list_test = [1, 2, 3, 4, 5, 6, 255]
# print('{:x}'.format(list_test))

list_chip_id = [0x67, 0x18, 0x51, 0x48, 0x57, 0x48, 0x88, 0x77, 0x06, 0x6b, 0xff, 0x48]
print(list_chip_id)

list1 = [1, 2, 3, 4, 5, "s"]
list_sub_1 = list1[3:5]
print(bytes(list_sub_1))

list2 = [6, 7, 8, 9, "a"]
list3 = list1 + list2
print(list3)

index = list1.index('s')
print(index)

for i, elem in enumerate(list1):
    print(i, elem)
    if elem == 2:
        list1.remove(elem)
print(list1)

for elem in list1:
    if elem == 2:
        list1.remove(elem)
        # ret = list1.pop(elem)
        # print(ret)
print(list1)


list1 = [1, 2, 3, 4, 5, "s"]
print(list1[5].title())

for target in list1:

    target = 6

print(list1)

count = 0
while count < len(list1):
    list1[count] = 6
    count += 1

print(list1)


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("\nVerifying user: " + current_user)
    confirmed_users.append(current_user)
    # 显示所有已验证的用户
    print("The following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user)

print(unconfirmed_users)