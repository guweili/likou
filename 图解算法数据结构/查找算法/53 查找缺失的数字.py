#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 53 查找缺失的数字.PY
# @Time      : 2022/1/19 15:00
# @Author    : weilig
'''
剑指 Offer 53 - II. 0～n-1 中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution(object):
    # def missingNumber(self, nums):
    #     """
    #     使用等差数列求和，然后和源数组相减，结果为最终结果
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     count1 = n * (1 + n) / 2  # 等差数列求和
    #     count2 = sum(nums)
    #     return int(count1 - count2)

    # def missingNumber(self, nums):
    #     """
    #     位运算处理, 异或运算具有交换律  a^a = 0,  a^b = b^a, a^b^a = b
    #     0 异或任何数为 0 根据这个特性
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     res = 0
    #     for i in range(len(nums)):
    #         res ^= nums[i] ^ (i + 1)
    #     return res

    def missingNumber(self, nums):
        """
        二分查找, 通过下标比较  num[i] = i 如果相等，证明数组左边没有缺失，向右边查找，反之则去左边查找
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == mid:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    res = Solution().missingNumber([0, 1, 3])
    print(res)
