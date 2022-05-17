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

from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponse


class UserMiddlerware(MiddlewareMixin):
    def process_request(self, request):
        print("自定义process_request")
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        return None

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        print("自定义process_response")
        return response

    def process_exception(self, request, exception):
        return HttpResponse(exception)
