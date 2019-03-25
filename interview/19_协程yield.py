# -*- coding: utf-8 -*-
#generator for the Fibonacci sequence
#生成器每次运行到yield语句停止，并返回yield后面的数值
#调用方法 f=genFib(),f.next()
def genFib():
    fibn_1 = 1
    fibn_2 = 1
    while True:
        temp = fibn_1 + fibn_2
        yield temp
        fibn_2 = fibn_1
        fibn_1 = temp

