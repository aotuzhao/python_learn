#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/8 8:19
# @Author : zhaoxuezhao
# @Site : 排序算法
# @File : Sorted.py
# @Software: PyCharm

'''

排序算法
Python内置的sorted() 函数可以对list进行排序
sorted(Iterable) 默认排序
sorted(Iterable，key) 传入key函数实现自定义的排序
sorted(Iterable,key=function,reverse=Boolean)
reverse 反向排序
'''
list1=[3,42,4,5,42,6]
print(sorted(list1))
print(sorted(list1,reverse=True))
list2=[-2,-45,-3,39,434,23,4,5,3]
print(sorted(list2,key=abs))
print(sorted(list2,key=abs,reverse=True))

'''
sorted() 函数排序的关键是实现一个映射函数，实现自定义的排序规则
'''
