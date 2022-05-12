#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 46 把数字翻译成字符串.py
# @Time      : 2022/2/23 14:39
# @Author    : weilig
'''
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
'''


class Solution(object):
    def translateNum(self, num):
        """
        分析 :
            尝试分析前面几个计数:
            (1)如果只有一个数字的时候只有一种可能就是1
            (2)如果只有两个数字，如12，12大于等于0且小于等于25，则可以排布为两种可能:(1，2)，(12); 假如大于25，如28，则只有一种排布(2， 8);
            (3)如果有三个数字，如122，则有三种排布(1,2,2),(12,2),(1,22);若爲128,则只有两种排布(1,2,8),(12,8);
        由上面分析可知:
            (1)num只有一个数字dp[0] = 1
            (2)num有两个数字分为两种情况: num大于等于0且小于等于25，dp[1] = 2;否则dp[1] = 1
            (3)num有三个及三个以上数据:dp[i] = dp[i - 1] + dp[i - 2]且要求num[i - 1]不等于0，反之若num[i - 1]为0，则dp[i] = dp[i - 1];比如102，dp[2] = dp[1]; 122,dp[2] = dp[1] + dp[0]
        :type num: int
        :rtype: int
        """
        if num <= 1:
            return 1
        string = str(num)
        a, b = 1, 1

        for i in range(1, len(string)):
            if string[i - 1] != '0' and '0' <= string[(i - 1):(i + 1)] <= '25':
                a, b = b, a + b
            else:
                a = b

        return b


if __name__ == '__main__':
    num = 25
    Solution().translateNum(num)
