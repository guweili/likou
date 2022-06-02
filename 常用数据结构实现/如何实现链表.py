#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 如何实现链表.PY
# @Time      : 2021/12/22 10:03
# @Author    : weilig
'''
链表
链表是一种物理存储单元上非连续、非顺序的存储结构，数据元素的逻辑顺序是通过链表中的指针链接次序实现的。链表由一系列节点组成，这些节点不必在内存中相连。每个节点由数据部分Data和链部分Next，Next指向下一个节点，这样当添加或者删除时，只需要改变相关节点的Next的指向，效率很高。

链表数据接口特点：
    1. 每个节点都会有当前节点的值 val 和下一个值的内存地址 next， 最后一个节点next=None

  node1 = ['val':1, 'next': node2(obj)]
    |
  node2 = ['val':2, 'next': node3(obj)]
    |
  node3 = ['val':3, 'next': node4(obj)]
    |
  node4 = ['val':4, 'next': None]

类似于上述的特性，为单链表,根据上述实现单链表类
'''


class Node:
    def __init__(self, item, random=None):
        '''
        构建链表节点
        :param item:
        '''
        self.val = item
        self.next = None
        self.random = random

    def __str__(self):
        return self.val


class LinkNode:
    def __init__(self):
        '''
        构建链表
        '''
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

    def add(self, node):
        '''
        从头部添加
        :param node: 链表节点
        :return:
        '''
        if self.is_empty():
            self.head = node
        else:
            #
            node.next = self.head
            self.head = node

        self.length += 1

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

    def batch_add(self, values):
        nodes = [Node(i) for i in values]  # 构建链表节点
        for node in nodes:
            self.append(node)

    def insert(self, node, index):
        '''
        指定索引插入, 从0开始
        :param node:
        :param index:
        :return:
        '''
        if self.length < index or index < 0:
            raise IndexError('索引超出链表范围')

        current_node = self.head
        flag = 0
        while True:
            if flag == index == 0:
                node.next = current_node
                self.head = node
                self.length += 1
                break
            elif flag == index:
                node.next = current_node.next
                current_node.next = node
                self.length += 1
                break
            else:
                if flag > 0:
                    current_node = current_node.next
                flag += 1


if __name__ == '__main__':
    head = [4, 5, 1, 9]
    link = LinkNode()  # 构建链表对象
    link.batch_add(head)
