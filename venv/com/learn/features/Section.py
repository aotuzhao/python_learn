#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 16:38
# @Author : zhaoxuezhao
# @Site :  切片
# @File : Section.py
# @Software: PyCharm

names = ['zahng','tom','cat','dog']
for name in names:
    print(name)

# 获得指定范围内元素
print(names[0:2])
print(names[:2])
print(names[1:3])
print(names[1:-1])
print(names[1:-2])
print(names[-3:])
'''
list[start:end:step]
list[:] 复制一个list
'''

'''
迭代
'''
students={'name':'Tom','sage':24,'className':'一班'}
for keyName in students:
    print(keyName)

for val in students.values():
    print(val)

for k,v in students.items():
    print(k,'-->',v)


'''
判断一个对象是可迭代对象
isinstance(obj,Iterable)
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
'''
for i,value in enumerate(names):
    print(i,"--->",value)

'''
列表生成表达式

'''
temp = [x*x for x in range(1,10)]
for t in temp:
    print(t)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ x.lower() for x in L1 if(isinstance(x,str)) ]
print(L2)
