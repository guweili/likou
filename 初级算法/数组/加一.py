#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 加一.PY
# @Time      : 2021/12/2 10:55
# @Author    : weilig

'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]

如果数组中的所有元素都是9，类似9999，加1之后肯定会变为10000，也就是数组长度会增加1位。
如果数组的元素只要有一个不是9，加1之后直接返回即可。

类似加法满10进一运算
'''


class Solution(object):
    def plusOne(self, digits: list):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(digits) + 1):
            index = -i  # 取最后尾数
            value = digits[index]
            if index == -1:
                value += 1

            if value == 10:
                digits[index] = 0
                try:
                    digits[index - 1] += 1
                except IndexError:
                    digits.insert(index - 1, 1)
                    break
            else:
                digits[index] = value
                break

        return digits


if __name__ == '__main__':
    digits = [4, 9, 9]
    Solution().plusOne(digits)
    pass
