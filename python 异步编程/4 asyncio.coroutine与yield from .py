#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 4 asyncio.coroutine与yield from .py
# @Time      : 2022/5/12 14:38
# @Author    : weilig
'''
@asyncio.coroutine与yield from
@asyncio.coroutine：asyncio模块中的装饰器，用于将一个生成器声明为协程。

yield from 其实就是等待另外一个协程的返回。
'''


def func():
    for i in range(10):
        yield i


f = func()
print(type(next(f)))
print(next(f))
print(list(f))


# 上述的代码可以写成这样
def func():
    yield from range(10)


f = func()
print(type(next(f)))
print(next(f))
print(list(f))

'''
yield  和  yield from 区别
yield返回的是一个值，

'''
