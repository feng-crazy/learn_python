#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 16:32
# @Author  : hedengfeng
# @Site    : 
# @File    : AsyncIOScheduler_test.py
# @Software: LearnPython
# @description: 
"""
Demonstrates how to use the asyncio compatible scheduler to schedule a job that executes on 3
second intervals.
"""

from datetime import datetime
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler

try:
    import asyncio
except ImportError:
    import trollius as asyncio


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(tick, 'interval', seconds=0.5)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass