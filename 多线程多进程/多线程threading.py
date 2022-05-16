#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 多线程threading.py
# @Time      : 2022/5/13 15:14
# @Author    : weilig
'''
threading模块包含下面的类：

Thread：基本线程类
Lock：互斥锁
RLock：可重入锁，使单一进程再次获得已持有的锁(递归锁)
Condition：条件锁，使得一个线程等待另一个线程满足特定条件，比如改变状态或某个值。
Semaphore：信号锁。为线程间共享的有限资源提供一个”计数器”，如果没有可用资源则会被阻塞。
Event：事件锁，任意数量的线程等待某个事件的发生，在该事件发生后所有线程被激活
Timer：一种计时器
Barrier：Python3.2新增的“阻碍”类，必须达到指定数量的线程后才可以继续执行。
'''
import time

import threading

'''
有两种方式来创建线程：一种是继承Thread类，并重写它的run()方法；
另一种是在实例化threading.Thread对象的时候，将线程要执行的任务函数作为参数传入线程。
'''

# 第一种方法：
# class MyThread(threading.Thread):
#     def __init__(self, thread_name):
#         # 注意：一定要显式的调用父类的初始化函数。
#         super(MyThread, self).__init__(name=thread_name)
#
#     def run(self):  # 重写Thread.run方法
#         print("%s正在运行中......" % self.name)
#
#
# for i in range(10):
#     MyThread("thread-" + str(i)).start()


# 第二种方法：
# def show(arg):
#     time.sleep(1)
#     print('thread ' + str(arg) + " running....")
#
#
# for i in range(10):
#     t = threading.Thread(target=show, args=(i,))
#     t.start()


# 在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务，比如下面的例子：
# def doWaiting():
#     print('start waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))
#
#
# t = threading.Thread(target=doWaiting)
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start job')
# print('end job')


# 有时候我们希望主线程等等子线程，不要“埋头往前跑”。那要怎么办？使用join()方法！如下所示：
# def doWaiting():
#     print('start waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))
#
#
# t = threading.Thread(target=doWaiting)
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start join')
# # 将一直堵塞，直到t运行结束。
# t.join()
# print('end join')


# 我们还可以使用setDaemon(True)把所有的子线程都变成主线程的守护线程，当主线程结束后，守护子线程也会随之结束，整个程序也跟着退出。
# def run():
#     print(threading.current_thread().getName(), "开始工作")
#     time.sleep(2)  # 子线程停2s
#     print("子线程工作完毕")
#
#
# for i in range(3):
#     t = threading.Thread(target=run, )
#     t.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
#     t.start()
#
# time.sleep(1)  # 主线程停1秒
# print("主线程结束了！")
# print(threading.active_count())  # 输出活跃的线程数


# 自定制线程类
# class MyThreading(threading.Thread):
#
#     def __init__(self, func, arg):
#         super(MyThreading, self).__init__()
#         self.func = func
#         self.arg = arg
#
#     def run(self):
#         self.func(self.arg)
#
#
# def my_func(args):
#     """
#     你可以把任何你想让线程做的事定义在这里
#     """
#     print('线程执行', args)
#     pass
#
#
# obj = MyThreading(my_func, 123)
# obj.start()

'''
线程锁
由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。
当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。
为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。
线程锁用于锁定资源，可以同时使用多个锁，当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。
我们先看一下没有锁的情况下，脏数据是如何产生的。
'''

# def plus():
#     global number  # global声明此处的number是外面的全局变量number
#     for _ in range(1000000):  # 进行一个大数级别的循环加一运算
#         number += 1
#     print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
#
#
# number = 0

# for i in range(2):  # 用2个子线程，就可以观察到脏数据
#     t = threading.Thread(target=plus)
#     t.start()
#
# time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算。
# print("主线程执行完毕后，number = ", number)

'''
结果并不等于2,000,000，可以很明显地看出脏数据的情况。
这是因为两个线程在运行过程中，CPU随机调度，你算一会我算一会，在没有对number进行保护的情况下，就发生了数据错误。
如果想获得正确结果，可以使用join()方法，让多线程变成顺序执行，如下修改代码片段：
'''

# for i in range(2):
#     t = threading.Thread(target=plus)
#     t.start()  # 启动线程
#     t.join()  # 等待当前线程执行完，进入下次循环

'''
上面为了防止脏数据而使用join()的方法，其实是让多线程变成了单线程，
属于因噎废食的做法，正确的做法是使用线程锁。
Python在threading模块中定义了几种线程锁类，分别是：

Lock 互斥锁
RLock 可重入锁
Semaphore 信号
Event 事件
Condition 条件
Barrier “阻碍”

互斥锁Lock
互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。使用很简单，
初始化锁对象，然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。
'''

# number = 0
# lock = threading.Lock()
#
#
# def plus(lk):
#     global number  # global声明此处的number是外面的全局变量number
#     lk.acquire()  # 开始加锁
#     for _ in range(1000000):  # 进行一个大数级别的循环加一运算
#         number += 1
#     print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
#     lk.release()  # 释放锁，让别的线程也可以访问number
#
#
# for i in range(2):  # 用2个子线程，就可以观察到脏数据
#     t = threading.Thread(target=plus, args=(lock,))  # 需要把锁当做参数传递给plus函数
#     t.start()
# time.sleep(2)  # 等待2秒，确保2个子线程都已经结束运算。
# print("主线程执行完毕后，number = ", number)

'''
RLock的使用方法和Lock一模一样，只不过它支持重入锁。该锁对象内部维护着一个Lock和一个counter对象。
counter对象记录了acquire的次数，使得资源可以被多次require。
最后，当所有RLock被release后，其他线程才能获取资源。
在同一个线程中，RLock.acquire()可以被多次调用，利用该特性，可以解决部分死锁问题。

信号Semaphore
类名：BoundedSemaphore。这种锁允许一定数量的线程同时更改数据，它不是互斥锁。
比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队

信号Semaphore
类名：BoundedSemaphore。这种锁允许一定数量的线程同时更改数据，它不是互斥锁。比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队。
'''

# def run(n, se):
#     se.acquire()
#     print("run the thread: %s" % n)
#     time.sleep(1)
#     se.release()  # 释放线程
#
#
# # 设置允许5个线程同时运行
# semaphore = threading.BoundedSemaphore(5)
# for i in range(20):
#     t = threading.Thread(target=run, args=(i, semaphore))
#     t.start()

'''
事件Event
类名：Event

事件线程锁的运行机制：全局定义了一个Flag，如果Flag的值为False，那么当程序执行wait()方法时就会阻塞，如果Flag值为True，线程不再阻塞。
这种锁，类似交通红绿灯（默认是红灯），它属于在红灯的时候一次性阻挡所有线程，在绿灯的时候，一次性放行所有排队中的线程。
事件主要提供了四个方法set()、wait()、clear()和is_set()。
调用clear()方法会将事件的Flag设置为False。
调用set()方法会将Flag设置为True。
调用wait()方法将等待“红绿灯”信号。
is_set():判断当前是否"绿灯放行"状态
下面是一个模拟红绿灯，然后汽车通行的例子：
'''

# event = threading.Event()
#
#
# def lighter():
#     green_time = 5  # 绿灯时间
#     red_time = 5  # 红灯时间
#     event.set()  # 初始设为绿灯
#     while True:
#         print("\33[32;0m 绿灯亮...\033[0m")
#         time.sleep(green_time)
#         event.clear()  # Flag设置为False
#         print("\33[31;0m 红灯亮...\033[0m")
#         time.sleep(red_time)  # 等待红灯5秒后
#         event.set()  # Flag设置为True
#
#
# def run(name):
#     while True:
#         if event.is_set():  # 读取信号量是否放行
#             print("一辆[%s] 呼啸开过..." % name)
#             time.sleep(1)
#         else:
#             print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
#             event.wait()
#             print("[%s] 看到绿灯亮了，瞬间飞起....." % name)
#
#
# light = threading.Thread(target=lighter)
# light.start()  # 信号量线程控制信号状态
#
# for name in ['奔驰', '宝马', '奥迪']:
#     car = threading.Thread(target=run, args=(name,))
#     car.start()

'''
条件Condition
类名：Condition

Condition称作条件锁，依然是通过acquire()/release()加锁解锁。
wait([timeout])方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
notify()方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池），其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
notifyAll()方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
下面的例子，有助于你理解Condition的使用方法：
'''

# num = 0
# con = threading.Condition()  # 条件锁
#
#
# class Foo(threading.Thread):
#
#     def __init__(self, name, action):
#         super(Foo, self).__init__()
#         self.name = name
#         self.action = action
#
#     def run(self):
#         global num
#         con.acquire()  # 加锁
#         print("%s开始执行..." % self.name)
#         while True:
#             if self.action == "add":
#                 num += 1
#             elif self.action == 'reduce':
#                 num -= 1
#             else:
#                 exit(1)
#             print("num当前为：", num)
#             time.sleep(1)
#             if num == 5 or num == 0:
#                 print("暂停执行%s！" % self.name)
#                 con.notify()  # 获得锁定
#                 con.wait()  # 释放当前锁
#                 print("%s开始执行..." % self.name)
#         con.release()  # 解锁
#
#
# a = Foo("线程A", 'add')
# b = Foo("线程B", 'reduce')
# a.start()
# b.start()


'''
定时器Timer
定时器Timer类是threading模块中的一个小工具，用于指定n秒后执行某操作。一个简单但很实用的东西。
'''

# from threading import Timer
#
#
# def hello():
#     print("hello, world")
#
#
# # 表示1秒后执行hello函数
# t = Timer(1, hello)
# t.start()

'''
通过with语句使用线程锁
所有的线程锁都有一个加锁和释放锁的动作，非常类似文件的打开和关闭。
在加锁后，如果线程执行过程中出现异常或者错误，没有正常的释放锁，那么其他的线程会造到致命性的影响。
通过with上下文管理器，可以确保锁被正常释放。其格式如下：
'''


# 构建上下文管理器
class MyLock:
    _lock = threading.Lock()

    def __enter__(self):
        print('上锁')
        self._lock.acquire()  # 上锁

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('解锁')
        self._lock.release()  # 解锁


_lock = MyLock()
# _lock = threading.Lock()
num = 0


def add():
    global num
    with _lock:
        for i in range(1000000):
            num += 1


for i in range(2):  # 用2个子线程，就可以观察到脏数据
    t = threading.Thread(target=add)
    t.start()

time.sleep(2)
print("主线程执行完毕后，number = ", num)
