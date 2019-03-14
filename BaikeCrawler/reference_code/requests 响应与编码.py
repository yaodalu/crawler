# -*- coding: utf-8 -*-
import requests
import chardet

r = requests.get('http://www.baidu.com')
#爬取内容的字节形式(str)
#print 'content-->'+r.content 
#print isinstance(r.content,str)

#爬取内容的文本形式(unicode),中文乱码
#print 'text-->'+r.text
#print isinstance(r.text,unicode)

#url的编码格式是utf,Requsts猜测是ISO，手动修改r.encoding，显示正确
print 'encoding-->'+r.encoding
print r.encoding == 'ISO-8859-1'
r.encoding = 'utf-8'
print 'new text-->'+r.text
print isinstance(r.text,unicode)

#chardet模块自动检测url编码
#{'confidence': 0.99, 'language': '', 'encoding': 'utf-8'}
print chardet.detect(r.content)
r.encoding = chardet.detect(r.content)['encoding']
print r.text

