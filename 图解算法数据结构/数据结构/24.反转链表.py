#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 24.反转链表.PY
# @Time      : 2022/1/12 15:44
# @Author    : weilig
'''
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

'''
from 常用数据结构实现.如何实现链表 import Node, LinkNode


class Solution(object):
    # def reverseList(self, head):
    #     """
    #     递归做法
    #     :type head: ListNode
    #     :rtype: List[int]
    #     """
    #     if not head:
    #         return None
    #
    #     if head.next:
    #         val = self.reverseList(head.next)
    #         old = val
    #
    #         while old.next:
    #             old = old.next
    #         old.next = Node(head.val)
    #
    #     else:
    #         val = Node(head.val)
    #
    #     return val

    def reverseList(self, head):
        if not head or not head.next:
            return head

        q = head
        p = head.next
        q.next = None

        while p and q:
            r = p.next
            p.next = q
            q = p
            p = r

        return q


if __name__ == '__main__':
    nodes = [Node(i) for i in [1, 2, 3, 4, 5]]  # 构建链表节点
    link = LinkNode()  # 构建链表对象

    for node in nodes:
        # link.add(node)
        link.append(node)

    res = Solution().reverseList(link.head)
    print(res)
