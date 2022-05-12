#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 两个数组的交集.PY
# @Time      : 2021/12/2 9:25
# @Author    : weilig

'''
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''


class Solution(object):
    # def intersect(self, nums1: list, nums2: list):
    #     """
    #     双指针, 循环做法
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     nums1.sort()
    #     nums2.sort()
    #
    #     index1 = 0
    #     index2 = 0
    #
    #     new_list = []
    #
    #     max_length = len(nums1) + len(nums2)  # 最多循环的次数
    #
    #     for i in range(max_length):
    #         try:
    #             value1 = nums1[index1]
    #             value2 = nums2[index2]
    #             if value1 == value2:
    #                 new_list.append(value2)
    #                 index1 += 1
    #                 index2 += 1
    #             else:
    #                 if value1 > value2:
    #                     index2 += 1
    #                 else:
    #                     index1 += 1
    #         except IndexError:
    #             break
    #
    #     return new_list

    def intersect(self, nums1: list, nums2: list):
        """
        字典哈希做法
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_dic1 = {}
        for num in nums1:
            if num in num_dic1:
                num_dic1[num] += 1
            else:
                num_dic1[num] = 1

        num_dic2 = {}
        for num in nums2:
            if num in num_dic2:
                num_dic2[num] += 1
            else:
                num_dic2[num] = 1

        new_list = []
        for k, v in num_dic1.items():
            if k in num_dic2:
                v = num_dic2[k] if v > num_dic2[k] else v
                for i in range(v):
                    new_list.append(k)

        return new_list


if __name__ == '__main__':
    nums1 = [0, 5, 8, 7, 2, 9, 7, 5]
    nums2 = [1, 4, 8, 9]
    Solution().intersect(nums1, nums2)
