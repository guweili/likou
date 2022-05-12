#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 05替换空格.PY
# @Time      : 2022/1/19 11:10
# @Author    : weilig
'''
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

'''


class Solution(object):
    def replaceSpace(self, s):
        st = ""
        for i in s:
            if i == " ":
                i = "%20"
            st += i

        return st
