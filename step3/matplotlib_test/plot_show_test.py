#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019-07-02 15:56
# @Author  : hedengfeng
# @Site    : 
# @File    : plot_show_test.py
# @Software: learn_python
# @description: 
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


loc_x_list = [i for i in range(0, 100)]
loc_y_list = [i for i in range(0, 100)]

optimize_x_list = [i for i in range(0, 100)]
optimize_y_list = [i for i in range(0, 100)]

if __name__ == "__main__":
    for i in range(0, len(optimize_x_list)):
        optimize_x_list[i] += 10
        
        plt.plot(loc_x_list, loc_y_list)
        plt.plot(optimize_x_list, optimize_y_list)
        plt.draw()

    plt.show()