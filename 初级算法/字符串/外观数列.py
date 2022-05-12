#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 外观数列.PY
# @Time      : 2021/11/30 9:50
# @Author    : weilig
'''
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

'''
import copy


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start_res = '1'

        for i in range(1, n + 1):
            pointer1 = 0  # start_res 字符串的初始索引

            if i == 1:
                continue

            count = 1  # 计数
            pointer1_val = start_res[pointer1]  # 记录初始值，与后续值作比较
            length = len(start_res)
            new_res = ''

            for e in range(1, length):
                if length == 1:
                    continue

                if start_res[e] == pointer1_val:
                    count += 1
                else:
                    new_res += '{}{}'.format(count, pointer1_val)
                    pointer1 = e
                    pointer1_val = start_res[e]
                    count = 1  # 计数

            new_res += '{}{}'.format(count, pointer1_val)

            start_res = new_res

        return start_res


if __name__ == '__main__':
    n = 6
    res = Solution().countAndSay(n)
    print(res)
