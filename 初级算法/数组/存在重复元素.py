#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 存在重复元素.PY
# @Time      : 2021/11/30 9:36
# @Author    : weilig
'''

给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        转化集合比较长度
        :type nums: List[int]
        :rtype: bool
        """
        import copy
        nums2 = copy.copy(nums)
        nums_set = set(nums2)
        if len(nums) == len(nums_set):
            return False
        else:
            return True
