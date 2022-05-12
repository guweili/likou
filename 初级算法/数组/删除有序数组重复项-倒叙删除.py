#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 删除有序数组重复项-倒叙删除.py
# @Time      : 2021/11/26 11:33
# @Author    : weilig

'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 2, 2, 3, 4]
    solution = Solution()
    solution.removeDuplicates(nums)
