#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 18 删除链表节点.py
# @Time      : 2022/3/14 15:03
# @Author    : weilig
'''
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
'''
from 常用数据结构实现.如何实现链表 import LinkNode


class Solution(object):
    def deleteNode(self, head, val):
        """
        分析：
            通过双指针记录当前节点和上一个节点值, 如果当前节点值是要删除的值，则将当前节点的next属性直接对接上上一节点的next上，将当前节点数值跳过,达到删除的目的
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next

        pre, cur = head, head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                break
            else:
                pre, cur = cur, cur.next
        return head


if __name__ == '__main__':
    head = [-3, 5, -99]
    val = -3
    link = LinkNode()  # 构建链表对象
    link.batch_add(head)
    res = Solution().deleteNode(link.head, val)
