#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 打家劫舍.PY
# @Time      : 2022/1/5 11:06
# @Author    : weilig
'''
打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


class Solution(object):
    def rob(self, nums):
        """
        dp 为累计最大值
        最大值--->  1. 要么当前为 i 的房间偷了，最大值为  num[i] + dp[i-2]
                  2. 要么当前为 i 的房间没偷， 最大值为上个累计值 dp[i-1]
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]

        dp = [0] * length
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        for i in range(2, length):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])  # 当前房间如果偷 num[i] + dp[i-2] 比较 当前房间不偷 dp[i-1] 最大值，赋给当前位置

        return max(dp)


if __name__ == '__main__':
    nums = [2, 1, 1, 2]
    res = Solution().rob(nums)
    print(res)
