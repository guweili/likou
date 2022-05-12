#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : test.PY
# @Time      : 2021/12/1 10:11
# @Author    : weilig
from functools import reduce

nums = list(range(101))

'''
map(修改列表中的元素),并返回新的可迭代对象, 需要一个参数
'''
a = map(lambda x: x + 1, nums)
print(list(a))
print(list(nums))

'''
filter(过滤列表中的元素),并返回新的可迭代对象， 需要一个参数
'''

b = filter(lambda x: x % 3 == 0, nums)
print(list(b))
print(list(nums))

'''
reduce(列表元素操作结果累计), 并返回最后的结果， 需要两个参数
'''
c = reduce(lambda x, y: x - y, nums)
print(c)
print(list(nums))
