# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""
from functools import reduce
from typing import Iterable
map_test = {'status': [79, 75], 'Address': [34], 'cmd': [2]}
print(map_test.keys(), map_test.values())
for x in map_test.keys():
    print(x)
key_list = [x for x in map_test.keys()]
print(key_list)
# print(bytes([x for x in map_test.values()]))

exit(0)

my_map = {}
print(len(my_map))
if my_map:
    print('not null')

my_map['1'] = 1
if my_map:
    print('not null',my_map)
print(len(my_map))
exit(0)
def f(x):
    return x * x


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, list_num)

for i in r:
    print(i)


def f1(x):
    return x + x


r = map(f1, ['a', 'b', 'c'])

print(isinstance(r, Iterable))
print(list(r))

r = map(str, list_num)
num_list = list(r)
print(num_list)

var = '.'.join(['a', 'b', 'c'])
print(var)

var = '.'.join(num_list)
print(var)


def fn(x, y):
    return x * 10 + y


r = reduce(fn, [1, 3, 5, 7, 9])
print(r)
