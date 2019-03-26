# -*- coding: utf-8 -*-
一.函数引用
def test1():
    print("-----in test1 func----")

#调用函数
test1()

#引用函数
ret = test1

#函数也是对象
print(id(ret))
print (id(test1))

#通过引用调用函数
ret()

二.闭包
def test(number):

    #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量
    #那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print ("in test_in 函数，num_in is %d" %number_in)
        return number+number_in
    return test_in

#给test函数赋值，number=20
#这里的ret引用函数test_in
ret = test(20)

#100给test_in函数赋值，即number_in=100
print(ret(100))

三.闭包再理解
内部函数对外部函数作用域里变量的引用(非全局变量)，则称内部函数为闭包

四.闭包实例
1.闭包提高了代码的可复用性，不需要每次都创建变量a,b，优化了变量，类似于泛函？
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1 = line_conf(1,1)
print lin1(5)
line2 = line_conf(4,5)
print line2(5)

五.闭包与匿名函数
def get_y(a,b):
    return lambda x:a*x+b
y1 = get_y(1,1)
y1(1)

    




