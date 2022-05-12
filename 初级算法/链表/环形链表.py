#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 回纹链表.PY
# @Time      : 2021/12/24 14:35
# @Author    : weilig


'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
'''
from 初级算法.链表.合并两个有序的链表 import ListNode, Node


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    nodes = [Node(i) for i in [1, 2, 2, 1]]

    head = ListNode()
    for node in nodes:
        head.append(node)

    res = Solution().isPalindrome(head.head)
    print(res)
