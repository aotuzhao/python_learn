#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 9:05
# @Author : zhaoxuezhao
# @Site : 装饰器
# @File : DecoratorDemo.py
# @Software: PyCharm

import functools


def myLog(func):
    @functools.wraps(func)
    def wapper(*args,**kw):
        print('args %s()' % func.__name__)
        return func(*args,**kw)
    return wapper

@myLog
def add_num(x,y):
    return x+y


print(add_num.__name__)
print(add_num(1,2)

'''
在面向对象（OOP）模式中，decorator被称为装饰模式，
'''