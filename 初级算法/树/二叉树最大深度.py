#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 二叉树最大深度.PY
# @Time      : 2021/12/30 10:52
# @Author    : weilig
'''
二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

'''
from 常用数据结构实现.如何实现树 import TreeNode, Tree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        # 左边的深度
        left = self.maxDepth(root.left)
        # 右边的深度
        right = self.maxDepth(root.right)
        # 当前节点的最大深度等于，左右子节点的最大深度 + 1
        return max(left, right) + 1


if __name__ == '__main__':
    a = [9, 20, None, None, 15, 7]
    tree = Tree()
    tree.add_root(3)
    tree.add_batch(a)
    res = Solution().maxDepth(tree.root)
    pass
