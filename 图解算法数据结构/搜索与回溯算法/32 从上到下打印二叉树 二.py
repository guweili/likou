#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 从上到下打印二叉树 二.PY
# @Time      : 2022/1/27 16:55
# @Author    : weilig
'''
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [[root]]  # 队列
        res = []
        if root:
            while queue:
                item = []
                tree_list = []
                trees = queue.pop(0)
                for tree in trees:
                    item.append(tree.val)
                    if tree.left:
                        tree_list.append(tree.left)

                    if tree.right:
                        tree_list.append(tree.right)

                if tree_list: queue.append(tree_list)
                res.append(item)

        return res


if __name__ == '__main__':
    from 常用数据结构实现.如何实现树 import TreeNode, Tree

    root = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    tree.add_batch(root)
    res = Solution().levelOrder(tree.root)
    print(res)
