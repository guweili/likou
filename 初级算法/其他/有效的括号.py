#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 有效的括号.PY
# @Time      : 2022/1/7 11:43
# @Author    : weilig
'''
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true

'''


class Solution(object):
    def isValid(self, s):
        """
        使用栈的特性，来检测是否符合题目要求
        :type s: str
        :rtype: bool
        """
        flag = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        stack = []  # 构建栈
        for i in s:
            if stack and i == stack[-1]:  # 判断栈顶是否相同
                stack.pop()  # 出栈
            else:
                i = flag.get(i, None)
                stack.append(i)

        return False if stack else True


if __name__ == '__main__':
    s = "(){}}{"
    res = Solution().isValid(s)
    print(res)
