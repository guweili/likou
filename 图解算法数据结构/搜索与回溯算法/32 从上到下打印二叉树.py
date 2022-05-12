#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 32 从上到下打印二叉树.PY
# @Time      : 2022/1/27 15:28
# @Author    : weilig
'''
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
'''

from 常用数据结构实现.如何实现树 import TreeNode, Tree


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]  # 队列
        res = []
        if not root:
            return res
        while queue:
            node = queue.pop(0)  # 获取当前节点
            res.append(node.val)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return res


if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    tree.add_batch(root)
    res = Solution().levelOrder(tree.root)
    print(res)
