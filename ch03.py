#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch03.py
@Time    :   2019/11/22 15:20:50
@Author  :   shaopf 
@Version :   1.0
@Contact :   feipengshao@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   Chapter 03
'''

# zip函数的一个机智的拆分方式
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens')]
first_names, last_names = zip(*pitchers)
print(first_names) # ('Nolan', 'Roger')
print(last_names) # ('Ryan', 'Clemens')

# 列表推导式
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
new_strings = [x.upper() for x in strings if len(x) > 2]
print(new_strings) # ['BAT', 'CAR', 'DOVE', 'PYTHON']

# 字典，集合也可以使用列表推导式
unique_length = {len(x) for x in strings} # 集合
print(unique_length) # {1, 2, 3, 4, 6}
# 上面的列表推导式也可以用map函数
unique_length_map = set(map(len, strings))
print(unique_length_map) # {1, 2, 3, 4, 6}

loc_mapping = {val : index for index, val in enumerate(strings)}
print(loc_mapping) # {'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}

# 函数，位置参数，关键字参数
def my_fuction(x, y, z=0.1):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)
print(my_fuction(5, 6, z=10.7)) # 117.69999999999999
print(my_fuction(3.14, 7, 0.5)) # 0.049309664694280074
print(my_fuction(10, 20)) # 0.0033333333333333335，此时z=0.1
def my_fuction_2(x, y, z=0.1):
    if z > 1:
        return z * x
    else:
        return z * y
print(my_fuction_2(x=5, y=6, z=7)) # 35
print(my_fuction_2(y=5, x=6, z=7)) # 42

# 函数是对象
# 第一种方式：常规操作
import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip() # 去除首尾空格
        value = re.sub('[!#?]', '', value) # 替换掉!#?符号
        value = value.title() # 统一单词的大小写
        result.append(value)
    return result
states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south   carolina##', 'West virginia?']
print(clean_strings(states)) # ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South   Carolina', 'West Virginia']
# 第二种方式
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops = [str.strip, remove_punctuation, str.title] # 函数作为操作列表，更有通用性，复用性
def cle_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
print(cle_strings(states, clean_ops)) # ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South   Carolina', 'West Virginia']
# 第三种方式，可以用内建的map函数，每次可以完成一种操作
for x in map(remove_punctuation, states):
    print(x)