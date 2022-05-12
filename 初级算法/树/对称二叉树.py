#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 对称二叉树.PY
# @Time      : 2021/12/30 11:03
# @Author    : weilig

'''
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
'''

from 常用数据结构实现.如何实现树 import Tree, TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        通过循环添加到队列中，然后根据每层的关系，第一层为 2**0 个数 ， 第二层为 2**1 个数， 第三层 2**2, 然后根据每层的个数，去切割队列的长度，
        通过数组倒叙，跟原数组进行比较，是否相等
        :param root:
        :return:
        '''
        if root is None:
            return True

        queue = [root.left, root.right]
        while queue:  # 循环所有节点
            left: TreeNode = queue.pop(0)
            right: TreeNode = queue.pop(0)
            if left == None and right == None:  # 都为空进入下次循环
                continue

            if left == None or right == None:  # 有一个为空,说明不对称,直接返回false
                return False

            if left.val != right.val:  # 值不相同，不对称
                return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True


if __name__ == '__main__':
    a = [1,2,2,3,4,4,3]
    tree = Tree()
    tree.create_tree(a)
    res = Solution().isSymmetric(tree.root)
    pass
