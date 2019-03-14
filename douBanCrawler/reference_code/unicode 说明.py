# -*- coding: UTF-8 -*-
'''
Unicode（中文：万国码、国际码、统一码、单一码）是计算机科学领域里的一项业界标准。
Unicode涵盖的数据除了视觉上的字形、编码方法、标准的字符编码外，还包含了字符特性，如大小写字母。
Unicode的实现方式称为Unicode转换格式（Unicode Transformation Format，简称为UTF）.
'''

'''
对UTF-8编码的str'汉'使用len()函数时，结果是3，因为实际上，UTF-8编码的'汉' == '\xE6\xB1\x89'。
unicode才是真正意义上的字符串，对字节串str使用正确的字符编码进行解码后获得，并且len(u'汉') == 1。
'''

u=u'汉'
print repr(u)
print isinstance(u,unicode)

s = u.encode('utf-8')
print isinstance(s,str)

u2 = s.decode('utf-8')
print repr(u2)

s2 = u2.encode('utf-8')
print repr(s2)

u3 = [u'汉',u'文'] #unicode组成的列表需要通过循环逐个解码
s3 = []
for i in range(len(u3)):
    s3 += u3[i].encode('utf-8')   
print isinstance(s3[1],str)

s4 = '汉文: 我爱汉文'
u4 = s4.decode('utf-8')
print u4
print isinstance(u4,unicode)

s5 = '\xe5\x87\xba\xe7\x89\x88\xe4\xbf\xa1\xe6\x81\xaf\xef\xbc\x9a \xe5/\x85/\x83' #长度12个字节utf编码？
u5 = s5.decode('gbk')
print u5
'''
内置的open()方法打开文件时，read()读取的是str，读取后需要使用正确的编码格式进行decode()->unicode。
write()写入时，如果参数是unicode，则需要使用你希望写入的编码进行encode()，unicode->其他
如果是其他编码格式的str，则需要先用该str的编码进行decode()，转成unicode后再使用写入的编码进行encode()，源-》unicode->其他
'''
