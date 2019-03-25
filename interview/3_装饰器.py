# -*- coding: utf-8-*-
#装饰器

#正常写法
print u"正常写法"+"#"*50
def func1():
    print (u"测试")

def outer():
    print("*"*50)
    func1()

outer()

#装饰器写法1
print u"装饰器写法1"+"#"*50
def outer(fun):
    def inner():
        print("*"*50)
        fun()
    return inner
func2 = outer(func1)
func2()

#装饰器写法2
print u"装饰器写法2"+"#"*50
def outer(fun):
    def inner():
        print("*"*50)
        fun()
    return inner

@outer
def func3():
    print (u"测试")
func3()



