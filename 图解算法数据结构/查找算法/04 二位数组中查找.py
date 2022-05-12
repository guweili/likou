#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 04 二位数组中查找.PY
# @Time      : 2022/1/21 13:45
# @Author    : weilig
'''
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

'''


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        从18这个点开始看，像一个倒过来的二叉数，且根节点始终比左叶子节点大，比右叶子节点小
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix) - 1  # 行数(二叉树层高)
        res = False
        line = 0  # line 列数
        while row >= 0 and line < len(matrix[0]):
            node = matrix[row][line]
            if node > target:
                row -= 1
            elif node < target:
                line += 1
            else:
                res = True
                break

        return res


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    res = Solution().findNumberIn2DArray(matrix, target)
    print(res)
