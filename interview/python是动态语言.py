# -*- coding: utf-8 -*-
动态编程语言是高级程序设计语言的一个类别。
它是一类在运行时可以改变其结构的语言：例如新的函数、对象、代码

1.运行过程中给对象绑定(添加)属性
class　Person(object):
    def __init__(self,name=None.age=None):
        self.name=name
        self.age =age
P = Person('小明','24')
#动态给实例绑定属性
P.sex = 'male' 

2.运行过程中给类绑定(添加)属性
#给类Person添加一个属性
Person.sex = None
P1=Person('小丽','25')
print P1.sex

3.运行的过程中给类绑定(添加)方法

4.运行过程中删除属性和方法
del 对象.属性名
静态语言具有严谨性
