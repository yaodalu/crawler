# -*- coding: utf-8 -*-
一.代码"开放封闭"原则
封闭：已实现的功能代码块；开放：对扩展开发
def w1(func):
    def inner():
        验证
        func()
    return inner

@w1
def f1():
    print('f1')

执行w1函数，并将@w1下面的函数作为w1函数的参数
即@w1等价于w1(f1)
inner = w1(f1)
将执行完的w1函数返回值 赋值给f1
new f1 = inner

二.装饰器(decorator)功能
1.引入日志
2.函数执行时间统计
3.执行函数前预备处理
4.执行函数后清理功能
5.权限校验
6.缓存？

三.装饰器实例1
执行过程可以理解为
#foo先作为参数赋值给func后，foo接收指向timefun返回的wrappedfunc,即foo = timefun(foo)
#调用foo(),等价于调用wrappedfun()
#内部函数wrappedfun被引用，所以外部函数的func变量没有被释放，类似于闭包
from time import ctime,sleep

def timefun(func):
    def wrappedfunc():
        print ("%s called at %s" %(func.__name__,cttime()))
        func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

foo()

四.装饰器中的return
from time import ctime,sleep

def timefun(func):
    def wrappedfunc():
        print ("%s called at %s" %(func.__name__,cttime()))
        func()
    return wrappedfunc

@timefun
def getInfo():
    return '------haha------'
print (getInfo())
#结果
##getInfo called at Fri Nov  4 21:55:37 2016
##None ??
#如果return wrappedfunc修改为return func()
##getInfo called at Fri Nov  4 21:55:59 2016
##----hahah--

