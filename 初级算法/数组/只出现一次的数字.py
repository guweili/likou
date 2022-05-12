#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 只出现一次的数字.PY
# @Time      : 2021/12/1 9:31
# @Author    : weilig

'''

只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例2:

输入: [4,1,2,1,2]
输出: 4

'''

'''
异或运算

任何数和自己做异或运算，结果为 0; a^a=0
任何数和 0 做异或运算，结果还是自己; a^0 = a
异或运算中，满足交换律和结合律，也就是a^b^a = b^a^a = b^(a^a) = b^0 = b

'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce

        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    a = Solution().singleNumber(nums)
    print(a)
