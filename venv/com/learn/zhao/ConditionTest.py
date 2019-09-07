#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 10:31
# @Author : zhaoxuezhao
# @Site : 条件判断
# @File : ConditionTest.py
# @Software: PyCharm


'''
input() 输入为字符串，使用int() 转化为int类型

'''
# age =int(input("请输入你的年龄："))
# print(age)
# if(age>=18 and age<=30):
#      print("青年屌丝")
# elif age>30 and age<50:
#     print("老油腻")
# elif age>100:
#     print("老乌龟")
# else:
#      print("小傻屌")

'''
    循环
    for...in循环 依次把list 或 tuple 每个元素进行迭代
    
'''
names=["赵四","谢广坤","赵鑫","蔡徐坤"]
for name in names:
    print(name)

ages = [1,2,3,4,5,6,7,8]
sum=0
for age in ages:
    sum+=age
print(sum)


# python 提供了一个生成整数序列的函数 range(),在通过list() 函数转换为list
print(range(3))
print(list(range(0,3)))

'''
    while 循环，只要条件满足，就可以不断循环，条件不满足时退出
    
'''
sum=0
n=100
while n>0:
    if(n%2==0):
        sum+=n
    n-=1
print(sum)

'''
    break 退出循环 
    continue 退出本次循环
    break语句可以在循环过程中直接退出循环，
    而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用
'''

