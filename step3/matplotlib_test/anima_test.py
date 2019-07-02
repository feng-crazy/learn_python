#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-07-02 16:29
# @Author  : hedengfeng
# @Site    : 
# @File    : anima_test.py
# @Software: learn_python
# @description: 
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=False)


def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    return ln,


def update(frame):
    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, range(1, 100), init_func=init, blit=True)

# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128),
#                     init_func=init, blit=True)
plt.show()
