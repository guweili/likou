#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 如何实现栈.PY
# @Time      : 2022/1/5 16:41
# @Author    : weilig
'''
栈结构特点:
    1. 后进先出
    入口            出口
    -------      -------
    |        f         |
    |        e         |
    |        d         |
    |        c         |
    |        b         |
    |        a         |
    | -----------------|

根据上述特点，实现栈类
'''


class Stack:
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

    def batch_push(self, vals):
        '''
        批量插入
        :return:
        '''
        for val in vals:
            self.push(val)


if __name__ == '__main__':
    # vals = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    vals = [[], [-2], [0], [-3], [], [], [], []]
    stack = Stack()
    stack.batch_push(vals)
    top = stack.top()
    print(top)
    pass
