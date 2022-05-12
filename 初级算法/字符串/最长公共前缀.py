#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 最长公共前缀.PY
# @Time      : 2021/12/21 9:24
# @Author    : weilig
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''


class Solution(object):
    def longestCommonPrefix(self, strs: list):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs, key=len)  # 获取最短字符串
        flag = strs.pop(strs.index(shortest))
        for v in strs:
            flag1 = ''
            for i, e in enumerate(flag):
                if i == 0 and v[i] != e:
                    return ''
                if v[i] == e:
                    flag1 += e
                else:
                    break

            if flag1 == '':
                break

            flag = flag1

        return flag


if __name__ == '__main__':
    strs = ["flower", "flow", "fight"]
    res = Solution().longestCommonPrefix(strs)
    print(res)
