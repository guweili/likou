#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 13. 机器人的运动范围.py
# @Time      : 2022/3/18 10:33
# @Author    : weilig
'''
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
'''


class Solution(object):
    def movingCount(self, m, n, k):
        """
        分析:
            根据题意可知， 假设x,y分别为横坐标纵坐标,
            范围 0<=x,y<m,n   且 a = x // 10 + x % 10     b = y // 10 + y % 10   a+b的和要等于K
            这个坐标才算成立，
            假设起点【0，0】开始 ,  m,n=3  k=1
            当 x = 0时 , 当x值确定时，y有且仅有唯一值  y=k-x ，根据这个特性y也是同理算法
            [0,1] [0,2] 当y为2时, x+y 刚好大于 K ,所以当x=0时，y=1   [0,1]
            当 x = 1时 ,  [1,0] [1,1]  1+1 >2 ，计算到这里时循环就结束了所以结果为 [1,0]
            计算Y的值时候也是一样，但要记住去重
            当y=0 , [0,0] [0,1] 重复计算了 [0,0]，需要记录
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        vis = set()

        def dfs(x, y):
            a = x // 10 + x % 10
            b = y // 10 + y % 10
            if (x, y) in vis or x >= m or y >= n or a + b > k:  # a + b 结果如果大于K，后续的循环没必要继续下去
                return 0
            vis.add((x, y))  # 记录坐标避免重复计算
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)  # 从0，0开始，可以不用判断是否大于0


if __name__ == '__main__':
    m = 3
    n = 2
    k = 17
    res = Solution().movingCount(m, n, k)
    print(res)
