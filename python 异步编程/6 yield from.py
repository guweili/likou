#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 6 yield from.py
# @Time      : 2022/5/13 9:51
# @Author    : weilig
'''
其实在上面的例子一里面已经有协程返回值的影子了:
　　　　　　...
　　　　　　try:
　　　　　　　　a.send(666)  # 给yield发送数据, 执行x = 666,打印: end, recived value: 666 并报错StopIteration
　　　　　　　　　　　　　　# 此时协程继续向下执行,知道遇到下一个yield,或终止(StopIteration)
　　　　　　except StopIteration as s: # 捕获异常,并获取返回值
　　　　　　　　print(s, s.value) # 666 666
　　　　想获取整个协程的返回值,必然需要等到协程终止,而判断协程终止必然会有StopIteration情况出现;
　　　　而yield from则集中处理了这些异常,并且实现返回值的功能.(这也是我说例子5是yield转变为yield from的简单机制的原因)
　　　　yield from 可以简单理解为: for x in iterable: yield x;即生成器嵌套.
　　　　但是yield from 的功能不仅如此.
　　　　其主要功能为:
　　　　　　打开双向通道,把最外层的调用方与最内层的子生成器连接起来,这样二者可以直接发送和产出值,
　　　　　　还可以直接传入异常,而不用在协程中添加大量处理异常的代码.
'''

from collections import namedtuple

Result = namedtuple('Result', 'count average')  # 具名元组


# 子生成器: 原始逻辑处理
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield total  # 位置3
        if term is None:  # 位置6
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# 委派生成器: yield from: 中间管道,连接子生成器和客户端,让双方数据直接对接
def grouper(results, key):
    while True:  # 位置7
        results[key] = yield from averager()  # 位置2  等协程执行完成后续返回的 Result(count, average) 结果会返回给  results[key] 接收


def report(results):
    # 格式化打印结果
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print('{:2}{:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


# 客户端调用,调用方,向子生成器输送数据,运行逻辑
def main(data):
    results = {}
    for key, values in data.items():  # 位置8
        group = grouper(results, key)  # 位置0
        next(group)  # 位置1
        for value in values:  # 位置4
            print('接收返回值', group.send(value))
        group.send(None)  # 位置5

    # print(results)
    report(results)


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)

'''
运行流程：
    1. main函数处开始调用,到位置1处调用grouper,并执行next()进行预激活;(这里表明: yield from 和 自动预激活装饰器不兼容)
    2. 进入grouper()函数,进行while True循环,执行到yield from处(位置2),然后到该处暂停,开始执行averager()函数;(委派生成器开始阻塞,只作为调用通道)
    3. 进入averager()函数,一直运行到位置3处,term = yield,暂停在"="右侧,开始执行yield表达式,此时yield右侧为空,返回None给客户端(main)
    4. 回到1处(None值接不接收无所谓),进入位置4处的for循环,开始遍历values,并将value的值send到位置3处;(此时子生成器和客户端已经实现数据对接)
    5. 此时运行位置3处"="的左侧,即term = value,term拿到客户端发送过来的值,然后如上进行循环计算;
　　 6. 直到位置4处的循环结束,进入位置5,客户端发送给term一个None的值,子生成器进入位置6,中断循环,并return具名元组Result到位置2;
　　 7. 此时运行位置2处"="的左侧,即results[key] = Result(count, average),赋值完毕后,到位置7处,开始下一个循环,又开始调用averager();
　　 8. 直到位置8处的for循环完毕,将results字典传入report函数打印出结果,整个流程结束;
　　 9. 至此,关于客户端(调用方,main函数)通过委派生成器(yield form, grouper函数)和子生成器(averager函数)完成数据对接完整过程完毕.
'''
