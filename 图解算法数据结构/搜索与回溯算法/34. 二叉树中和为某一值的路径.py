#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 34. 二叉树中和为某一值的路径.py
# @Time      : 2022/3/18 14:44
# @Author    : weilig
'''
剑指 Offer 34. 二叉树中和为某一值的路径
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

示例 1：
            5
           /\
          4  8
         /   /\
        11  13 4
       /\      /\
      7 2     5  1
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：
    1
   / \
  2  3
输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：
输入：root = [1,2], targetSum = 0
输出：[]
'''
import copy

from 常用数据结构实现.如何实现树 import Tree


class Solution(object):
    def pathSum(self, root, target):
        """
        分析:
            根据题意可知树的最底层到根节点相加的和等于target,可以逆向分析:
            从根节点一直网下加，加到最底节点值是否和target相等，不相等回退到上个节点继续相加，
            直到相等，把路径走过的节点存储在列表中，
            零界值分析，当到最底节点特点为 count 为多个节点和
            node.left = None   node.right = None   count + node.val = target

        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(tree_node, count):
            if not tree_node or tree_node.val is None:
                return

            path.append(tree_node.val)
            count += tree_node.val
            if count == target and tree_node.left is None and tree_node.right is None:
                res.append(copy.copy(path))

            dfs(tree_node.left, count)
            dfs(tree_node.right, count)
            path.pop()

        res, path = [], []
        dfs(root, 0)

        return res


if __name__ == '__main__':
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    tree = Tree()
    tree.add_batch(root)
    target = 22
    res = Solution().pathSum(tree.root, target)
    print(res)
