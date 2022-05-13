#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 8async和await.py
# @Time      : 2022/5/13 11:06
# @Author    : weilig
import asyncio
import datetime

'''
Python3.5中对协程提供了更直接的支持，引入了async/await关键字。
上面的代码可以这样改写：使用async代替@asyncio.coroutine，使用await代替yield from，代码变得更加简洁可读。
从Python设计的角度来说，async/await让协程独立于生成器而存在，不再使用yield语法。
'''


async def display_date(num, loop):  # 注意这一行的写法
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果


loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
loop.close()
