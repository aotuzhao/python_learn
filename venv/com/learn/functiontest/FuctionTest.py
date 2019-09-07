#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 14:53
# @Author : zhaoxuezhao
# @Site : 函数验证类
# @File : FuctionTest.py
# @Software: PyCharm
from MyFunctionOne import num_add
from MyFunctionOne import move
from MyFunctionOne import oneOrTwo
from MyFunctionOne import str_append
from MyFunctionOne import personal



print(num_add(1,2,'+'))
print(move(1,2))
print(oneOrTwo(2,3,1))
print(oneOrTwo(1, 3, -4))
print(str_append())
print(str_append())
extra = {'city': 'Beijing', 'job': 'Engineer'}

personal('赵',12,city='北京',saly=1000000);
personal('赵',12,**extra);
