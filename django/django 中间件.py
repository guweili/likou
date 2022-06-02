#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : django 中间件.py
# @Time      : 2022/5/16 17:18
# @Author    : weilig
'''
中间件的概念
中间件是Django请求与响应处理的钩子框架，是一个轻量级的插件系统。
中间件用于在视图函数执行之前和执行之后做一些预处理和后处理操作，功能类似装饰器。
它的表现形式是一个Python类。简而言之就是处理请求和响应。

process_request(self,request) :
执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
process_view(self, request, callback, callback_args, callback_kwargs):
调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
process_template_response(self,request,response):
在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
process_exception(self, request, exception)
当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
process_response(self, request, response)
所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
'''

import time
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# 限制用户访问次数,每60秒不超过5次
# 构建访问者IP池
visit_ip_pool = {}  # 以'ip'地址为键，以访问的网站的时间戳列表作为值形如{'127.0.0.1':[时间戳,...]}


class VisitLimitMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 获取用户的访问的ip地址
        ip = request.META.get("REMOTE_ADDR")
        # 获取访问时间
        visit_time = time.time()
        if ip not in visit_ip_pool:
            # 维护字典,将新的ip地址加入字典
            visit_ip_pool[ip] = [visit_time]
        else:
            # 已经存在，则将ip对应值的插入列表开始位置
            visit_ip_pool[ip].insert(0, visit_time)
        # 获取ip_list列表
        ip_list = visit_ip_pool[ip]
        # 计算访问时间差
        lead_time = ip_list[0] - ip_list[-1]
        print('地址:', ip, '访问次数:', len(ip_list), '时间差', lead_time)
        # 两个条件同时成立则，间隔时间在60s内
        while ip_list and lead_time > 60:
            # 默认移除列表中的最后一个元素
            ip_list.pop()
        # 间隔在60s内判断列表的长度即访问的次数是否大于5次
        if len(ip_list) > 5:
            return HttpResponse("对不起，访问过于频繁，将终止你的访问请求...")
        print('地址:', ip, '访问次数:', len(ip_list), '时间差', lead_time)
