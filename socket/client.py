#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : client.py
# @Time      : 2022/3/1 15:55
# @Author    : weilig
import json
import socket
import time

buffer_size = 1024

p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.connect(('127.0.0.1', 8080))
while 1:
    '''  客户端发送消息  '''
    # msg = input('please input')
    # # 防止输入空消息
    # if not msg:
    #     continue
    # p.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码
    # if msg == '1':
    #     break

    '''  客户端接收消息  '''
    ran = p.recv(buffer_size).decode('utf-8')
    print('ran', json.loads(ran))

p.close()
