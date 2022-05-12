#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 有效字符异位.PY
# @Time      : 2021/12/15 10:18
# @Author    : weilig
'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
'''


class Solution(object):
    # def isAnagram(self, s, t):
    #     """
    #     通过哈希表判断是否为异位
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     if len(s) != len(t):
    #         return False
    #
    #     s_dic = {}
    #     t_dic = {}
    #     for i in range(len(s)):
    #         if s[i] in s_dic.keys():
    #             s_dic[s[i]] += 1
    #         else:
    #             s_dic[s[i]] = 0
    #
    #         if t[i] in t_dic.keys():
    #             t_dic[t[i]] += 1
    #         else:
    #             t_dic[t[i]] = 0
    #
    #     for k, v in s_dic.items():
    #         if k not in t_dic.keys() or v != t_dic[k]:
    #             return False
    #
    #     return True

    def isAnagram(self, s, t):
        """
        通过排序，判断字符串是否相等
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        s.sort()
        s = ''.join(s)

        t = list(t)
        t.sort()
        t = ''.join(t)

        if s == t:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    res = Solution().isAnagram(s, t)
    print(res)
