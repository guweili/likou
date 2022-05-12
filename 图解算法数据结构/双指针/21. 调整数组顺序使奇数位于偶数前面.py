#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 21. 调整数组顺序使奇数位于偶数前面.py
# @Time      : 2022/3/17 10:14
# @Author    : weilig
'''
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
'''


class Solution(object):
    def exchange(self, nums):
        """
        分析：
            根据题意可知，当前元素如果是偶数时，就必须放到数组的末尾，基数放到首部，
            通过快慢指针进行定位掉换奇偶数的位置，
            1. 快指针移动到基数时，将慢指针的数值与之掉换，然后快慢指针各+1，进入下次循环
            2. 快指针移动到偶数时，快指针继续+1，慢指针不变
            通过上述这种方法，可以用慢指针定位偶数，快指针循环数组，迅速将元素进行替换
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, 0
        while left < len(nums):
            if nums[left] % 2 != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1

            left += 1

        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    res = Solution().exchange(nums)
    print(res)
