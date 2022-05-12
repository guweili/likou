#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 09.用两个栈实现队列.PY
# @Time      : 2022/1/12 10:47
# @Author    : weilig
'''
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

'''


# 两个栈实现队列
# class CQueue(object):
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def appendTail(self, value):
#         """
#         :type value: int
#         :rtype: None
#         """
#         self.stack1.append(value)
#
#     def deleteHead(self) -> int:  # 考虑队列先入先出
#         val = -1
#         if len(self.stack2):
#             val = self.stack2.pop()
#         else:
#             while self.stack1:
#                 tmp = self.stack1.pop()  # 将栈1的数据依次出栈，放入栈2中
#                 self.stack2.append(tmp)
#             if self.stack2:  # 判断栈2是否有值存在， 然后将栈顶的元素出栈
#                 val = self.stack2.pop()
#
#         return val

# 用队列实现
class CQueue(object):
    def __init__(self):
        self.queue = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)

    def deleteHead(self):  # 考虑队列先入先出
        if len(self.queue):
            val = self.queue.pop(0)
        else:
            val = -1

        return val

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
