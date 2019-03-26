# -*- coding: utf-8 -*-
#类变量和实例变量

xx: 公有变量
_x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
__xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
__xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
xx_:单后置下划线,用于避免与Python关键词的冲突

print "test1"+"*"*50
class Test(object):
    #类变量
    instanceNum = 0 
    def __init__(self,name):
        #实例变量
        self.name = name
        Test.instanceNum += 1
if __name__ == "__main__":
    print Test.instanceNum
    t1 = Test('jack')
    print Test.instanceNum
    t2 = Test('lucy')
    print Test.instanceNum

print "test2"+"*"*50
class Person():
    name = "aaa"

p1 = Person()
p2 = Person()
p1.name = 'bbb'
print p1.name #函数传参string不可变类型
print p2.name
print Person.name

print "test3"+"*"*50
class Person():
    name = []

p1 = Person()
p2 = Person()
p1.name.append('bbb')
print p1.name #函数传参list可变类型
print p2.name
print Person.name
