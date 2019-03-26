# -*- coding: utf-8 -*-
L = [x*x for x in range(10)] #列表
g = (x*x for x in range(5)) #生成器
print next(g)
print next(g)
print next(g)
print next(g)
print next(g)
#print next(g)

#可迭代对象：可以直接作用于for循环的对象(iterable)
#包括集合数据类型，如list tuple dict string set
#是generator, 包括生成器和带yield的生成器函数
    

#生成器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
########直到抛出StopIteration错误
########iterator
########可以利用iter()将list,tuple,dict,set,string强制转换

生成器特点：
采取一边循环一边计算的机制，节约内存
生成器不仅记住了数据状态，还记住了它在流控制构造中的位置

生成器特点：
凡是可作用于 for 循环的对象都是 Iterable 类型；可迭代对象
凡是可作用于 next() 函数的对象都是 Iterator 类型；迭代器
集合数据类型如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。

#生成器实现换行输入
endstr = "end"
str1 = ""
for line in iter(input,endstr):
    str1 += line + '\n'

print str1
