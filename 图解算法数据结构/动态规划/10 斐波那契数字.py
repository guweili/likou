#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 10 斐波那契数字.py
# @Time      : 2022/2/22 17:27
# @Author    : weilig
'''
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,F(1)= 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
'''


class Solution:
    def fib(self, n: int):
        if n == 0:
            return 0
        a = 0
        b = 1
        for i in range(n):
            # 给定一个正整数p，任意一个整数n，一定存在等式 ：
            # n = kp + r
            # 1 = 0 * 1000000007 + 1
            # 1 -1 = 0 * 1000000007
            sum = (a + b) % 1000000007
            print(sum)
            a = b
            b = sum

        return a


if __name__ == '__main__':
    item = 10
    res = Solution().fib(item)
    print(res)
