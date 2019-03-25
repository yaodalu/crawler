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
    

#迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
########直到抛出StopIteration错误
########iterator
########可以利用iter()将list,tuple,dict,set,string强制转换

#迭代器实现换行输入
endstr = "end"
str1 = ""
for line in iter(input,endstr):
    str1 += line + '\n'

print str1
