#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 计数质数.PY
# @Time      : 2022/1/5 17:24
# @Author    : weilig
'''
计数质数
统计所有小于非负整数 n 的质数的数量。

 

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0
 

提示：

0 <= n <= 5 * 106
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0  # 记录质数个数
        td = [True] * n  # 给出的数字大小设置数组长度
        for i in range(2, n):
            if td[i]:
                count += 1
                for j in range(i * i, n, i):  # 根据当前i的值，i * i 之前的质数，已经将td数组的非质数状态修改成false，所以直接   2 = 4,6,8,10    3 = 9,12  根据这个性，进行修改, 可减少重复操作
                    td[j] = False

        return count


if __name__ == '__main__':
    n = 100
    res = Solution().countPrimes(n)
    print(res)
