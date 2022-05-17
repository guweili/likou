'''
从上文的介绍和官方的定义来看，GIL无疑就是一把全局排他锁。毫无疑问全局锁的存在会对多线程的效率有不小影响。甚至就几乎等于Python是个单线程的程序。
那么读者就会说了，全局锁只要释放的勤快效率也不会差啊。只要在进行耗时的IO操作的时候，能释放GIL，这样也还是可以提升运行效率的嘛。
或者说再差也不会比单线程的效率差吧。理论上是这样，而实际上呢？Python比你想的更糟。
下面我们就对比下Python在多线程和单线程下得效率对比。测试方法很简单，一个循环1亿次的计数器函数。一个通过单线程执行两次，一个多线程执行。最后比较执行总时间。
测试环境为双核的Mac pro。注：为了减少线程库本身性能损耗对测试结果带来的影响，这里单线程的代码同样使用了线程。只是顺序的执行两次，模拟单线程。
顺序执行的单线程
'''
from threading import Thread
import time


# 计时器
def timepiece(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("Total time: {}".format(end_time - start_time))

    return inner


n = 100000000


@timepiece
def count_down():
    global n
    while n > 0:
        n -= 1


# count_down()  # 单线程模式
# Total time: 5.306222438812256

# 多线程模式下
# t1 = Thread(target=count_down)
# t2 = Thread(target=count_down)
# t3 = Thread(target=count_down)
# t4 = Thread(target=count_down)
# t1.start()
# t2.start()
# t3.start()
# t4.start()
#  Total time: 8.045806169509888


'''
多线程为什么会比单线程慢?
而是 Python 的线程失效了，没有起到并行计算的作用。
Python 的线程是不是假的线程？
Python 的线程，的的确确封装了底层的操作系统线程，在 Linux 系统里是 Pthread（全称为 POSIX Thread），而在 Windows 系统里是 Windows Thread。另外，Python 的线程，也完全受操作系统管理，比如协调何时执行、管理内存资源、管理中断等等。
所以，虽然 Python 的线程和 C++ 的线程本质上是不同的抽象，但它们的底层并没有什么不同。
为什么有 GIL？
看来我的两个猜想，都不能解释开头的这个未解之谜。那究竟谁才是“罪魁祸首”呢？事实上，正是我们今天的主角，也就是 GIL，导致了 Python 线程的性能并不像我们期望的那样。
GIL，是最流行的 Python 解释器 CPython 中的一个技术术语。它的意思是全局解释器锁，本质上是类似操作系统的 Mutex。每一个 Python 线程，在 CPython 解释器中执行时，都会先锁住自己的线程，阻止别的线程执行。
当然，CPython 会做一些小把戏，轮流执行 Python 线程。这样一来，用户看到的就是“伪并行”——Python 线程在交错执行，来模拟真正并行的线程。

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
