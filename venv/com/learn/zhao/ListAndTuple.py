#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 8:45
# @Author : zhaoxuezhao
# @Site : python 中的集合
# @File : ListAndTuple.py
# @Software: PyCharm
'''
Python内置的一种数据类型是列表：list list是有序集合，可以随时添加删除其中的元素
len(list) 获取list 的元素个数
list[index] index 超出范围报错 IndexError
'''
names = ["张小涛","朱小光","李小顺"]
print(names)
print(len(names))
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])
print(names[-3])
reverse = names.reverse()
print(reverse)
'''
    向list中追加元素 
    list.append(value) 追加在最后
    list.insert(index,value) 插入到指定位置
'''
ages = [1,2,3]
ages.append(4)
ages.insert(0,0)
print(ages)
'''
list.pop() 删除尾部元素
pop(i) 删除指定位置元素

'''

# 删除list尾部的元素 使用pop() 方法
ages.pop()
ages.pop(0)
print(ages)

# 替换值的时候，直接赋值就可以
# list中各个元素的数据类型可以不同
obj=[1,"账单",22,[1,2]]
print(obj)
print(obj[3])
print(obj[3][1])
print(len(obj))
print(len(obj[3]))


'''
    python3 中另外一种列表叫元组 tuple 。
    tuple和list相似，但是tuple一旦初始化后就不可修改。
    tuple不可修改，更加安全
'''
fanleId = ('BJ00001','BJ00002','BJ00003')
print(fanleId)
print(fanleId[2])

'''
    t=t(1) 定义不是只用1个元素的元组，而是数字1这个数， （）既可以表示元祖，也可表示数字小括号
    所以在定义一个元素的元祖时，末尾要加个 ，
'''
t= (1)
print(t)
t=(1,)
print(t)
