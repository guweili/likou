#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 27 二叉树的镜像.py
# @Time      : 2022/2/22 16:15
# @Author    : weilig
'''
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

        4
       / \
     2    7
   / \   / \
  1   3 6   9
镜像输出：

         4
       /  \
     7     2
    / \   / \
   9  6  3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
'''
from 常用数据结构实现.如何实现树 import Tree, TreeNode


class Solution(object):
    # def mirrorTree(self, root):
    #     """
    #     分析:
    #         根据镜像得知，可以使用队列进行广度遍历，依次执行获取元素，从而达到镜像的目的
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     queue = [root]
    #     res = []
    #     while queue:
    #         node = queue.pop(0)  # 获取第一个元素
    #         res.append(node)  # 添加元素
    #         if node.right:
    #             queue.append(node.right)  # 先添加右节点，再添加左节点
    #         if node.left:
    #             queue.append(node.left)
    #
    #     return res

    def mirrorTree(self, root):
        """
        分析:
            根据镜像得知，可以使用队列进行广度遍历，依次执行获取元素，从而达到镜像的目的
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        root.right, root.left = root.left, root.right
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        return root


if __name__ == '__main__':
    item = [4, 2, 7, 1, 3, 6, 9]
    tree = Tree()
    tree.add_batch(item)
    res = Solution().mirrorTree(tree.root)
    print(res)
