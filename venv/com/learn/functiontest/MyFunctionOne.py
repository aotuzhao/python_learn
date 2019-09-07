#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 14:51
# @Author : zhaoxuezhao
# @Site : 测试函数1
# @File : MyFunctionOne.py
# @Software: PyCharm

import  math

def num_add(x,y,z):
    if not isinstance(x,(int,float)):
        raise TypeError(x+' 不是数字类型')
    if not isinstance(y,(int,float)):
        raise TypeError(y+' 不是数字类型')
    if(z=='+'):
        return x + y
    elif (z=='-'):
        return  abs(x-y)


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
def my_none():
    pass

def move(x,y):
    sum = x+y;
    b = abs(x-y);
    return sum,b,math.pi


'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
'''
def oneOrTwo(a,b,c):
    x1=0
    x2=0
    if not isinstance(a,(int,float)):
        raise TypeError('bad num');
    if not isinstance(b,(int,float)):
        raise TypeError('bad num');
    if not isinstance(c,(int,float)):
        raise TypeError('bad num');
    if a==0:
        raise TypeError('a 不能为0')
    else:
        num1=2*a;
        temp =math.sqrt(pow(b,2)-4*a*c);
        num2=(-b)-temp
        num3=(-b)+temp
        x1=num2/num1
        x2=num3/num1
    return x1,x2

'''
函数可以设置默认参数
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''
def str_append(L=None):
    if L is None:
        L=[]
    L.append('str')
    return L


'''
可变参数
可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
在参数前面加了一个*号
在函数内部，参数numbers接收到的是一个tuple
在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
'''
def calc(*numbers):
    print(numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def personal(name,age,**moneys):
    print(name,age,moneys)
    print("\n")
    print(moneys['city'])
    print(moneys.get('saly'))

'''
命名关键字参数
限制关键字参数的名字，就可以用命名关键字参数
只接收city和job作为关键字参数
命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
'''
def person(name, age, *, city, job):
        print(name,age,city,job)


'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
'''

'''

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
'''