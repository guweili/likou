#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 22. 链表中倒数第 k 个节点.py
# @Time      : 2022/3/15 16:35
# @Author    : weilig
'''
剑指 Offer 22. 链表中倒数第 k 个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
'''
from 常用数据结构实现.如何实现链表 import LinkNode


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        分析:
            k值为，从后往前取第k个节点，可以通过双指针进行范围的控制，始终让快慢指针相距k个节点，
            然后判断快指针指向的节点 next 属性是否为 None，来判断是否走到链表的尾部，
            最后返回慢指针指向的节点，就是所获取的节点
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        left, right = head, head
        count = 0  # 间距
        while left:
            left = left.next  # 快指针走向下个节点
            if k == count:  # 间距是否与约定的相等
                right = right.next  # 慢指针走向下个节点
            else:
                count += 1

        return right


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    k = 3
    link = LinkNode()  # 构建链表对象
    link.batch_add(head)
    res = Solution().getKthFromEnd(link.head, k)
    pass
