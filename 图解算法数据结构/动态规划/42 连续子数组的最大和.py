#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 42 连续子数组的最大和.py
# @Time      : 2022/2/23 11:16
# @Author    : weilig
'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        分析：
            如果前一项值小于0，当前值记作本身，大于0时，修改成 i + i-1, 最后结果为下列表
            [-2, 1, -2, 4, 3, 5, 6, 1, 5]
            获取列表最大值就行
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution().maxSubArray(nums)
    print(res)
