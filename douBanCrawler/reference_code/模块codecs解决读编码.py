# -*- coding: GBK-*-
import codecs

'''
ģ��codecs�ṩ��һ��open()������
����ָ��һ��������ļ���
ʹ����������򿪵��ļ���ȡ���صĽ���unicode��

д��ʱ�����������unicode����ʹ��open()ʱָ���ı�����б����д�룻
�����str�����ȸ���Դ�����ļ��������ַ����룬��Ҫ�����unicode,���ٽ���ǰ��������
'''

f = codecs.open(r'C:\Users\1\Desktop\python code\Crawler\codecsTest.txt',encoding = 'UTF-8')
u = f.read()
f.close()
print repr(u)
print type(u)

f = codecs.open(r'C:\Users\1\Desktop\python code\Crawler\codecsTest.txt','a',encoding = 'UTF-8')
s = '��'
print repr(s) #GBK
s1 = s.decode('GBK')
print repr(s1) #GBK->unicode
f.write(s1) # unicode -> utf-8 codecsTest.txt��utf-8��ʽ����
f.close()

