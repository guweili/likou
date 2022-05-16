#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 多进程 multiprocess.py
# @Time      : 2022/5/16 15:00
# @Author    : weilig

# 多进程multiprocess

import os
import multiprocessing

# def foo(i):
#     # 同样的参数传递方法
#     print("这里是 ", multiprocessing.current_process().name)
#     print('模块名称:', __name__)
#     print('父进程 id:', os.getppid())  # 获取父进程id
#     print('当前子进程 id:', os.getpid())  # 获取自己的进程id
#     print('------------------------')
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=foo, args=(i,))
#         p.start()
import time

'''
进程间的数据共享
在Linux中，每个子进程的数据都是由父进程提供的，每启动一个子进程就从父进程克隆一份数据。
创建一个进程需要非常大的开销，每个进程都有自己独立的数据空间，不同进程之间通常是不能共享数据的，要想共享数据，一般通过中间件来实现。
下面我们尝试用一个全局列表来实现进程间的数据共享：
'''

# from multiprocessing import Process
#
# lis = []
#
#
# def foo(i):
#     lis.append(i)
#     print("This is Process ", i, " and lis is ", lis, " and lis.address is  ", id(lis))
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = Process(target=foo, args=(i,))
#         p.start()
#     print("The end of list_1:", lis)

'''
The end of list_1: []
This is Process  2  and lis is  [2]  and lis.address is   40356744
This is Process  1  and lis is  [1]  and lis.address is   40291208
This is Process  0  and lis is  [0]  and lis.address is   40291208
This is Process  3  and lis is  [3]  and lis.address is   40225672
This is Process  4  and lis is  [4]  and lis.address is   40291208

可以看到，全局列表lis没有起到任何作用，在主进程和子进程中，lis指向内存中不同的列表。
想要在进程之间进行数据共享可以使用Queues、Array和Manager这三个multiprocess模块提供的类。
'''

'''
可以看到，全局列表lis没有起到任何作用，在主进程和子进程中，lis指向内存中不同的列表。
想要在进程之间进行数据共享可以使用Queues、Array和Manager这三个multiprocess模块提供的类。

使用Array共享数据
对于Array数组类，括号内的“i”表示它内部的元素全部是int类型，而不是指字符“i”，数组内的元素可以预先指定，
也可以只指定数组的长度。Array类在实例化的时候必须指定数组的数据类型和数组的大小，类似temp = Array('i', 5)。对于数据类型有下面的对应关系：
'''

from multiprocessing import Process
from multiprocessing import Array


def func(i, temp):
    temp[0] += 100
    print("进程%s " % i, ' 修改数组第一个元素后----->', temp[0])


if __name__ == '__main__':
    temp = Array('i', [1, 2, 3, 4])
    for i in range(10):
        p = Process(target=func, args=(i, temp))
        p.start()
