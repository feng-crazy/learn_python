
# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""

from random import randint
import time
import zmq

context = zmq.Context(1)
server = context.socket(zmq.REP)
server.bind("tcp://*:5555")

cycles = 0
while True:
    request = server.recv_string()
    cycles += 1

    # Simulate various problems, after a few cycles
    if cycles > 3 and randint(0, 3) == 0:
        print("I: Simulating a crash")
        break
    elif cycles > 3 and randint(0, 3) == 0:
        print("I: Simulating CPU overload")
        time.sleep(2)
        break

    print("I: Normal request (%s)" % request)
    time.sleep(1)  # Do some heavy work
    send_ret = server.send_string(request)
    print(send_ret)

server.close()
context.term()
