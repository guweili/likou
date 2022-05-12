#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 03 数组中重复的数字.PY
# @Time      : 2022/1/19 11:34
# @Author    : weilig
'''
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
'''


class Solution(object):
    # def findRepeatNumber(self, nums):
    #     """
    #     哈希表实现查重
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     dic = {}
    #     for i in nums:
    #         if i in dic.keys():
    #             return i
    #         else:
    #             dic[i] = 1

    def findRepeatNumber(self, nums: list):
        """
        排序，双指针查重
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        for i in range(length - 1):
            first = nums[i]  # 第一个指针
            second = nums[i + 1]  # 第二个指针
            if first == second:
                return first


if __name__ == '__main__':
    Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
