#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 二叉树的层序遍历.PY
# @Time      : 2021/12/30 14:12
# @Author    : weilig
'''
二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''

from 常用数据结构实现.如何实现树 import TreeNode, Tree


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            length = len(queue)
            node_list = []

            for i in range(length):
                node = queue.pop(0)
                node_list.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(node_list)

        return res


if __name__ == '__main__':
    a = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    tree.create_tree(a)
    res = Solution().levelOrder(tree.root)
    pass
