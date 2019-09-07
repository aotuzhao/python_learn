#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 18:12
# @Author : zhaoxuezhao
# @Site : 生成
# @File : Generator.py
# @Software: PyCharm

'''

生成器 generator
它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束
yield

生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值
'''
g = (x*x for x in range(1,5))
print(g)
for s in g:
    print(next(g))
'''
迭代器
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数
 
凡是可作用于for循环的对象都是Iterable类型
凡是可以用于next() 函数的对象都是Iterator类型，它们表示一个惰性计算的序列
集合数据类型如 list、dict、str 等都是Iterable 但不是Iterator，不可以通过iter() 函数获得一个Iterator对象
Python的for循环本质是不断移动next() 函数实现
'''
t=[1,2,3]
print(iter(t))
