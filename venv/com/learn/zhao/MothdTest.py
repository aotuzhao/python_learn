#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 13:09
# @Author : zhaoxuezhao
# @Site : python 常见内置函数
# @File : MothdTest.py
# @Software: PyCharm



print("-------数学相关-------")
print(abs(-19))
print(max([1,2,3]))
print(len([1,2,3,4,5]))
print(divmod(5,3)) # （商，余数）
print(pow(2,3)) # 乘方
print(round(1.2))

print("-------功能相关-------")
'''
1、函数是否可调用：callable(funcname)，注意，funcname变量要定义过
2、类型判断：isinstance(x,list/int)
3、比较：cmp('hello','hello')
4、快速生成序列：(x)range([start,] stop[, step])
'''
'''
三、类型转换

1、int(x)
2、long(x)
3、float(x)
4、complex(x) //复数
5、str(x)
6、list(x)
7、tuple(x) //元组
8、hex(x)
9、oct(x)
10、chr(x)//返回x对应的字符，如chr(65)返回‘A'
11、ord(x)//返回字符对应的ASC码数字编号，如ord('A')返回65

四、字符串处理
1、首字母大写：str.capitalize
2、字符串替换：str.replace() 可以传三个参数，第三个参数为替换次数
3、字符串切割：str.split 可以传二个参数，第二个参数为切割次数
'''
print('hello'.capitalize())
print('hello'.replace('l','E'))
print('hello'.replace('l','E',1))
print('hello'.split('l'))
print('hello'.split('l',1))

'''
五、序列处理函数
1、len：序列长度
2、max：序列中最大值
3、min：最小值
4、filter：过滤序列
'''
i = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 6])
for x in i:
    print(x)

'''
5、zip：并行遍历
'''
names = ['A','B','C']
classs=['一','二','三']
souc=[100,102,99]
iterator = zip(names)
for y in iterator:
    print(y)
iterator=zip(names,classs)
for y in iterator:
    print(y)
iterator=zip(names,classs,souc)
for y in iterator:
    print(y)
'''
6、map：并行遍历，可接受一个function类型的参数
7、reduce：归并
'''
print(map(None,names, classs))

'''
自定义函数
函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑

'''


