#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 如何实现树.PY
# @Time      : 2021/12/27 9:42
# @Author    : weilig
'''
树的结构特点:
    1. 当前根节点有多个子节点的类型称为树
    2. 当前节点最多有两个节点才被称为二叉树

示例：
二叉树：[3,9,20,null,null,15,7],

                          3
                       /     \
                      9       20
                    /   \     / \
                  null null  15  7

根据如图所示，构建二叉树类
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        '''
        构建树节点
        :param val: 当前节点值
        :param left: 左子节点内存地址
        :param right: 右子节点内存地址
        '''
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self):
        '''

        '''
        self.length = 0
        self.size = 0
        self.root = None

    def is_empty(self):
        '''
        判断是否为根节点
        :return:
        '''
        if self.root == None:
            return True
        else:
            return False

    def add_root(self, val):
        '''
        创建根节点
        :return:
        '''
        if self.root:
            raise ValueError('Root exists')

        self.root = TreeNode(val)
        self.size += 1

    def add_batch(self, items: list):
        '''
        批量插入
        :return:
        '''
        self.add_root(items.pop(0))
        for val in items:
            self.append(val)

    def append(self, val):
        item = TreeNode(val)
        queue = [self.root]  # 通过队列先进先出，接收每层有多少个节点，从根节点开始
        while True:
            node: TreeNode = queue.pop(0)
            if node.val is None:  # 如果此节点值为none直接跳过，在其他节点插入
                continue

            if node.left is None:
                node.left = item
                self.size += 1
                break
            elif node.right is None:
                node.right = item
                self.size += 1
                break
            else:
                queue.append(node.left)
                queue.append(node.right)

    def breadth_find(self, val):
        '''
        查询指定节点, 广度优先
        :param item: 节点值
        :return:
        '''
        queue = [self.root]
        while True:
            if not len(queue):
                return None
            node: TreeNode = queue.pop(0)
            if node.val == val:
                return node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def depth_find(self, val, node: TreeNode):
        '''
        深度查找, 递归查找
        :param item:
        :param node:
        :return:
        '''
        if node is None:
            return
        elif node.val == val:
            return node

        left = self.depth_find(val, node.left)
        if left:
            return left

        right = self.depth_find(val, node.right)
        if right:
            return right

    def isValidBST(self, root):
        '''
        有效 二叉搜索树定义如下：
        节点的左子树只包含 小于 当前节点的数。
        节点的右子树只包含 大于 当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。
        :param item:
        :param node:
        :return:
        '''

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

    def create_tree(self, nodes: list):
        root = nodes.pop(0)
        self.add_root(root)
        self.add_batch(nodes)


if __name__ == '__main__':
    items = [2, 1, 3]
    tree = Tree()
    tree.add_batch(items)
    find = tree.breadth_find(3)
    find2 = tree.depth_find(3, tree.root)
    res = tree.isValidBST(tree.root)
    pass
