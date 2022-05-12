#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 28 对称二叉树.py
# @Time      : 2022/2/22 16:45
# @Author    : weilig
'''
剑指 Offer 28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
     2    2
    / \  / \
   3  4 4   3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

         1
        / \
      2    2
       \    \
       3     3

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 常用数据结构实现.如何实现树 import Tree, TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        分析:
            根据是否对称，可以通过栈的特性，进行消除，栈最后剩余一个根元素，则可以认为，这是个对称二叉树, 如下图所示
            [1]
            [1,2]
            [1,2,2]
            [1]栈顶元素2，2消除
            [1,3]
            [1,3,4]
            [1,3,4,4]栈顶元素4，4消除
            [1,3]
            [1,3,3]栈顶元素3，3消除
            [1]

        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]  # 队列
        inn = [root.val]  # 根节点入栈
        while queue:
            node = queue.pop(0)  # 取队列第一个元素
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if len(inn) > 0 and inn[-1] == node.val:  # 当前节点是否和栈顶元素相等
                inn.pop(-1)  # 栈顶元素出栈
            else:
                inn.append(node.val)  # 入栈

        return len(inn) == 0 or len(inn) == 4


if __name__ == '__main__':
    item = [1, 2, 2, None, 3, None, 3]
    tree = Tree()
    tree.add_batch(item)
    res = Solution().isSymmetric(tree.root)
    print(res)
