#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 使用多线程构建一个简单生产者消费者模式.py
# @Time      : 2022/5/16 15:03
# @Author    : weilig
'''
利用多线程和队列可以实现生产者消费者模式。
该模式通过平衡生产线程和消费线程的工作能力来提高程序整体处理数据的速度。
'''

import time
import queue
import threading

q = queue.Queue(10)  # 生成一个队列，用来保存“包子”，最大数量为10


def productor(i):
    # 厨师不停地每2秒做一个包子
    while True:
        q.put("厨师 %s 做的包子！" % i)
        time.sleep(1)


def consumer(j):
    # 顾客不停地每秒吃一个包子
    while True:
        print("顾客 %s 吃了一个 %s" % (j, q.get()))
        time.sleep(2)


# 实例化了3个生产者（厨师）
for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()
# 实例化了10个消费者（顾客）
for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()

# 通过中间人queue队列存放任务,达到并行生产和消耗任务
