#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/4 18:51
# @Author : zhaoxuezhao
# @Site : 数据类型 整数、浮点数、字符串、布尔值、空值、常量、变量、set\dict\list\tuple
# @File : DataType.py
# @Software: PyCharm

# 整数
#     十六进制
# 浮点数
# 字符串
#  ' 或者 " 包起来的字符
print('I\'m fine \"')
print('hello \t world')
# 用r''表示''内部的字符串默认不转义
print ('hello \t world \n',r' \t nihao \n nihao ')
# Python允许用'''...'''的格式表示多行内容
print('''
h
i
jkajsdf
asdf
''')

# boolean
print(3>2)
print(3<1)

# and or not 运算符
print('-----------------------')
print(3>2 and 3>1)
print(3>2 and 3<1)
print(3>2 or (3-1)<0)
print(3>2 or not (3-1)<0)

# 空值
print(None)

asdf = 10
print(asdf)
asdf = 'asdfaasdf'
print(asdf)

# 除法 / 计算结果是小数 //底板除 整数
print(10/3)
print(10/2)
print(10//3)
# 取模
print(10%2)
print(10%3)

# Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的
# 在Python3中，字符串编码是Unicode编码
# ord() 函数获取字符串的整数表示 单个字符  chr() 函数把编码转化为对应的字符
lk = "国";
print(ord(lk))
stringCode = ord(lk)
print(chr(stringCode))
# python 中的字符串是使用str保存的，在内存中是Unicode表示的，一个字符对应若干个字节，如果在网络中传输，或者保存到磁盘中，需要将
# str转换为 bytes
# python 对bytes类型的数据用带b前缀的单引号或双引号表示
x = 'ABC'
y=b'edf'
print(x)
print(x.encode('ascii'))
# encode() 编码
# decode() 解码
decode = b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
print(decode)

# 计算字符的长度
i = len('likekeshigedamienv')
print(i)
print(len("我和我的祖国，一刻也不能分隔"))
# len() 函数计算的是 str 的字符数，如果换成 bytes，len() 函数计算的是字节数
len(b'abc')

# 字符串格式化
# Python 中，采用的格式化方式和C语言一致，用 % 实现
print('hello ,%s ,you have $%d'%('world',100000000000))
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
# %% 转义的%
# 使用format() 格式化字符串，替换使用{0}、{1}。。。
print("hello,{0},恭喜你，获得{1}第{2}".format('zhao',"大乐透","一"))

