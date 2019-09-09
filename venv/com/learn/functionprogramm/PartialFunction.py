#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 9:56
# @Author : zhaoxuezhao
# @Site : 偏函数
# @File : PartialFunction.py
# @Software: PyCharm

import functools

'''

Python 的 functools模块提供了很多的功能，偏函数也是其中一个功能。
偏函数可以设置参数的默认值

'''
print(int('123'))
print(int('123',base=8))

def int2(x):
    return int(x,base=2)
print(int2('11'))
'''
通过偏函数，可以实现int2() 
functools.partial() 的作用就是，把一个函数的某些参数给固定，设置默认值，返回一个新函数

当函数的参数过多，需要简化时，使用functools.partial() 可以创建一个新的简化函数，这个新函数可以固定住原函数的部分参数，从而简化函数的调用 
'''
int2 = functools.partial(int,base=2)
print(int2('11'))

