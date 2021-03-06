#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 35.复杂链表复制.PY
# @Time      : 2022/1/12 17:10
# @Author    : weilig
'''
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
'''
from 常用数据结构实现.如何实现链表 import Node, LinkNode


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        dic = {}
        p = head
        while p:
            dic[p] = Node(p.val)
            p = p.next

        p = head
        while p:
            dic[p].next = dic.get(p.next)
            dic[p].random = dic.get(p.random)
            p = p.next

        return dic[head]


if __name__ == '__main__':
    nodes = [Node(i[0], i[1]) for i in [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]]  # 构建链表节点
    link = LinkNode()  # 构建链表对象
    for node in nodes:
        link.append(node)
    Solution().copyRandomList(link.head)
