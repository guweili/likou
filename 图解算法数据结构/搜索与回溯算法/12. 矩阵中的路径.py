#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 12. 矩阵中的路径.py
# @Time      : 2022/3/17 16:10
# @Author    : weilig
'''
剑指 Offer 12. 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
'''


class Solution(object):
    def exist(self, board, word):
        """
        分析：
            给出一个二位数组计算出，目标字符串是否
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "E", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    res = Solution().exist(board, word)
    print(res)
