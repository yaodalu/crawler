# -*- coding: utf-8 -*-
#lambda匿名函数
#1.匿名函数可以应用在函数式编程中，如map、reduce、filter、sorted

print 'filter'+'*'*50
a = [1,2,3,4,5,6,7]
#调用一个布尔函数bool_func来迭代遍历每个seq中的元素；
#返回一个使bool_seq返回值为true的元素的序列。
b = filter(lambda x:x>5,a)
print b

print 'map'+'*'*50
#map函数对每一个序列的每个项一次执行函数
c = map(lambda x:x*2,[1,2,3])
print list(c)


print 'reduce'+'*'*50
#reduce函数是对一个序列的每个项迭代调用函数
print reduce(lambda x,y:x*y,range(1,4))

d = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print '按姓名排序',sorted(d,key = (lambda x:x[0]))
print '按分数排序', sorted(d,key = (lambda x:x[1]))

#2.匿名函数可以应用在闭包中
def get_y(a,b):
    return lambda x:a*x+b
y1 = get_y(1,1)
y1(1)
