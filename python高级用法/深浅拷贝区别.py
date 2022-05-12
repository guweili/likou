#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 深浅拷贝区别.PY
# @Time      : 2022/1/5 14:14
# @Author    : weilig
'''
不可变数据类型时 ------ 浅拷贝
'''
import copy

print('不可变数据类型时 ------ 浅拷贝')

# int
a = 1
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a = 2
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

# str
a = 'aaaa'
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a = 'bbbb'
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

# tuple
a = (1, 2, 3)
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a = (4, 5)
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

'''
不可变数据类型时 ------ 深拷贝
'''
print('不可变数据类型时 ------ 深拷贝')

# int
a = 1
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a = 2
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

# str
a = 'aaaa'
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a = 'bbbb'
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

# tuple
a = (1, 2, 3)
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a = (1, 2, 3, 4)
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

print('''
结论： 
    1. 不可变数据类型，浅拷贝和深拷贝，修改a的值，b的值不会变, 因为b指向的是不可变类型的内存地址，修改a只是把当前指向a的地址，指向其他地方
''')

'''
可变数据类型---浅拷贝
'''
print('可变数据类型---浅拷贝')
# list
a = [1, 2, 3]
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a.append(4)
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

# dict
a = {'a': 1, 'b': 2}
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a['a'] = 3
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

print('可变数据类型夹带可变数据类型---浅拷贝')
# list
a = [1, 2, 3, [4, 5]]
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a[-1][0] = 10
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
print(f'浅拷贝子项可变数据类型查看 a : {a[-1]} ----- b : {b[-1]}')
print(f'浅拷贝子项可变数据类型地址 a : {id(a[-1])} ----- b : {id(b[-1])}')

# dict
a = {'a': 1, 'b': {'c': 3}}
b = copy.copy(a)
print(f'浅拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a['b']['c'] = 4
print(f'浅拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'浅拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
print(f'浅拷贝子项可变数据类型查看 a : {a["b"]} ----- b : {b["b"]}')
print(f'浅拷贝子项可变数据类型地址 a : {id(a["b"])} ----- b : {id(b["b"])}')

print('''
结论:
    1. 可变数据类型浅拷贝，是实实在在的复制一份出来，a和b的内存地址不相同，在a上面做修改，b是不会有任何改变
    2. 当可变数据类型中存在可变数据类型，修改a的可变数据类型，b中的可变数据类型也会跟着改变, 因为a中的可变数据类型地址和b中的可变数据类型地址指向相同，
''')

'''
可变数据类型---深拷贝
'''
print('可变数据类型---深拷贝')
# list
a = [1, 2, 3]
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a.append(4)
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

# dict
a = {'a': 1, 'b': 2}
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a['a'] = 3
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')

print('可变数据类型夹带可变数据类型---深拷贝')
# list
a = [1, 2, 3, [4, 5]]
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a[-1][0] = 10
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
print(f'深拷贝子项可变数据类型查看 a : {a[-1]} ----- b : {b[-1]}')
print(f'深拷贝子项可变数据类型地址 a : {id(a[-1])} ----- b : {id(b[-1])}')

# dict
a = {'a': 1, 'b': {'c': 3}}
b = copy.deepcopy(a)
print(f'深拷贝此时 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝此时 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
a['b']['c'] = 4
print(f'深拷贝修改后 a, b 值分别为 a : {a} ----- b : {b}')
print(f'深拷贝修改后 a, b 内存地址 a : {id(a)} ----- b : {id(b)}')
print(f'深拷贝子项可变数据类型查看 a : {a["b"]} ----- b : {b["b"]}')
print(f'深拷贝子项可变数据类型地址 a : {id(a["b"])} ----- b : {id(b["b"])}')

print('''
结论：
    1. 可变数据类型深拷贝，无论a的子项如何修改，b的内容不会发生任何改变，b所有内容都是独立复制一份出来的
''')
