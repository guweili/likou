#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 30.包含min函数的栈.PY
# @Time      : 2022/1/12 11:06
# @Author    : weilig
'''
剑指 Offer 30. 包含 min 函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

'''


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = []  # 将元素升序排列

    def push(self, x):
        """
        根据栈后进先出的特性，弄个辅助栈接收最小值,
        辅栈上次的值和这次的作比较，如果大于当前入栈值，则入栈，大于的就不入
        第一种情况:
            主栈  [0,1,2]     [0,1]     [0]
            辅栈  [0]         [0]       [0]
        第二种：
            主栈  [1,0,2]     [1,0]     [0]
            辅栈  [1,0]       [1,0]     [0]
        第三种：
            主栈  [2,1,0]     [2,1]     [2]
            辅栈  [2,1,0]     [2,1]     [2]

        根据辅栈的特性，只保留最小值，当删除主栈时，如果主栈出栈值和辅栈出栈值相等，
        则主栈当前的最小值以出栈，辅栈的最小值也应该出栈，使辅栈始终保留最小值
        """
        self.stack.append(x)
        if not self.min_val or self.min_val[-1] >= x:  # 将首次插入的值当作最小值，如果下次插入的值，没有上次插入的值
            self.min_val.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min_val[-1]:
            self.min_val.pop()  # 删除最小值
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
a = obj.min()
obj.pop()
b = obj.top()
param_4 = obj.min()
pass
