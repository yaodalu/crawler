# -*- coding: utf-8-*-
#静态方法@staticmethod
#类方法@classmethod


def foo(x):
    print "executing foo(%s)" %(x)

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)" %(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)" %(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" %(x)
#函数
foo(u'测试1')

#实例方法
a = A()
a.foo(u'测试2') #等同于foo(a,x)

#类方法，需要看成整体的
A.class_foo(u"测试3")

#静态方法,不需要实例化的
A.static_foo(u"测试3")
        
