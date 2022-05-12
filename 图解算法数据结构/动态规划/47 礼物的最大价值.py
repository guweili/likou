#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 47 礼物的最大价值.py
# @Time      : 2022/2/23 13:55
# @Author    : weilig
'''
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入:
[
[1,3,1],
[1,5,1],
[4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
'''


class Solution:
    def maxValue(self, grid) -> int:
        '''
        分析:
            根据题目得知，从起点 0，0 开始 ， 只能向右或者向下进行移动一步, 如下所示:
            [
                [1,4,1],
                [2,5,1],
                [4,2,1]
            ]
            根据移动的结果计算得出坐标 0,1 = 4 ， 坐标 1，0 = 2

            第二轮循环:
             [
                [1,4,5],
                [2,9,1],
                [6,2,1]
            ]
        :param grid:
        :return:
        '''
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                grid[i][j] += max(grid[i - 1][j] if i > 0 else 0, grid[i][j - 1] if j > 0 else 0)
        return grid[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = Solution().maxValue(grid)
    print(res)
