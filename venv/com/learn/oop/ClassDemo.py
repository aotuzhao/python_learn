#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/9 21:24
# @Author : zhaoxuezhao
# @Site : 类和实例
# @File : ClassDemo.py
# @Software: PyCharm

'''
在Python中，定义类是通过class 关键字，
class 类名(父类)
所有类的父类是object类

创建实例  类名（）

'''
class Student(object):
    pass

print(Student)

s1 = Student()
s1.name='张三'
print(s1.name)

'''
强制初始化一些参数，使用__init__ 方法
'''
class Student2(object):
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def print_args(self):
        print(' student %s : %s'%(self.name,self.age))
'''
__init__() 第一个参数self ，表示创建实例的本身，因此在__init__ 方法内部，就可以把各种属性绑定到self中，
以为self本身指向创建的实例本身
'''

# print(Student2()) TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
student_ = Student2('张三', 24)
print(student_.name,student_.age)

'''
数据封装
每个实例都有自己的数据，可以通过函数访问数据
'''
student_.print_args()

'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，
也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
'''
s = Student2('李四', 22)
s.className='二班'
s.print_args()
print(s.className)


