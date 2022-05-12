#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 53 在排序数组中查找数字.PY
# @Time      : 2022/1/19 14:18
# @Author    : weilig
'''
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

'''


class Solution(object):
    def search(self, nums, target):
        """
        """
        l, r = 0, len(nums) - 1
        count = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                count += 1
                nums.pop(mid)
                r -= 1  # 删除当前索引的值后，需要将r的下标减1，定位到之前的值

        return count


if __name__ == '__main__':
    a = [5, 7, 7, 8, 8, 10]
    res = Solution().search(a, 6)
    print(res)
    print(a)
