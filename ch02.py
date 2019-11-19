#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch02.py
@Time    :   2019/11/19 20:16:49
@Author  :   shaopf 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   Chapter 2
'''

def append_element(some_list, element):
    some_list.append(element)

def add_one(cur_value, add_value):
    b = cur_value
    b = add_value

def add_two(cur_value, add_value):
    cur_value += add_value

data = [1, 2, 3]
print(data) # [1, 2, 3]
append_element(data, 4) # [1, 2, 3, 4]
print(data)
a = 8
print(a) # 8
add_one(a, 3)
print(a) # 8
add_two(a, 2)
print(a) # 8

# isinstance函数检查一个对象是否是特定类型的实例
a = 5
print(isinstance(a, int)) # True

# 字符串格式化
template = '{0:.2f} {1:s} are worth US${2:d}'
result = template.format(4.5560, 'Argentina Pesos', 2)
print(result) # 4.56 Argentina Pesos are worth US$2

# Unicode编码
a = '中'
b = a.encode('utf-8')
print(str(a) + ', ' + str(b)) # 中, b'\xe4\xb8\xad'
c = b.decode('utf-8')
print(c) # 中

# 拆包，注意下划线表示不想要的变量
data = [1, 2]
_, b = data
print(str(b)) # 2

# 元组的count方法
a = (1, 2, 2, 0, 2, 3, 3, 4)
print(a.count(2)) # 3