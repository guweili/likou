#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 10协程asyncio模块编写爬虫.py
# @Time      : 2022/5/13 14:08
# @Author    : weilig
import asyncio


async def display(num):
    print(num)


d = display(1)  # 通过async得到协程对象
print(d)
