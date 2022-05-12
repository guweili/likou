#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 移动零.PY
# @Time      : 2021/12/3 9:46
# @Author    : weilig

'''
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''

'''
解法:
1. 冒泡排序
2. 将0删除，后续补零
'''


class Solution(object):
    def moveZeroes(self, nums):
        # """
        # 冒泡排序
        # :type nums: List[int]
        # :rtype: None Do not return anything, modify nums in-place instead.
        # """
        # end_index = 0
        # for start_index, num in enumerate(nums):
        #     if num:
        #         nums[end_index], nums[start_index] = nums[start_index], nums[end_index]
        #         end_index += 1

        """
       将0删除，后续补零
       :type nums: List[int]
       :rtype: None Do not return anything, modify nums in-place instead.
       """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
