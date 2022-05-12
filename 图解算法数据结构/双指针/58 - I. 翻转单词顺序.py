#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 58 - I. 翻转单词顺序.py
# @Time      : 2022/3/17 14:10
# @Author    : weilig
'''
剑指 Offer 58 - I. 翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
注意：本题与主站 151 题相同：https://leetcode-cn.com/problems/reverse-words-in-a-string/

注意：此题对比原题有改动
'''


class Solution(object):
    def reverseWords(self, s):
        """
        分析:
            通过字符串切割，将单次全部切割出来,通过列表反转在进行拼接
        :type s: str
        :rtype: str
        """
        res = [i for i in s.split(' ') if i]
        res.reverse()
        return ' '.join(res)


if __name__ == '__main__':
    s = "  hello world!  "
    res = Solution().reverseWords(s)
    print(res)
