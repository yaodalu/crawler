# -*- coding: utf-8 -*-
import copy
a = [1,2,3,4,['a','b']]

#赋值，传对象的引用,list可变对象
b = a

#对象拷贝，浅拷贝，没有拷贝子对象，子对象共享，
#所以子对象可变则变如list，子对象不可变则不变如num
c = copy.copy(a) 

#对象拷贝，深拷贝，拷贝子对象，互相不影响
d = copy.deepcopy(a) 

#a.append(5) #不可变
                        
#a[4].append('c')  #可变

print 'a=',a #[1,2,3,4,['a','b','c'],5]
print 'b=',b #[1,2,3,4,['a','b','c'],5]

print (c is a) #is 比较地址，==比较值

print 'c=',c #[1,2,3,4,['a','b','c']]
print 'd=',d #[1,2,3,4,['a','b']]
