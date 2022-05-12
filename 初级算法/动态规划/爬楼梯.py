#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 爬楼梯.PY
# @Time      : 2022/1/4 14:39
# @Author    : weilig

'''
爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

根据规律推导下列公式
F(1) = 1
F(2) = 2
F(3) = F(1) + F(2)
...
F(n) = F(n-1) + F(n-2)
'''


class Solution:
    def climbStairs(self, n) -> int:
        if n <= 2:
            return n

        first, second, count = 1, 2, 0
        for i in range(n - 2):
            count = first + second
            first, second = second, count

        return count


if __name__ == '__main__':
    n = 10
    Solution().climbStairs(n)
