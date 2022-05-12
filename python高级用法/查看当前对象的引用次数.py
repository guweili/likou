#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 查看当前对象的引用次数.PY
# @Time      : 2022/2/9 10:31
# @Author    : weilig


def hello_world():
    print('hello world')


hello = hello_world
hello()
import sys

count = sys.getrefcount(hello_world)  # 查看引用，根据当前的名称出现次数,可以判断引用了几次
print(count)
