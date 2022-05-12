#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 63 股票最大利润.py
# @Time      : 2022/2/23 10:51
# @Author    : weilig
'''
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

'''


class Solution(object):
    def maxProfit(self, prices):
        """
        分析：
            根据题意 '一次' 买卖股票最大的利润是多少, 可以记录数组的最小值 , 然后记录最大值 , 才能得到最大利润
            必须是顺序执行, 不能 7-1
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        price_min = prices[0]  # 获取列表第一个值
        price_max = 0  # 假设股票利润为0

        for i in range(len(prices) - 1):  # 最后一天没有买的必要, 所以范围为 数组长度-1
            if price_min > prices[i]:  # 记录最小数值
                price_min = prices[i]

            if prices[i + 1] - price_min > price_max:  # 用后一天的价格去比较最小值，结果如果大于最大值，则修改最大值
                price_max = prices[i + 1] - price_min

        return price_max


if __name__ == '__main__':
    n = []
    res = Solution().maxProfit(n)
    print(res)
