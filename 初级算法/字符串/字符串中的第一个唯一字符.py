#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 字符串中的第一个唯一字符.PY
# @Time      : 2021/12/14 15:15
# @Author    : weilig

'''

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

'''


class Solution(object):
    # def firstUniqChar(self, s):
    #     """
    #     通过字典存储计数方法，判断第一个唯一字符
    #     :type s: str
    #     :rtype: int
    #     """
    #     dic = {}
    #     for i, v in enumerate(s):
    #         if v in dic.keys():
    #             dic[v] += 1
    #         else:
    #             dic[v] = 1
    #
    #     for i, v in enumerate(s):
    #         if dic[v] == 1:
    #             return i
    #
    #     return -1

    def firstUniqChar(self, s):
        """
        通过 find 和 rfind 查询下表是否相等，达到判断第一个唯一字符
        :type s: str
        :rtype: int
        """
        for v in s:
            index = s.find(v)
            if index == s.rfind(v):
                return index

        return -1


if __name__ == '__main__':
    s = "leetcode"
    Solution().firstUniqChar(s)
    pass
