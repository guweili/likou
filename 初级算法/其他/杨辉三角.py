#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 杨辉三角.PY
# @Time      : 2022/1/7 9:13
# @Author    : weilig
'''
杨辉三角
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。



 

示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]

'''


class Solution(object):
    def generate(self, numRows):
        """
                   1
                  1 1
                 1 2 1
                1 3 3 1
               1 4 6 4 1
        分析：
            1. 根据上述特性，每行的第一个和最后一个都是1
            2. 中间元素从每行的第二个元素开始到 n - 1个元素的计算公式为, n + (n - 1)
        :type numRows: int
        :rtype: List[List[int]]
        """
        line = []
        for i in range(numRows):  # 循环每列
            row = []
            for j in range(i + 1):  # 循环每行的元素
                if j == 0 or j == i:  # 是否为每行的第一个或最后一个元素
                    row.append(1)
                else:
                    the_first = line[i - 1]  # 获取前一行
                    val = the_first[j] + the_first[j - 1]
                    row.append(val)

            line.append(row)

        return line


if __name__ == '__main__':
    numRows = 5
    Solution().generate(numRows)
