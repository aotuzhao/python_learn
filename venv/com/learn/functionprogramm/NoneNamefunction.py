#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/8 22:41
# @Author : zhaoxuezhao
# @Site : 匿名函数
# @File : NoneNamefunction.py
# @Software: PyCharm

'''
当我们再传递匿名函数时，不需要显示定义函数，直接传入匿名函数更方便

'''

print(list(map(lambda x:x*x ,range(1,5))))
'''
匿名函数 lambda x:x*x 
关键字Lambda表示匿名函数，冒号前面的x表示函数参数
匿名函数有一个限制，就是只能有一个表达式，不用写return
'''