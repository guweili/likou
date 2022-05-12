#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 50 第一次出现一次的字符.PY
# @Time      : 2022/1/21 14:44
# @Author    : weilig
'''
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = ""
输出：' '
'''


class Solution(object):
    # def firstUniqChar(self, s):
    #     """
    #     通过哈希表，进行查找
    #     :type s: str
    #     :rtype: str
    #     """
    #     dic = {}  # 哈希表
    #     queue = []  # 队列
    #     for i in s:
    #         if i in dic.keys():
    #             dic[i] += 1
    #         else:
    #             dic[i] = 1
    #             queue.append(i)
    #
    #     for i in queue:
    #         if dic[i] == 1:
    #             return i
    #
    #     return ' '

    def firstUniqChar(self, s):
        dic = {}
        for i in s:
            dic[i] = not i in dic
        for i in s:
            if dic[i]:
                return i
        return ' '


if __name__ == '__main__':
    s = "leetcode"
    Solution().firstUniqChar(s)
