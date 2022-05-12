#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 将有序数组转化为二叉搜索树.PY
# @Time      : 2021/12/30 14:53
# @Author    : weilig
'''
将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
'''
from 常用数据结构实现.如何实现树 import TreeNode


class Solution:
    def sortedArrayToBST(self, nums):
        '''
        因为是排序好的数组，所以取其中间值为树的根节点，左边的为左分支节点，右边的为右分支节点
        :param nums:
        :return:
        '''

        def bst(num):
            if not num:
                return None

            root_index = len(num) // 2  # 获取列表中间值的索引
            node = TreeNode(num[root_index])

            node.left = bst(num[:root_index])  # 树左边值
            node.right = bst(num[root_index + 1:])  # 树右边值

            return node

        return bst(nums)


if __name__ == '__main__':
    a = [1, 3]
    res = Solution().sortedArrayToBST(a)
    pass
