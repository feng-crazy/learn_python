# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""

# import asyncio
# import time
#
# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#     await asyncio.sleep(x)
#     print('await asyncio.sleep(x)')
#     return 'Done after {}s'.format(x)
#
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# print('a')
# loop.run_until_complete(task)
#
# print('b')
#
# print('Task ret: ', task.result())
# print('TIME: ', now() - start)


import threading
import asyncio
import time


async def helloA(arg):
    while True:
        print('HelloA world! %s (%s) time %s' % (arg, threading.currentThread(), time.asctime()))
        await asyncio.sleep(1)
        print('HelloA again! %s (%s) time %s' % (arg, threading.currentThread(), time.asctime()))


async def helloB(arg):
    while True:
        print('HelloB world! %s (%s) time %s' % (arg, threading.currentThread(), time.asctime()))
        await asyncio.sleep(1)
        while True:
            pass
        print('HelloB again! %s (%s) time %s' % (arg, threading.currentThread(), time.asctime()))


# async def helloC(arg):
#     print('HelloC world! %s (%s) time %s' % (arg, threading.currentThread(), time.asctime()))
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print('HelloC again! %s (%s) time %s' % (arg, threading.currentThread(), time.asctime()))


loop1 = asyncio.get_event_loop()
tasks = [helloA('A'), helloB('B')]
# loop1.run_until_complete(asyncio.wait(tasks))
# task = hello()
print('a')
future = asyncio.wait(tasks)
print('b')
loop1.run_until_complete(future)
print('c')

loop1.close()