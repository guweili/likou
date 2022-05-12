#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 旋转数组中的最小数字.PY
# @Time      : 2022/1/21 14:10
# @Author    : weilig
'''
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''


class Solution(object):
    def minArray(self, numbers):
        """
        通过双指针进行查询
        :type numbers: List[int]
        :rtype: int
        """
        left = -1
        right = -2
        res = numbers[0]
        while abs(right) <= len(numbers):
            l = numbers[left]
            r = numbers[right]
            if l < r:
                res = l
                break
            else:
                res = r
                left -= 1
                right -= 1

        return res


if __name__ == '__main__':
    numbers = [1, 3, 4]
    res = Solution().minArray(numbers)
    print(res)
