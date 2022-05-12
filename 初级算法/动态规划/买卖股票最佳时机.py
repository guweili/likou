#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 买卖股票最佳时机.PY
# @Time      : 2022/1/4 15:15
# @Author    : weilig
'''
买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num_min = prices[0]  # 记录最小值
        price_max = 0  # 记录交易最大值

        for i in range(len(prices) - 1):
            if num_min > prices[i]:
                num_min = prices[i]

            if prices[i + 1] - num_min > price_max:
                price_max = prices[i + 1] - num_min

        return price_max


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    Solution().maxProfit(prices)
