#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 合并两个有序的链表.PY
# @Time      : 2021/12/23 15:51
# @Author    : weilig

'''

'''


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        '''
        判断是否为链表头部
        :return:
        '''
        if self.head == None:
            return True
        else:
            return False

    def append(self, node):
        '''
        尾部插入，判段是否
        :param node:
        :return:
        '''
        current_node = self.head
        if self.is_empty():
            self.head = node
        else:
            # 将下个节点的值付给current_node，一直往复判断最后一个节点的next是否为None
            while (current_node.next != None):
                current_node = current_node.next
            current_node.next = node

        self.length += 1


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next


if __name__ == '__main__':
    node1 = [Node(i) for i in [2]]  # 构建链表节点
    node2 = [Node(i) for i in [1]]  # 构建链表节点
    list1 = ListNode()  # 构建链表对象
    list2 = ListNode()  # 构建链表对象

    for node in node1:
        list1.append(node)

    for node in node2:
        list2.append(node)

    Solution().mergeTwoLists(list1.head, list2.head)
