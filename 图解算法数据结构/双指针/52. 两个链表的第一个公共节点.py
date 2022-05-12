#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 52. 两个链表的第一个公共节点.py
# @Time      : 2022/3/17 9:33
# @Author    : weilig
'''

剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

'''
from 常用数据结构实现.如何实现链表 import LinkNode


class Solution:
    def getIntersectionNode(self, headA, headB):
        '''
        通过字典进行存储：
            将链表进行循环，获取的节点val作为key， 字典的value+1, 判断字典的value是否为2，如果为2直接跳出循环，就是当前节点
        :param headA:
        :param headB:
        :return:
        '''
        pa = headA
        pb = headB
        dic = {}
        while True:
            if pa and pa.val in dic.keys():
                return pa
            else:
                dic[pa.val] = 1
                pa = headA.next

            if pb and pb.val in dic.keys():
                return pb
            else:
                dic[pb.val] = 1
                pb = pb.next


if __name__ == '__main__':
    l1 = [4, 1, 8, 4, 5]
    link1 = LinkNode()  # 构建链表对象
    link1.batch_add(l1)
    l2 = [5, 0, 1, 8, 4, 5]
    link2 = LinkNode()  # 构建链表对象
    link2.batch_add(l2)
    res = Solution().getIntersectionNode(link1.head, link2.head)
    pass
