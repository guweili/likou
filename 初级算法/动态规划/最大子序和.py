#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 最大子序和.PY
# @Time      : 2022/1/5 10:34
# @Author    : weilig
'''
最大子序和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。


示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解
'''


class Solution:
    # def maxSubArray(self, nums):
    #     '''
    #     动态规划
    #     :param nums:
    #     :return:
    #     '''
    #     n = len(nums)
    #     dp = [0] * n  # dp[i]表示前i个元素的最大子序和
    #     dp[0] = nums[0]  # 边界条件，第一个元素的最大子序和为它自己
    #     for i in range(1, n):
    #         if dp[i - 1] > 0:
    #             dp[i] = dp[i - 1] + nums[i]  # 如果前边元素的最大子序和是正数，就相加
    #         else:
    #             dp[i] = nums[i]  # 如果前边元素的最大子序和是负数，最大子序和就是当前元素
    #     return max(dp)

    def maxSubArray(self, nums):
        n = len(nums)
        a, b = nums[0], nums[0]

        for i in range(1, n):
            if a > 0:
                a += nums[i]  # 如果前边元素的最大子序和是正数，就相加
            else:
                a = nums[i]  # 如果前边元素的最大子序和是负数，最大子序和就是当前元素

            b = max(a, b)

        return b


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Solution().maxSubArray(nums)
