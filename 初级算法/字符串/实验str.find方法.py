#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 实验str.find方法.PY
# @Time      : 2021/12/17 15:56
# @Author    : weilig

'''
实现 strStr()
实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 

示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        right = len(needle)  # 获取目标字符串长度
        if right == 0:
            return 0

        n = len(haystack)
        left = 0
        while right <= n - left:
            if haystack[left:left + right] == needle:
                return left

            left += 1

        return -1


if __name__ == '__main__':
    haystack = ''
    needle = ''
    a = Solution().strStr(haystack, needle)
    print(a)
