#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 整数反转.PY
# @Time      : 2021/12/10 14:33
# @Author    : weilig
'''

整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0

'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        status = x > 0
        x = x if status else -x  # 判断是否为负数
        while x != 0:
            res = res * 10 + x % 10  # 倒叙新值
            x //= 10

        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res if status else -res
        else:
            return 0


if __name__ == '__main__':
    a = 123
    res = Solution().reverse(a)
    print(res)
