#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 25. 合并两个排序的链表.py
# @Time      : 2022/3/15 17:08
# @Author    : weilig
'''
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
'''
from 常用数据结构实现.如何实现链表 import LinkNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        分析：
            递归调用返回最小值，然后记录
            1. 当 l1 < l2时, l1的下个节点和l2的当前节点进入递归，继续比较,将后续的返回的值记录在l1:
                l1.next = self.mergeTwoLists(l1.next, l2)
            2.当 l1 > l2时, l2的下个节点和l1的当前节点进入递归，继续比较,将后续的返回的值记录在l2:
                l2.next = self.mergeTwoLists(l1, l2.next)

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    l1 = [1, 2, 4]
    link1 = LinkNode()  # 构建链表对象
    link1.batch_add(l1)
    l2 = [1, 3, 4]
    link2 = LinkNode()  # 构建链表对象
    link2.batch_add(l2)
    Solution().mergeTwoLists(link1.head, link2.head)
