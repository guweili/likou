#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 1可迭代对象 迭代器.py
# @Time      : 2022/5/12 13:33
# @Author    : weilig
'''
先说结论，再解释：

iterable是可迭代对象，它的唯一特征是有__iter__函数，调用这个函数会返回一个iterator。
iterator是迭代器，它的唯一特征是有__next__函数，调用这个函数会返回下一个元素。
有些类同时有以上两个函数，所以即是iterable，又是iterator，这是为了方便，不用额外创建iterator类。
generator是用yield函数定义的iterator。它必然也有__next__函数。
'''

# 可以通过for循环遍历的对象都是可迭代对象iterable, 比如list ，range， tuple

# a = []
# b = ()
# c = range(10)
# print(dir(a))
# print(dir(b))
# print(dir(c))
# '''
# 下面返回的属性:
#     ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#     ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
#     ['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
# '''
# d = [2, 3, 4]
# e = iter(d)
# print(e)
# print(dir(e))
# # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
# for i in e:
#     print(i)
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))

''' 
迭代器的用法：

首先说两个概念，一个是可迭代的对象，一个是迭代器对象，两个不同。可迭代的(Iterable)：就是可以for循环取数据的，比如字典、列表、元组、字符串等，不可使用next()方法。
迭代器(Iterator)，也是可以依次迭代取出数据的对象，在内存空间是这样存储的： 占用内存小，并且可以使用next()方法依次取数据。
可以使用isinstance()方法来判断一个对象是可迭代对象还是迭代器对象。
'''
# from collections import Iterable, Iterator
#
# a = [1, 2, 3]
# print(isinstance(a, Iterable))  # 判断是否为可迭代对象
# print(isinstance(a, Iterator))  # 判断是否为迭代器
# b = iter(a)  # 将列表转化成迭代器
# print(isinstance(b, Iterable))
#
# # for i in b:
# #     print(i)
#
# for i in range(4):
#     # next方法超出界限会抛出异常  StopIteration
#     print(next(b))

'''
python迭代器的优缺点
1. 迭代器节省内存，在迭代器中只占一个数据空间的内存，每次迭代元素时，都会将上一条数据释放，然后在加载最新的数据, 惰性机制
2. 只能一直向下取值，超出后会报错 StopIteration
'''


# 自定制可迭代对象
class RandList:
    _index = -1  # 记录下标位置

    def __init__(self, alist: list):
        self.alist = alist

    # def __getitem__(self, item):
    #     return self.alist[item]

    def __iter__(self):
        for i in self.alist:
            yield i


alist = RandList([1, 3, 5])
for i in alist:
    print(i)

'''
发现运行结果又正确了，我们发现 __iter__ 和 __getitem__ 中实现任意一个，对象就是可迭代的，怎么解释这种情况呢，Python 解释器中有这样的描述

解释器需要迭代对象 x 时， 会自动调用 iter(x)。
内置的 iter 函数有以下作用。

检查对象是否实现了 __iter__方法， 如果实现了就调用它， 获取一个迭代器。
如果没有实现 __iter__方法， 但是实现了 __getitem__ 方法，Python 会创建一个迭代器， 尝试按顺序（从索引 0 开始） 获取元素。
如果尝试失败， Python 抛出 TypeError 异常， 通常会提示“C object is not iterable”（C 对象不可迭代） ， 其中 C 是目标对象所属的类。
任何 Python 序列都可迭代的原因是， 它们都实现了 __getitem__ 函数。 其实， 标准的序列都实现了 __iter__ 函数， 因此你也应该这么做。
'''
