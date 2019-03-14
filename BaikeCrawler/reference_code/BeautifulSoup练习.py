# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

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
#print isinstance(html,unicode)

soup = BeautifulSoup(html,'lxml')
#print soup.prettify()

#tag
#tag对象
#print soup.a
#tag对象的名
#print soup.a.name
#tag对象的属性
#print soup.a.attrs
#print soup.a['class']
'''
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
a
{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
['sister']
'''
#NavigableString
print soup.p.string
print type(soup.p.string)
print isinstance(unicode(soup.p.string),unicode)



