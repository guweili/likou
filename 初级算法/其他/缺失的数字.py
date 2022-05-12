#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 缺失的数字.PY
# @Time      : 2022/1/10 10:10
# @Author    : weilig
'''
缺失数字
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

 

示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        异或运算
        a^a=0；自己和自己异或等于0
        a^0=a；任何数字和0异或还等于他自己
        a^b^c=a^c^b；异或运算具有交换律

        根据上述的异或运算特性，可以计算出，那个数字只出现一次，最后就只会剩下他
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)  # 获取数组长度, 根据题意要求，数组本身长度始终要少一个元素, 所以需要在最后，比较下数组的长度的最大值，因为那个值在循环中不会出现
        flag = 0
        for i in range(length):  # 当length=3时，只循环 0，1，2 ,所以后续需要将length进行异或运算
            flag ^= nums[i] ^ i

        return flag ^ length


if __name__ == '__main__':
    nums = [1]
    res = Solution().missingNumber(nums)
    print(res)
