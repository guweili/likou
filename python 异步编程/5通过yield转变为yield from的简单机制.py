#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 5通过yield转变为yield from的简单机制.py
# @Time      : 2022/5/13 9:13
# @Author    : weilig
from functools import wraps
from inspect import getgeneratorstate


'''
通过yield转变为yield from的简单机制

'''
class DemoException(Exception):
    """异常示例"""


def coroutine(func):
    @wraps(func)  # wraps包装: 被包装函数会保留自己的属性
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)  # 返回生成器
        next(gen)  # 激活生成器
        return gen

    return primer


@coroutine
def demo_func():
    print('start...')
    try:
        while True:
            try:
                x = yield 666
            except DemoException:
                print("It's DemoException.Go on...")
            else:
                print('received: ', x)
    finally:
        print("The End!.")


a = demo_func()  # 实例化,预激活  打印:  start...
a.send(10)  # received:  10
a.send(20)  # received:  20
print(a.throw(DemoException))  # It's DemoException.Go on... 666 throw返回值为下一个yield右侧的值
# print(a.throw(ZeroDivisionError))  # The End!.  传入未处理异常,直接整个程序向上冒泡至结束
print(getgeneratorstate(a))  # GEN_SUSPENDED
a.close()  # The End!
print(getgeneratorstate(a))  # GEN_CLOSED
