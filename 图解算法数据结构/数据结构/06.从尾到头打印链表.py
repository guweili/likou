#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 06.从尾到头打印链表.PY
# @Time      : 2022/1/12 15:23
# @Author    : weilig
'''
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
'''
from 常用数据结构实现.如何实现链表 import Node, LinkNode


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head is None:
            return []

        if head.next:
            val = self.reversePrint(head.next)
        else:
            val = []

        val.append(head.val)

        return val


if __name__ == '__main__':
    nodes = [Node(i) for i in [1, 3, 2]]  # 构建链表节点
    link = LinkNode()  # 构建链表对象

    for node in nodes:
        # link.add(node)
        link.append(node)

    res = Solution().reversePrint(link.head)
    print(res)
