# -*- coding: utf-8 -*-
#类变量和实例变量

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
