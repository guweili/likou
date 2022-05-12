#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 10 青蛙跳台阶.py
# @Time      : 2022/2/23 10:13
# @Author    : weilig
'''
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
'''


class Solution:
    def numWays(self, n: int) -> int:
        '''
        分析:
            假设台阶为n,当 时
            n=1  1                                       0+1
            n=2  1,1   2                                 1+1
            n=3  1,1,1    1,2   2,1                      1+2
            n=4  1,1,1,1  1,1,2  2,1,1  2,2  1,2,1       2+3
            ...
            根据分析得知，有多少级台阶，就有多少种方法(斐波那契数列)
            当台阶为n时，方法为 f(n) = f(n-1) + f(n-2)
        :param n:
        :return:
        '''
        if n == 0 or n == 1:
            return 1

        a = 1  # 记录n-2的值
        b = 1  # 记录n-1 的值
        for i in range(2, n + 1):
            sum = (a + b) % 1000000007
            a = b
            b = sum

        return b


if __name__ == '__main__':
    n = 3
    res = Solution().numWays(n)
    print(res)
