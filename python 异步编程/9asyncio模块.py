#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 9asyncio模块.py
# @Time      : 2022/5/13 11:10
# @Author    : weilig
'''
协程(Coroutine)又称微线程、纤程，协程不是进程或线程，其执行过程类似于 Python 函数调用，Python 的 asyncio 模块实现的异步IO编程框架中，协程是对使用 async 关键字定义的异步函数的调用;

一个进程包含多个线程,类似于一个人体组织有多种细胞在工作，同样，一个程序可以包含多个协程。多个线程相对独立，线程的切换受系统控制。同样，多个协程也相对独立，但是其切换由程序自己控制。
'''

import asyncio
import time


async def display(num):
    print(num)


d = display('d')  # 通过async得到协程对象
print(d)
'''
event_loop: 事件循环,相当于一个无限循环,可以把一些函数添加到这个事件中,函数不会立即执行, 而是满足某些条件的时候,函数就会被循环执行;
'''
loop = asyncio.get_event_loop()  # 创建事件循环
loop.run_until_complete(d)  # 把协程对象丢给循环,并执行异步函数内部代码

# await: 用来挂起阻塞方法的执行;

import asyncio


def running1():
    async def test1():
        print('1')
        await test2()
        print('2')

    async def test2():
        print('3')
        print('4')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test1())


running1()


# task: 任务,对协程对象的进一步封装,包含任务的各个状态;
async def test():
    print('hello 异步')


c = test()  # 调用异步函数,得到协程对象-->c
loop = asyncio.get_event_loop()  # 创建事件循环
task = loop.create_task(c)  # 创建task任务,对协程对象的进一步封装
print(task)
loop.run_until_complete(task)  # 执行任务

'''
future: 代表以后执行或者没有执行的任务,实际上和task没有本质区别;这里就不做代码展示;
首先使用一般方式方法创建一个函数:
'''


async def func(url):
    print(f'正在对{url}发起请求:')
    print(f'请求{url}成功!')


c = func('www.baidu.com')  # 函数调用的写成对象--> c

loop = asyncio.get_event_loop()  # 创建一个时间循环对象
future_task = asyncio.ensure_future(c)
print(future_task, '未执行')
loop.run_until_complete(future_task)  # 注册加启动
print(future_task, '执行完了')

'''
await关键字的使用
在异步函数中，可以使用await关键字，针对耗时的操作(例如网络请求、文件读取等IO操作)进行挂起，比如异步程序执行到某一步时需要很长时间的等待，就将此挂起，去执行其他异步函数
'''


async def do_some_work(n):  # 使用async关键字定义异步函数
    print('等待:{}秒'.format(n))
    await asyncio.sleep(n)  # 休眠一段时间
    return '{}秒后返回结束运行'.format(n)


start_time = time.time()  # 开始时间
coro = do_some_work(2)
loop = asyncio.get_event_loop()  # 创建事件循环对象
loop.run_until_complete(coro)
print('运行时间: ', time.time() - start_time)

'''
任务(Task)对象用于封装协程对象，保存了协程运行后的状态，使用 run_until_complete() 方法将任务注册到事件循环;
如果我们想要使用多任务,那么我们就需要同时注册多个任务的列表,可以使用 run_until_complete(asyncio.wait(tasks))，
这里的tasks,表示一个任务序列(通常为列表)
注册多个任务也可以使用run_until_complete(asyncio. gather(*tasks))
'''


async def do_some_work(i, n):  # 使用async关键字定义异步函数
    print('任务{}等待: {}秒'.format(i, n))
    await asyncio.sleep(n)  # 休眠一段时间
    return '任务{}在{}秒后返回结束运行'.format(i, n)


start_time = time.time()  # 开始时间
tasks = [asyncio.ensure_future(do_some_work(1, 2)),
         asyncio.ensure_future(do_some_work(2, 1)),
         asyncio.ensure_future(do_some_work(3, 3))]  # 构建三个task任务
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  # 同时注册多个任务列表
for task in tasks:
    print('任务执行结果: ', task.result())
print('运行时间: ', time.time() - start_time)
