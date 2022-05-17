#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : test.py
# @Time      : 2022/5/17 10:39
# @Author    : weilig
import time

# def func1():
#     for i in range(10000000):
#         i + 1
#
#
# def func2():
#     for i in range(10000000):
#         i + 1
#
#
# start = time.time()
# func1()
# func2()
# stop = time.time()
# print(stop - start)


# 基于yield并发执行
# def func1():
#     while True:
#         yield
#
#
# def func2():
#     g = func1()
#     for i in range(10000000):
#         i + 1
#         next(g)
#
#
# start = time.time()
# func2()
# stop = time.time()
# print(stop - start)


# def func1():
#     while True:
#         print('func1')
#         yield
#
#
# def func2():
#     g = func1()
#     for i in range(10000000):
#         i + 1
#         next(g)
#         time.sleep(3)
#         print('func2')
#
#
# start = time.time()
# func2()
# stop = time.time()
# print(stop - start)

import gevent  # 通过gevent实现协程遇见io操作时自动切换


def eat(name):
    print('%s eat 1' % name)  # 1
    gevent.sleep(2)  # 模拟io阻塞，自动切换play方法
    print('%s eat 2' % name)  # 4


def play(name):
    print('%s play 1' % name)  # 2
    gevent.sleep(1)  # 模拟io阻塞，继续切换，没有就等待
    print('%s play 2' % name)  # 3


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
g1.join()
g2.join()
# 或者gevent.joinall([g1,g2])
print('主')
