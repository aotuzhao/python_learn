#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/8 0:00
# @Author : zhaoxuezhao
# @Site : 内部的map和reduce
# @File : MapReduce.py
# @Software: PyCharm
from functools import reduce
'''
Python 内建了map() 和 reduce() 函数
map() 函数接收两个参数，一个函数，一个Iterable ，map将传入的函数依次作用在Iterable每个元素上，并将结果作为新的
Iterator返回
'''
def method1(x,y=0):
    return pow(x,2)

print(method1(2))
r = range(1, 5)

i = map(method1, r)
print(i)
print(list(i))
'''
Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
print(list(map(str,[1,2,3])))
'''
reduce() 把一个函数作用在一个序列上，这个函数也接收两个参数，reduce把结果继续和序列的元素做累计计算
'''
def method2(x,y):
    return x+y
print(reduce(method2,[1,2,3]))