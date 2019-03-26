# -*- coding: utf-8 -*-
import types

#定义一个类
class Person(object):
    num=0
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def eat(self):
        print("eat food")


#定义一个实例方法
def run(self,speed):
    print "%s在移动，速度是%d km/h" %(self.name,speed)

#定义一个类方法
@classmethod
def testClass(cls):
    cls.num = 100

#定义一个静态方法
@staticmethod
def testStatic():
    print "------static method--------"

#创建一个实例对象
P = Person("老王"，24)
P.eat()

#给这个对象添加实例方法
P.run = types.MethodType(run,P)
P.run(180)

#给类绑定classmethod,调用类方法
Person.testClass = testClass
print Person.num
Person.testClass()

#给类绑定静态方法
Person.testStatic = testStatic
