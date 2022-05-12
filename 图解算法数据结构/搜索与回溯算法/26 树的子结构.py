#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 26 树的子结构.py
# @Time      : 2022/2/18 16:50
# @Author    : weilig
'''
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

        3
       / \
     4    5
    / \
   1   2
给定的树 B：

      4
     /
    1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 常用数据结构实现.如何实现树 import Tree, TreeNode


class Solution(object):
    def isSubStructure(self, A, B):
        """
        分析：
            使用前序遍历，进行比较，b子树是否存在a数中
            前序遍历，先将左节点找完后，然后再找右节点如下图
                        1
                       / \
                      2   3
                    / \  / \
                   4  5 6   7
                  /    \
                 8     9

            [1,2,4,8,5,9,3,6,7] 前序遍历获取的元素
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not B:
            return False

        def son_node(son_a, son_b):  # 匹配后续子节点是否相同
            if son_b is None:
                return True

            if getattr(son_a, 'val', None) == getattr(son_b, 'val', None):  # 判断节点是否为空
                return son_node(son_a.left, son_b.left) and son_node(son_a.right, son_b.right)
            else:
                return False

        def tree(base_tree):  # 查询根节点是否相同
            if not base_tree:  # 当前节点没有值，跳出递归
                return False

            if base_tree.val == B.val:  # 判断当前节点值是否相等
                if son_node(base_tree, B):
                    return True

            return tree(base_tree.left) or tree(base_tree.right)  # 判断是否有一个为true

        return tree(A)


if __name__ == '__main__':
    a = [10, 12, 6, 8, 3, 11]
    a_tree = Tree()
    a_tree.add_batch(a)
    b = [10, 12, 6, 8]
    b_tree = Tree()
    b_tree.add_batch(b)
    # b_tree.root = TreeNode(None)
    res = Solution().isSubStructure(a_tree.root, b_tree.root)
    print(res)
