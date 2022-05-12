#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 48 最长不含重复字符的字符串.py
# @Time      : 2022/2/23 17:35
# @Author    : weilig
'''
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        分析:
            双指针加集合实现最大长度
            通过快慢指针获取截取的字符串长度，然后将截取的部分通过集合去重在比较长度，是否相等
            1. 相等，则证明没有重复元素，快指针移动到下一个元素
            2. 不相等，则证明有重复元素，慢指针移动下一个元素
            上述操作一直重复执行
        :type s: str
        :rtype: int
        """
        max_length = 0  # 保留最大长度
        left_pointer, right_pointer = 1, 0  # 左为快指针，右为慢指针
        while len(s) >= left_pointer:
            a = s[right_pointer:left_pointer]
            res_set = set(a)
            if len(a) == len(res_set):
                max_length = max(len(a), max_length)  # 记录最大长度
                left_pointer += 1
            else:
                right_pointer += 1

        return max_length


if __name__ == '__main__':
    s = " "
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
