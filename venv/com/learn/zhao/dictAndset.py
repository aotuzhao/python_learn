#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/6 11:17
# @Author : zhaoxuezhao
# @Site : dict 和set 类似map
# @File : dictAndset.py
# @Software: PyCharm

'''
dict 类似map 提供key-value 的存储，具有很快的查找速度
key 不存在，会报错 keyerror  可以使用in 判断key是否存在 或者使用get()
'''
city={'北京':18,'上海':14,'深圳':12}
print(city['北京'])
city['北京']=22
print(city['北京'])
print('上海' in city)
print('上海ren' in city)
print(city.get('上海'))
print(city.get('上海任',"不存在的"))
'''
    使用pop(key) 删除dict中的元素
    dict内部存放的顺序和key放入的顺序是没有关系的
和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要
需要牢记的第一条就是dict的key必须是不可变对象。
在Python中，字符串、整数等都是不可变的
'''

'''
    set
    和 dict类似，也是一组key的集合，但是不可存储value，类似java.util.Set
    创建set时，需要提供一个list作为输入集合
    重复元素在set中自动过滤去除
    可以通过add(key)方式添加元素到set中
    使用pop()移除收个元素，使用remove(key)移除元素 
'''
setA = set(list(range(6)))
print(setA)
setA.add(6)
setA.add(6)
print(setA)
setA.add(7)
print(setA)
setA.pop()
print(setA)
setA.remove(4)
print(setA)
setA.pop()
print(setA)
'''
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
& 取交集  | 取并集（去重）
'''
set1 = set([1,2,3,5,7])
set2=set([3,4,5,6])
print(set1 & set2)
print(set2 | set1)

print('---------------')
a='nihao'
b=a.replace('h',"H")
print(b)
print(a)

