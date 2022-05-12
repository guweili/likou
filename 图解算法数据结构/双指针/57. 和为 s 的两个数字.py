#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 57. 和为 s 的两个数字.py
# @Time      : 2022/3/17 11:09
# @Author    : weilig
'''
剑指 Offer 57. 和为 s 的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        分析:
            一个递增的数组，找到两个数相加的和等于 target ，通过双指针进行查找
            1. 一个指针从数组的头部开始，一个指针从尾部开始进行相加，结果大于 target 尾部的数索引减 1
            2. 如果target大于两数之和，则头部索引加1，依次交替执行，可以得到两数
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]

            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(nums, target)
    print(res)
