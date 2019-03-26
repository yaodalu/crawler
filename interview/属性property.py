# -*- coding: utf-8 -*-
不懂！！！
一.私有属性添加get和set方法 __XX
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")


二.使用property升级get和set方法
get_set.py
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
money = property(getMoney,setMoney)

#运行
from get_set import Money
a = Money()
a.money #0
a.money = 100 # 100
a.getMoney()  #100
