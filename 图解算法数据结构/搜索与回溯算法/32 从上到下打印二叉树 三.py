#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 32 从上到下打印二叉树 三.PY
# @Time      : 2022/1/27 17:24
# @Author    : weilig
'''
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

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
  [20,9],
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
        index = 1
        if root:
            while queue:
                item = []
                tree_list = []
                trees = queue.pop(0)
                remainder = index % 2
                if remainder == 0:
                    trees.reverse()

                for tree in trees:
                    item.append(tree.val)
                    if tree.left:
                        tree_list.append(tree.left)

                    if tree.right:
                        tree_list.append(tree.right)

                if tree_list: queue.append(tree_list)
                res.append(item)
                index += 1

        return res


if __name__ == '__main__':
    from 常用数据结构实现.如何实现树 import TreeNode, Tree

    root = [1, 2, 3, 4, None, None, 5]
    # root = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    tree.add_batch(root)
    res = Solution().levelOrder(tree.root)
    print(res)
