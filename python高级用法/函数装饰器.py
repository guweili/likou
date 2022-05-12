#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 函数装饰器.PY
# @Time      : 2021/12/1 11:08
# @Author    : weilig

'''
普通装饰器
'''

def testa(func):
    print('test1')

    def testb(*args):
        print('test2')
        func(*args)

    return testb


def wrapper(func):
    print('wrapper')

    def inner(*args):
        print('inner')
        print('开始装饰')
        func(*args)
        print('装饰结束')

    return inner


# 当有多个装饰器时，下从最下面的装饰器依次向上执行
@testa
@wrapper
def test(val):
    print('test')
    print(val)


# test(333)

'''
带参装饰器
'''


def params_fun(a, b):
    print(a)
    c = a + b

    def wrapper(func):
        def inner(*args):
            print(b)
            print(c)
            print('开始装饰')
            func(*args)
            print('装饰结束')

        return inner

    return wrapper


# def test1(a):
#     print(a)
# wrapper = params_fun(1, 2)
# test1 = wrapper(test1)
# test1('sssssssss')

@params_fun(1, 2)
def test1(a):
    print(a)


test1('111')
