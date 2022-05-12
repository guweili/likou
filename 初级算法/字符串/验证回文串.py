#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 验证回文串.PY
# @Time      : 2021/12/15 10:51
# @Author    : weilig
'''

验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

 

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串

'''
import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.findall("[a-z0-9]", s)
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s)
    print(res)
