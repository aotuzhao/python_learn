#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 10:32
# @Author : zhaoxuezhao
# @Site : 模块的使用
# @File : ModuleTestOne.py
# @Software: PyCharm

# 模块的文档注释，任何模块代码的第一个字符串都被认为模块的文档注释
__doc__ =' a test module'

# 作者变量
__author__ ='zhaoxuezhao'


import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()



'''
作用域
在python中，是通过 _ 前缀来实现变量的作用域限定的
正常的函数和变量名是公开的，直接被引用的，
类似 __xxx__ 这样的变量是特殊变量，可以直接被引用，但是有特殊用途，比如 __doc__ 等

_xxx或__xx 这样的函数或变量是非公开的，不应该直接被引用，这里说不应该指的是可以，并不是不能，因为Python并没有一种
方法完全
'''