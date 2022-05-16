#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : with  上下文管理器.py
# @Time      : 2022/5/16 10:01
# @Author    : weilig
'''
对比传统的打开文件方式，
为预防打开文件流错误，
所以需要用到try语句异常处理，
同时也是为了无论能否正常打开文件，
最后都要关闭文件流
'''

# try:
#     file = open('1.txt', 'r')
#     file_data = file.read()
#     print(file_data)
# except Exception as e:
#     print(e)
# finally:
#     file.close()  # 关闭文件

'''
通过with方式打开文件
不需要异常处理，
也不需要手动关闭文件流
'''
# with open('1.txt', 'r') as f:
#     file_data = f.read()
#     print(file_data)

'''
如何使用上下文管理器:
第一种  类方式自定制上下文管理器
'''

# class File:
#     def __init__(self, file_name, file_mode):
#         self.file_name = file_name
#         self.file_mode = file_mode
#
#     def __enter__(self):
#         # 可以在这里构建数据库连接和游标
#         print('我执行了enter魔法方法')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # 数据库操作完成后在这里关闭数据库连接
#         print('我执行了exit魔法方法')
#
#     def read(self):
#         print('我执行了了read方法')
#
#
# with File('1.txt', 'r') as f:
#     print('执行with内部代码')
#     file_data = f.read()
#     print('执行完成')

'''
我执行了enter魔法方法
执行with内部代码
我执行了了read方法
执行完成
None None None
我执行了exit魔法方法

根据上述的结果可知，
如果是数据库操作时，可以通过enter方法先构建数据库连接和游标对象，然后在with中使用自定制方法，和后续的游标对象进行数据库的读写操作，
然后将with中的数据操作执行完成后，在exit中构建数据库关闭等操作。
'''

# 第二种：函数式上下文
from contextlib import contextmanager


@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        # 通过yield返回file对象，等待with中的操作完成后，执行finally关闭操作
        yield file
    except Exception as e:
        print(e)
    finally:
        file.close()  # 关闭文件


with my_open('1.txt', 'r') as f:
    file_data = f.read()
    print(file_data)
