#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/8 9:05
# @Author : zhaoxuezhao
# @Site : 返回函数
# @File : ReturnFunction.py
# @Software: PyCharm

'''
函数作为返回值
高阶函数除了可以接受函数作为参数，还可以将函数作为结果返回

'''
def lazy_sum(x):
    def my_sum():
        sumNum = 0
        for i in x:
            sumNum = sumNum + i
        return sumNum
    return my_sum

f = lazy_sum(range(1,4))
print(f)
print(f())

def my_sum(x):
    sumNum=0
    for i in x:
       sumNum=sumNum+i
    return sumNum
print(my_sum(range(1,5)))

'''
返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs



def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

