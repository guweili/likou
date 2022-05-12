#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 1 可迭代对象 迭代器.py
# @Time      : 2022/5/12 13:33
# @Author    : weilig
'''
迭代器的用法：

首先说两个概念，一个是可迭代的对象，一个是迭代器对象，两个不同。可迭代的(Iterable)：就是可以for循环取数据的，比如字典、列表、元组、字符串等，不可使用next()方法。
迭代器(Iterator)，也是可以依次迭代取出数据的对象，在内存空间是这样存储的： 占用内存小，并且可以使用next()方法依次取数据。
可以使用isinstance()方法来判断一个对象是可迭代对象还是迭代器对象。
'''
from collections import Iterable, Iterator

a = [1, 2, 3]
print(isinstance(a, Iterable))  # 判断是否为可迭代对象
print(isinstance(a, Iterator))  # 判断是否为迭代器
b = iter(a)  # 将列表转化成迭代器
print(isinstance(b, Iterable))

# for i in b:
#     print(i)

for i in range(4):
    # next方法超出界限会抛出异常  StopIteration
    print(next(b))

'''
python迭代器的优缺点
1. 迭代器节省内存，在迭代器中只占一个数据空间的内存，每次迭代元素时，都会将上一条数据释放，然后在加载最新的数据, 惰性机制
2. 只能一直向下取值，超出后会报错 StopIteration
'''
