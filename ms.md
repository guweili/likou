### 总结

1. RestfulApi 规范

```python
# 理解规范统一的接口
# 1. 未使用Rest规范之前，我们可能有增删改查 等接口，会设计出类似这样的接口: /xxx/newAdd (新增接口), /xxx/delete(删除接口), /xxx/query (查询接口), /xxx/uddate(修改接口)等这样的。增删改查有四个不同的接口，维护起来可能也不好。
# 2. Restful规范，请求只需要一个接口，比如设计该接口为 /xxx/apis 这样的一个接口就可以了，然后请求方式(method)有 GET--查询(从服务器获取资源); POST---新增(从服务器中新建一个资源); PUT---更新(在服务器中更新资源)，DELETE---删除(从服务器删除资源)，PATCH---部分更新(从服务器端更新部分资源) 等这些方式来做，服务器端返回的数据也可以是相同的，只是我们前端会根据状态码来判断请求成功或失败的状态值来判断。

# HTTP请求规范
# GET (SELECT): 查询；从服务器取出资源.
# POST(CREATE): 新增; 在服务器上新建一个资源。
# PUT(UPDATE): 更新; 在服务器上更新资源(客户端提供改变后的完整资源)。
# PATCH(UPDATE): 更新；在服务器上更新部分资源(客户端提供改变的属性)。
# DELETE(DELETE): 删除; 从服务器上删除资源。

# 返回数据格式
# RESTful规范中的请求应该返回统一的数据格式。对于返回的数据，一般会包含如下字段:
# 1) code: http响应的状态码。
# 2) status: 包含文本, 比如：'success'(成功), 'fail'(失败), 'error'(异常)
# 当status的值为 'fail' 或 'error'时，需要添加 message 字段，用于显示错误信息。
# 3) data: 当请求成功的时候, 返回的数据信息。 但是当状态值为 'fail' 或 'error' 时，data仅仅包含错误原因或异常信息等。
# 返回成功的响应JSON格式一般为如下:

{
    "code": 200,
    "status": "success",
    "data": [{
        "userName": "tugenhua",
        "age": 31
    }]
}

{
    "code": 401,
    "status": "error",
    "message": '用户没有权限',
    "data": null
}
```

2. python 协程

```python
'''
又称微线程,他能使用单线程实现并发任务的效果, 为此我们需要先回顾下并发的本质：切换+保存状态
cpu 运行任务时，会在两种情况下切走去执行其他任务，一种该任务发生了阻塞，另一种该任务执行时间过长，有更高效率的程序代替
1、协程：
    单线程实现并发
    在应用程序里控制多个任务的切换+保存状态
    优点：
        应用程序级别速度要远远高于操作系统的切换
    缺点：
        多个任务一旦有一个阻塞没有切，整个线程都阻塞在原地
        该线程内的其他的任务都不能执行了

        一旦引入协程，就需要检测单线程下所有的IO行为,
        实现遇到IO就切换,少一个都不行，以为一旦一个任务阻塞了，整个线程就阻塞了，
        其他的任务即便是可以计算，但是也无法运行了

2、协程序的目的：
    想要在单线程下实现并发
    并发指的是多个任务看起来是同时运行的
    并发=切换+保存状态
'''

# 串行执行
import time


def func1():
    for i in range(10000000):
        i + 1


def func2():
    for i in range(10000000):
        i + 1


start = time.time()
func1()
func2()
stop = time.time()
print(stop - start)


# 基于yield并发执行
def func1():
    while True:
        yield


def func2():
    g = func1()
    for i in range(10000000):
        i + 1
        next(g)


start = time.time()
func2()
stop = time.time()
print(stop - start)
# 上述的这种单纯cpu计算操作，通过yield频繁的切换func2 和func1，反而会降低运行效率

'''
二：第一种情况的切换。在任务一遇到io情况下，切到任务二去执行，这样就可以利用任务一阻塞的时间完成任务二的计算，效率的提升就在于此。
yield不能检测IO，实现遇到IO自动切换
'''
import time


def func1():
    while True:
        print('func1')
        yield


def func2():
    g = func1()
    for i in range(10000000):
        i + 1
        next(g)
        time.sleep(3)
        print('func2')


start = time.time()
func2()
stop = time.time()
print(stop - start)

'''
总结协程特点：
必须在只有一个单线程里实现并发
修改共享数据不需加锁
用户程序里自己保存多个控制流的上下文栈
附加：一个协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））
'''

# Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
import gevent


def eat(name):
    print('%s eat 1' % name)
    gevent.sleep(2)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    gevent.sleep(1)
    print('%s play 2' % name)


g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
g1.join()
g2.join()
# 或者gevent.joinall([g1,g2])
print('主')
```

3. django 中间件

```python
# 中间件的概念
# 中间件是Django请求与响应处理的钩子框架，是一个轻量级的插件系统。
# 中间件用于在视图函数执行之前和执行之后做一些预处理和后处理操作，功能类似装饰器。
# 它的表现形式是一个Python类。简而言之就是处理请求和响应。
# 
# process_request(self, request):
# 执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
# process_view(self, request, callback, callback_args, callback_kwargs):
# 调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
# process_template_response(self, request, response):
# 在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
# process_exception(self, request, exception)
# 当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
# process_response(self, request, response)
# 所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
```

4. gil 线程全局锁

```python
'''
CPython 使用引用计数来管理内存，所有 Python 脚本中创建的实例，都会有一个引用计数，来记录有多少个指针指向它。当引用计数只有 0 时，则会自动释放内存。
什么意思呢？我们来看下面这个例子：
import sys
a = []
b = a
sys.getrefcount(a)3复制代码这个例子中，a 的引用计数是 3，因为有 a、b 和作为参数传递的 getrefcount 这三个地方，都引用了一个空列表。
这样一来，如果有两个 Python 线程同时引用了 a，就会造成引用计数的 race condition，引用计数可能最终只增加 1，这样就会造成内存被污染。因为第一个线程结束时，会把引用计数减少 1，这时可能达到条件释放内存，当第二个线程再试图访问 a 时，就找不到有效的内存了。

所以说，CPython 引进 GIL 其实主要就是这么两个原因：
一是设计者为了规避类似于内存管理这样的复杂的竞争风险问题（race condition）；
二是因为 CPython 大量使用 C 语言库，但大部分 C 语言库都不是原生线程安全的（线程安全会降低性能和增加复杂度）。

细心的你可能会发现一个问题：为什么 Python 线程会去主动释放 GIL 呢？
毕竟，如果仅仅是要求 Python 线程在开始执行时锁住 GIL，而永远不去释放 GIL，那别的线程就都没有了运行的机会。
没错，CPython 中还有另一个机制，叫做 check_interval，意思是 CPython 解释器会去轮询检查线程 GIL 的锁住情况。
每隔一段时间，Python 解释器就会强制当前线程去释放 GIL，这样别的线程才能有执行的机会。

gil 内部机制
while True:
    acquire GIL
    for i in 1000:
        do something
    release GIL
    /* Give Operating System a chance to do thread scheduling */
'''
```

5. with 上下文管理器

```python
#     def __enter__(self):
#         # 可以在这里构建数据库连接和游标
#         print('我执行了enter魔法方法')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # 数据库操作完成后在这里关闭数据库连接
#         print('我执行了exit魔法方法')
```