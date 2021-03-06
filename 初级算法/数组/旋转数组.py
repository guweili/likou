#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 旋转数组.PY
# @Time      : 2021/11/29 10:12
# @Author    : weilig
'''
给你一个数组，将数组中的元素向右轮转 k个位置，其中k是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

'''

'''
不新增数组，在原有的数组上进行操作，通过指针来定位所需要的旋转零界点

1. 通过切片进行操作，然后拼接
'''


class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        print(k)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(num, k)
