#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 两数之和.PY
# @Time      : 2021/12/3 10:49
# @Author    : weilig

'''

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

'''


class Solution(object):
    def twoSum(self, nums: list, target):

        # """
        # 通过index查询耗费时间
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
        # new_list = []
        # for i, v in enumerate(nums):
        #     diff = target - v
        #
        #     try:
        #         index = nums.index(diff)
        #         if index == i:
        #             continue
        #     except ValueError:
        #         continue
        #
        #     new_list.append(i)
        #     new_list.append(index)
        #     break
        #
        # print(new_list)
        #
        # return new_list

        """
        通过字典存储，进行查询
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict_num = {}
        for i, v in enumerate(nums):
            diff = target - v

            if dict_num.get(diff) is not None:
                return dict_num.get(diff), i
            else:
                dict_num[v] = i

        print(dict_num)
        return 0, 0


if __name__ == '__main__':
    nums = [0, 4, 3, 0]
    target = 0
    a, b = Solution().twoSum(nums, target)
    print(a, b)
    pass
