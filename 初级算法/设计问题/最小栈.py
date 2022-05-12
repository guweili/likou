#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 最小栈.PY
# @Time      : 2022/1/5 15:03
# @Author    : weilig
'''
最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
 

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 

提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。
'''


class MinStack(object):
    def __init__(self):
        self.stack = []  # 创建一个空栈
        self.size = 0  # 记录栈的大小

    def push(self, val):
        '''
        入栈
        :return:
        '''
        self.stack.append(val)
        self.size += 1

    def pop(self):
        '''
        出栈
        :return:
        '''
        self.size -= 1
        return self.stack.pop()

    def top(self):
        '''
        获取栈顶元素
        :return:
        '''
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
