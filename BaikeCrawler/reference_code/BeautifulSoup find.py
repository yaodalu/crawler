# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

html = u"""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')

#find_all(name,attrs,recursive,text,**kwargs)

#name参数，包括字符串，正则表达式，列表，True和方法
##字符串
#print soup.findAll('b')
##正则
#print soup.findAll(re.compile('^b$'))
##列表
#print soup.findAll(['a','b'])

#kwargs参数，键值对，键是tag的name,值是tag的属性，属性可以用字符串，正则，列表，True，方法表示
##字符串
#print soup.findAll(id = 'link2')
#print soup.findAll('a',class_='sister')
##正则
#print soup.findAll(href = re.compile('elsie'))

#text参数，可以搜索文档中的字符串内容，包括字符串...方法
print soup.findAll(text = ["Tillie","Elsie",'Lacie'])
print soup.findAll(text = re.compile("Dormouse"))

#limit参数，限制返回结果的数量
print soup.findAll("a",limit = 2)
