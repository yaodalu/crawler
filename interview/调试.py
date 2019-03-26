# -*- coding: utf-8-*-

##一.demo1
##import pdb
##a = 'aaa'
##pdb.set_trace()
##b = 'bbb'
##c = 'ccc'
##pdb.set_trace()
###当有多个pdb.set_trace()时，键入c会追踪到下一个pdb.set_trace()
##final = a+b+c
##print final

##二.进入函数
###设置断点b lineno, s 进入函数, r 执行代码到函数退出
##import pdb
##def combine(s1,s2):
##    s3 = s1 + s2 + s1
##    s3 = "*"+ s3 +"*"
##    return s3
##a = "aaa"
##pdb.set_trace()
##b = "bbb"
##c = "ccc"
##final = combine(a,b)
##print final

##三.pdb实例
import pdb

def add3Nums(a1,a2,a3):
    result = a1 + a2 + a3
    return result

def get3NumsAvarage(s1,s2):
    s3 = s1 + s2 + s1
    result = 0
    result = add3Nums(s1,s2,s3)
    return result
if __name__ == "__main__":
    a = 11
    pdb.set_trace()
    b = 12
    final = get3NumsAvarage(a,b)
    print final
