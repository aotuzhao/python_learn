#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/7 21:01
# @Author : zhaoxuezhao
# @Site : 高阶函数
# @File : Higher_Function.py
# @Software: PyCharm
'''
变量可以指向函数

'''
print(abs)
x=abs
print(x)
print(x(-9))

'''
函数名也是变量，
abs() 可以将abs = 10  但是abs() 函数不可用
'''

'''
传入函数
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数成为高阶函数
编写高阶函数，就是让函数的参数能够接收别的函数
把函数作为参数传入，这样的函数成为高阶函数，函数式编程就是这种高度抽象的编程范式
'''

def my_add(x,y ,z):
    return z(x)+z(y)

print(my_add(-1,2,abs))