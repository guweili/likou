#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 验证二叉搜索树.PY
# @Time      : 2021/12/30 10:52
# @Author    : weilig
'''

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
 

输入：root = [2,1,3]
输出：true

输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
 

提示：

树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1

'''
from 常用数据结构实现.如何实现树 import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归并引入上界，下界来判断是否有效的二叉搜索树
        def check(node, min_val=float('-inf'), max_val=float('inf')) -> bool:
            if not node:
                return True
                # 每个节点如果超过这个范围，直接返回false
            if node.val <= min_val or node.val >= max_val:
                return False
            # 这里再分别以左右两个子节点分别判断，
            # 左子树范围的最小值是minVal，最大值是当前节点的值，也就是root的值，因为左子树的值要比当前节点小
            # 右子数范围的最大值是maxVal，最小值是当前节点的值，也就是root的值，因为右子树的值要比当前节点大
            return check(node.left, min_val, node.val) and check(node.right, node.val, max_val)

        return check(root)
