#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 3yieldSend方法.py
# @Time      : 2022/5/12 13:21
# @Author    : weilig
'''
其实对于IO密集型任务我们还有一种选择就是协程。协程，又称微线程，英文名Coroutine，是运行在单线程中的“并发”，协程相比多线程的一大优势就是省去了多线程之间的切换开销，获得了更高的运行效率。Python中的异步IO模块asyncio就是基本的协程模块。

Python中的协程经历了很长的一段发展历程。最初的生成器yield和send()语法，然后在Python3.4中加入了asyncio模块，引入@asyncio.coroutine装饰器和yield from语法，在Python3.5上又提供了async/await语法，目前正式发布的Python3.6中asynico也由临时版改为了稳定版。

1. 协程：
协程的切换不同于线程切换，是由程序自身控制的，没有切换的开销。协程不需要多线程的锁机制，因为都是在同一个线程中运行，所以没有同时访问数据的问题，执行效率比多线程高很多。

因为协程是单线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

如果你还无法理解协程的概念，那么可以这么简单的理解：

进程/线程：操作系统提供的一种并发处理任务的能力。

协程：程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧。

多进程和多线程体现的是操作系统的能力，而协程体现的是程序员的流程控制能力。看下面的例子，甲，乙两个工人模拟两个工作任务交替进行，在单线程内实现了类似多线程的功能。
'''

import time


def task1():
    while True:
        res = yield "我是task1返回值"
        print('接收task2传入的参数', res)
        time.sleep(1)
        print("<甲>工作了一段时间.....")
        print("<甲>也累了，让<乙>工作一会儿")


def task2(t):
    # next继续执行yield后续的代码块，生成器是特殊的迭代器，也实现了__next__ , __iter__ 方法
    res = next(t)  # 通过next方法触发生成器使其工作,到达yield关键字位置暂停, 通过next方法接收返回的数据
    print(res)
    while True:
        print("-----------------------------------")
        print("<乙>工作了一段时间.....")
        time.sleep(2)
        print("<乙>累了，让<甲>工作一会儿....")
        ret = t.send('我是task2传入的参数')  # ret 接受 taks1 返回的 yield 返回值
        print(ret)


# t = task1()  # 函数调用后通过yield进行函数暂停, 后续通过send方法启动yield方法
# task2(t)
# t.close()

'''
运行结果如下:
我是task1返回值
-----------------------------------
<乙>工作了一段时间.....
<乙>累了，让<甲>工作一会儿....
接收task2传入的参数 我是task2传入的参数
<甲>工作了一段时间.....
<甲>也累了，让<乙>工作一会儿
我是task1返回值
-----------------------------------
<乙>工作了一段时间.....
<乙>累了，让<甲>工作一会儿....
接收task2传入的参数 我是task2传入的参数
<甲>工作了一段时间.....
<甲>也累了，让<乙>工作一会儿
我是task1返回值
-----------------------------------
<乙>工作了一段时间.....

通过上述结果得知，
生成器具有函数暂停的效果，当接收到next方法和send方法会触发生成器，会切换到生成器的代码块进行工作，然后到达yield关键字后暂停，
继续其他类型的工作,等待下次next，send 方法进行触发
'''

'''
3. send()
最初的yield只能返回并暂停函数，并不能实现协程的功能。后来，Python为它定义了新的功能——接收外部发来的值，这样一个生成器就变成了协程。

每个生成器都可以执行send()方法，为生成器内部的yield语句发送数据。此时yield语句不再只是yield xxxx的形式，还可以是var = yield xxxx的赋值形式。它同时具备两个功能，一是暂停并返回函数，二是接收外部send()方法发送过来的值，重新激活函数，并将这个值赋值给var变量！

协程可以处于下面四个状态中的一个。当前状态可以导入inspect模块，使用inspect.getgeneratorstate(...) 方法查看，该方法会返回下述字符串中的一个。
'GEN_CREATED'　　等待开始执行。
'GEN_RUNNING'　　协程正在执行。
'GEN_SUSPENDED' 在yield表达式处暂停。
'GEN_CLOSED' 　　执行结束。

因为send()方法的参数会成为暂停的yield表达式的值，所以，仅当协程处于暂停状态时才能调用 send()方法，例如my_coro.send(10)。不过，如果协程还没激活（状态是'GEN_CREATED'），就立即把None之外的值发给它，会出现TypeError。因此，始终要先调用next(my_coro)激活协程（也可以调用my_coro.send(None)），这一过程被称作预激活。
除了send()方法，其实还有throw()和close()方法：

generator.throw(exc_type[, exc_value[, traceback]])
使生成器在暂停的yield表达式处抛出指定的异常。如果生成器处理了抛出的异常，代码会向前执行到下一个yield表达式，而产出的值会成为调用generator.throw()方法得到的返回值。如果生成器没有处理抛出的异常，异常会向上冒泡，传到调用方的上下文中。

generator.close()
使生成器在暂停的yield表达式处抛出GeneratorExit异常。如果生成器没有处理这个异常，或者抛出了StopIteration异常（通常是指运行到结尾），调用方不会报错。如果收到GeneratorExit异常，生成器一定不能产出值，否则解释器会抛出RuntimeError异常。生成器抛出的其他异常会向上冒泡，传给调用方。
'''

def simple_coroutine():
    print('-> 启动协程')
    y = 10
    x = yield y
    print('-> 协程接收到了x的值:', x)


my_coro = simple_coroutine()
ret = next(my_coro)
print(ret)
my_coro.send(10)
