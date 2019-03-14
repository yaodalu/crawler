# -*- coding: GBK-*-
import codecs

'''
模块codecs提供了一个open()方法，
可以指定一个编码打开文件，
使用这个方法打开的文件读取返回的将是unicode。

写入时，如果参数是unicode，则使用open()时指定的编码进行编码后写入；
如果是str，则先根据源代码文件声明的字符编码，需要解码成unicode,后再进行前述操作。
'''

f = codecs.open(r'C:\Users\1\Desktop\python code\Crawler\codecsTest.txt',encoding = 'UTF-8')
u = f.read()
f.close()
print repr(u)
print type(u)

f = codecs.open(r'C:\Users\1\Desktop\python code\Crawler\codecsTest.txt','a',encoding = 'UTF-8')
s = '汉'
print repr(s) #GBK
s1 = s.decode('GBK')
print repr(s1) #GBK->unicode
f.write(s1) # unicode -> utf-8 codecsTest.txt以utf-8格式保存
f.close()

