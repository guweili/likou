#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 7 asyncio与yieldFrom .py
# @Time      : 2022/5/12 14:38
# @Author    : weilig
'''
@asyncio.coroutine与yield from
@asyncio.coroutine：asyncio模块中的装饰器，用于将一个生成器声明为协程。
'''

import asyncio
import datetime


@asyncio.coroutine  # 声明一个协程
def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果


loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
loop.close()
