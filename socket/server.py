#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : server.py
# @Time      : 2022/3/1 15:54
# @Author    : weilig
import json
import random
import socket

# 明确配置变量
import time

values = [
    {
        'x': "1号",
        'y': 10,
        'y2': 20,
    },
    {
        'x': "2号",
        'y': 11,
        'y2': 20,
    },
    {
        'x': "3号",
        'y': 23,
        'y2': 30,
    },
    {
        'x': "4号",
        'y': 55,
        'y2': 35,
    },
    {
        'x': "5号",
        'y': 11,
        'y2': 25,
    },
    {
        'x': "6号",
        'y': 23,
        'y2': 15,
    },
    {
        'x': "7号",
        'y': 35,
        'y2': 5,
    },
    {
        'x': "8号预测",
        'y': 36,
        'y2': 50,
    },
]

ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024
# 创建一个TCP套接字
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 套接字类型AF_INET, socket.SOCK_STREAM   tcp协议，基于流式的协议
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 对socket的配置重用ip和端口号
# 绑定端口号
ser.bind(ip_port)  # 写哪个ip就要运行在哪台机器上
# 设置半连接池
ser.listen(back_log)  # 最多可以连接多少个客户端
while 1:
    # 阻塞等待，创建连接
    con, address = ser.accept()  # 在这个位置进行等待，监听端口号
    print('链接成功')
    while 1:
        try:
            '''  服务端接受消息  '''
            # 接受套接字的大小，怎么发就怎么收
            # msg = con.recv(buffer_size)
            # print('msg', msg)
            # if msg.decode('utf-8') == '1':
            #     # 断开连接
            #     con.close()
            # print('服务器收到消息', msg.decode('utf-8'))

            '''  服务端发送消息  '''
            ran = random.choice(values)
            ran = json.dumps(ran).encode('utf-8')
            print('ran', ran)
            con.send(ran)
            time.sleep(1)

        except Exception as e:
            break
# 关闭服务器
ser.close()
