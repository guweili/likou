#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : python描述器的深度解析.PY
# @Time      : 2022/2/9 10:35
# @Author    : weilig
'''
什么是描述器
简而言之，如果一个类中定义了__get__、__set__、__delete__中的任意一个，这个类的实例就可以叫做一个描述器，其功能强大，应用广泛，它可以控制访问属性、方法的行为，是属性、方法、静态方法、类方法、super函数背后的实现机制。

类型
描述符有__get__和__set__2个方法
非数据描述符只有一个__get__方法,通常用于方法。非数据描述符的优先级低于实例属性。
'''

# # 首先看一个例子，说明什么是描述器：
# class RevealAccess(object):
#     """A data descriptor that sets and returns values
#        normally and prints a message logging their access.
#     """
#
#     def __init__(self, initval=None, name='var'):
#         self.val = initval
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         print('Retrieving', self.name)
#         return self.val
#
#     def __set__(self, obj, val):
#         print('Updating', self.name)
#         self.val = val
#
#
# class MyClass(object):
#     x = RevealAccess(10, 'var "x"')
#     y = 5
#
#
# m = MyClass()
# print("=" * 20)
# print(m.x)
# print("=" * 20)
# m.x = 20
# print(m.x)
# print("=" * 20)
# print(m.y)
import types

'''
输出：
== == == == == == == == == ==
Retrieving
var
"x"
10
== == == == == == == == == ==
Updating
var
"x"
Retrieving
var
"x"
20
== == == == == == == == == ==
5

上面这个例子中：
创建m实例和普通类没什么区别，我们从m.x开始看
m.x是m实例调用了x这个类属性，然而这个类属性不是普通的值，而是一个描述器，所以我们从访问这个类属性变成了访问这个描述器
如果调用时得到的是一个描述器，python内部就会自动触发一套使用机制
访问的话自动触发描述器的__get__方法
修改设置的话就自动触发描述器的__set__方法
这里就是m.x触发了__get__方法，得到的是self.value的值，在前面__init__中定义的为10
m.x = 20
则触发了__set__方法，赋的值20传到value参数之中，改变了self.value的值，所以下一次m.x调用的值也改变了
'''

'''
描述器的访问
整个描述器的核心是__getattribute__()，因为对像任何属性的访问都会调用到这个特殊的方法。这个方法被用来查找属性，同时也是你的一个代理，调用它可以进行属性的访问操作。
一般我们的类的__getattribute__()方法都是继承自object，自己改写__getattribute__()是很危险的，也会阻止正常的描述器调用。__getattribute__()的Python描述原型如下：

def __getattribute__(self, key):
    "Emulate type_getattro() in Objects/typeobject.c"
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
       return v.__get__(None, self)
    return v
如果通过实例ins访问描述器，由__getattribute__()转化为：
type(ins).__dict__['attr'].__get__(ins, type(ins)
如果通过类Class访问描述器，由__getattribute__()转化为：
Class.__dict__['attr'].__get__(None, Class)
'''

# # 例二
# class Descriptor(object):
#     def __init__(self):
#         self.aaaa = 'anonymous'
#
#     def __get__(self, instance, owner):
#         print('instance: %s' % instance)
#         print('owner: %s' % owner)
#         print("Invoke __get__: %s" % self.aaaa)
#         return self.aaaa
#
#     def __set__(self, instance, name):
#         print("invoke __set__: %s" % name)
#         self.aaaa = name.title()
#
#     def __delete__(self, instance):
#         print("Invoke __delete__: %s" % self.aaaa)
#         del self.aaaa
#
#
# class Person(object):
#     name = Descriptor()
#
#
# # 通过类Person访问
# print(Person.name)
# # instance: None
# # owner: <class '__main__.Person'>
# # Invoke __get__: anonymous
# # anonymous
#
# print(Person.__dict__['name'].__get__(None, Person))
# # instance: None
# # owner: <class '__main__.Person'>
# # Invoke __get__: anonymous
# # anonymous
#
# user = Person()
#
# # 通过实例user访问， `owner`访问描述器实例的对象。`instance`则是访问描述器实例的实例
# print(user.name)
# # instance: <__main__.Person object at 0x7f88c5472dd0>
# # owner: <class '__main__.Person'>
# # Invoke __get__: anonymous
# # anonymous
#
# print(type(user).__dict__['name'].__get__(user, type(user)))
# # instance: <__main__.Person object at 0x7f0873fb5d90>
# # owner: <class '__main__.Person'>
# # Invoke __get__: anonymous
# # anonymous
#
# user.name = 'jack'
# # invoke __set__: jack
#
# del user.name
# # Invoke __delete__: Jack


'''
另外通过super访问，如SubPerson是Person的子类，super(SubPerson, subins).name)访问通过subins.__class__.__mro__查找到Person类，然后调用： Person.__dict__['name'].__get__(subins, Person)
'''

# # 例三
# class SubPerson(Person):
#     pass
#
#
# subins = SubPerson()
#
# print(subins.__class__.__mro__)
# # (<class '__main__.SubPerson'>, <class '__main__.Person'>, <class 'object'>)
#
# # 通过super访问
# print(super(SubPerson, subins).name)
# # instance: <__main__.SubPerson object at 0x7f30b1537f28>
# # owner: <class '__main__.Person'>
# # Invoke __get__: anonymous
# # anonymous
#
# print(Person.__dict__['name'].__get__(subins, Person))
# # instance: <__main__.SubPerson object at 0x7f30b1537f28>
# # owner: <class '__main__.Person'>
# # Invoke __get__: anonymous
# # anonymous

'''
访问的优先级
实例
上面提到实例ins访问描述器，实际是由__getattribute__()访问： type(ins).__dict__['attr'].__get__(ins, type(ins)。
具体实现是依据这样的优先顺序是：数据描述器 > 实例属性 > 非数据描述符 -> __getter__() 方法
如下，我们user.name = 'andy'我们通过实例对属性name赋值，但由于数据描述器优先级高于实例属性。赋值操作被数据描器中的__set__方法截获，我们在__set__忽略了重新赋值(当然也可以在其中更新赋值，但实质不是通过实例属性绑定的方式)。易见实例user的属性字典__dict__还是空的。
'''

# # 例四
# class Descriptor(object):
#     def __init__(self, name):
#         self.aaaa = name
#
#     def __get__(self, instance, owner):
#         print("Invoke __get__: %s" % self.aaaa)
#         return self.aaaa
#
#     def __set__(self, instance, name):
#         print("invoke __set__, ignore assignment.")
#
#     def __delete__(self, instance):
#         print("Invoke __delete__: %s" % self.aaaa)
#         del self.aaaa
#
#
# class Person(object):
#     name = Descriptor('jack')
#
#
# user = Person()
#
# print(user.name)
# # Invoke __get__: jack
# # jack
# print(user.__dict__)
# # {}
#
# user.name = 'andy'  # 实例属性赋值
# # invoke __set__, ignore assignment.
#
# print(user.name)
# # Invoke __get__: jack
# # jack
# print(user.__dict__)
# # {}

'''
再看非数据描述器和实例属性比较。user.name = 'andy'成功的把属性name绑定到user.__dict__中。
'''

# # 例五
# class Descriptor(object):
#     def __init__(self, name):
#         self.aaaa = name
#
#     def __get__(self, instance, owner):
#         print("Invoke __get__: %s" % self.aaaa)
#         return self.aaaa
#
#
# class Person(object):
#     name = Descriptor('jack')
#
#
# user = Person()
#
# print(user.name)
# # Invoke __get__: jack
# # jack
# print(user.__dict__)
# # {}
#
# user.name = 'andy'
#
# print(user.name)
# # andy
# print(user.__dict__)
# # {'name': 'andy'}

'''
从上述的三个例子中可以得出，实现了（get  set）方法的数据描述器 > 实例属性 > 实现了（get）方法的非数据描述符
'''

'''
类
如果通过类Class访问描述器，由__getattribute__()访问：Class.__dict__['attr'].__get__(None, Class)。
优先级是：类属性 > 描述器。
通过类对象Person.name = 'andy'更新属性name，并没有进入到描述器的__set__方法中，而且Person.__dict__中的属性name也由描述器<__main__.Descriptor object at 0x7f1a72df9710>更新为字符串'andy'。可见类属性的优先级高于描述器。

类属性 > 数据描述器 > 实例属性 > 非数据描述符 > __getter__() 方法
如果有__getattribute__方法，当__getattribute__出现异常时可能会调用__getter__()。
'''

# class Descriptor(object):
#     def __init__(self, name):
#         self.aaaa = name
#
#     def __get__(self, instance, owner):
#         print("Invoke __get__: %s" % self.aaaa)
#         return self.aaaa
#
#     def __set__(self, instance, name):
#         print("invoke __set__, ignore assignment.")
#
#     def __delete__(self, instance):
#         print("Invoke __delete__: %s" % self.aaaa)
#         del self.aaaa
#
#
# class Person(object):
#     name = Descriptor('jack')
#
#
# print(Person.__dict__)
# # {'__module__': '__main__', 'name': <__main__.Descriptor object at 0x7f1a72df9710>,
# # '__dict__': <attribute '__dict__' of 'Person' objects>, '__doc__': None, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
# # Invoke __get__: jack
#
# print(Person.name)
# # jack
# Person.name = 'andy'
#
# print(Person.__dict__)
# # {'__module__': '__main__', 'name': 'andy', '__dict__': <attribute '__dict__' of 'Person' objects>,
# # '__doc__': None, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
# print(Person.name)
# # andy


'''
函数都是非数据描述器
类字典将方法存储为函数。在类定义中，方法是用 def 或 lambda 这两个创建函数的常用工具编写的。方法与常规函数的不同之处仅在于第一个参数是为对象实例保留的。按照 Python 约定，实例引用称为 self ，但也可以称为 this 或任何其他变量名称。

为了支持方法调用，函数包含 __get__() 方法用于在访问属性时将其绑定成方法。这意味着所有函数都是非数据描述器，当从对象调用它们时，它们返回绑定方法。在纯 Python 中，它的工作方式如下:
'''

# class Function:
#     def __get__(self, obj, owner):
#         if obj is None:
#             return self
#         return types.MethodType(self, obj)
#
#     def __call__(self, *args, **kwargs):
#         print('使对象当作函数调用')
#
#
# class Test:
#     func = Function()
#
#
# test = Test()
# print(test.func)
# test.func()
# # <bound method ? of <__main__.Test object at 0x000001C051CF5860>>
# # 使对象当作函数调用

'''
使用property类创建描述器
class property(fget=None, fset=None, fdel=None, doc=None)，fget是获取属性的函数，fset是设置属性的函数，fdel是删除属性的函数，doc是这个属性的文档字符串。
'''

# class C:
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         print('invoke getx')
#         return self._x
#
#     def setx(self, value):
#         print('invoke setx')
#         self._x = value
#
#     def delx(self):
#         print('invoke delx')
#         del self._x
#
#     x = property(getx, setx, delx, "I'm the 'x' property.")
#
#
# ins = C()
#
# ins.x = 'property'
# # invoke setx
#
# print(ins.x)
# # invoke getx
# # property
#
# print(C.x.__doc__)
# # I'm the 'x' property.
#
# del ins.x
# # invoke delx

'''
纯python实现property
'''


class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('unreadable attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('unreadable attribute')
        self.fset(instance, value)

    def __del__(self, instance):
        if self.fdel is None:
            raise AttributeError('unreadable attribute')
        self.fdel(instance)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.doc)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fdel, fdel, self.doc)


class S:
    def __init__(self):
        self._s = 'sssss'

    @Property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value

    @s.deleter
    def s(self):
        del self._s


'''
在程序创建实例s之前，会先将装饰器和描述器先执行，将 Property 描述器执行装载到 s 实例的属性中,然后再通过描述器特性执行 __get__  __set__  __del__ 等方法触发在当前S类中的对应方法
'''
s = S()
# s.s = 2
print(s.s)
# del s.s
print(s.__dict__)
