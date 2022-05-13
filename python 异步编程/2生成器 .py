#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 2生成器 .py
# @Time      : 2022/5/12 13:48
# @Author    : weilig
'''
Python中迭代器协议主要用到了两个魔法方法：__iter__(),__next__()
__iter__() 方法创建一个具有__next__()方法的迭代器对象
__next__() 方法返回下一个迭代器对象

1. 什么是yield?
首先我们需要认识一生成器（generator），从字面意思上理解，循环计算的操作方式。在Python中，提供一种可以边循环边计算的机制。

生成器是解决使用序列存储大量数据时，内存消耗大的问题。我们可以根据存储数据的某些规律，演算为算法，在循环过程中通过计算得到，这样可以不用创建完整序列，从而大大节省占用空间。

yield 是实现生成器方法之一，当函数使用yield方法，则该函数就成为了一个生成器。调用该函数，就等于创建了一个生成器对象。

2. yield 原理
一个生成器，主要是通过循环反复调用next()方法，直到捕获异常。

具有 yield方法的函数也是一个生成器，创建如下栗子：
'''
import time


def test(n=1):
    print("starting...")
    while True:
        res = yield n  # res 为 send 方法传入的接收值
        print("res:", res)
        time.sleep(3)
        g = test()
        print(next(g))  # next方法接收yield返回值 ， 打印 yield 返回值 n
        print("######")
        print(g.send(2))


t = test()  # 函数中有关键字yield时，会返回一个生成器对象 generator
print(type(t))
next(t)  # 通过next触发生成器对象的调用, 遇到yield进行暂停
t.send(4)  # 通过yield进行暂停将4这个参数传入到生成器中接收,触发后续的代码块,进入下次循环，到达 yield 再次进入暂停, 等待下个next或send再次触发后续的操作

'''
<class 'generator'>
starting...
res: 4
starting...
1
######
res: 2
starting...
1
######
res: 2
'''
