#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 4通过装饰器预激协程.py
# @Time      : 2022/5/12 14:56
# @Author    : weilig
from functools import wraps


def coroutine(func):
    @wraps(func)  # wraps包装: 被包装函数会保留自己的属性
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)  # 返回生成器
        next(gen)  # 激活生成器
        return gen

    return primer


@coroutine
def averager2():
    total = 0.0
    count = 0
    average = None
    print('协程已激活，yield处等待下一步的指令')
    while True:
        term = yield average
        print('通过send传入参数', term)
        total += term
        count += 1
        average = total / count


coro_avg = averager2()
from inspect import getgeneratorstate

print(getgeneratorstate(coro_avg))  # 查看生成器状态
print(coro_avg.send(10))  # send发送消息，并接收yield返回值
print(coro_avg.send(30))
print(coro_avg.send(50))

'''
协程已激活，yield处等待下一步的指令
GEN_SUSPENDED
通过send传入参数 10
10.0
通过send传入参数 30
20.0
通过send传入参数 50
30.0
'''
