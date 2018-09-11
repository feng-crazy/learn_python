# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""


def test():
    for i in range(1, 11):
        yield i


for tmp in test():
    print(tmp)


g = (x * x for x in range(10))
print(g)

for i in g:
    print(i)

g = g

print('**************************')
while True:
    try:
        tmp = next(g)
        print(tmp)
    except StopIteration:
        print('StopIteration')
        break

