#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/8 7:59
# @Author : zhaoxuezhao
# @Site : filter() 函数用于过滤序列
# @File : Filter.py
# @Software: PyCharm


'''
和map() 类似，filter() 也接收一个函数和一个序列。和map()不同的是，
filter() 把传入的函数依次作用于每个元素，然后根据是True还是False决定保留还是丢弃该元素。

'''

# 删除list中的偶数
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,range(1,6))))

'''
filter() ，关键在于正确实现一个筛选函数，filter返回的一个Iterator,也是一个
惰性序列，所以强迫filter() 完成计算结果，需要用list() 函数将结果返回list
由于filter() 使用了惰性计算，所以只有在取filter() 结果的时候，才会真正筛选
并每次返回下一个筛选出的元素
'''