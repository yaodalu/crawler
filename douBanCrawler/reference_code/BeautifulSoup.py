# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())#缩进表示
print(soup.title)#title标签
print(soup.title.name)#title标签名
print(soup.title.string)#title标签内容
print(soup.title.parent.name)#标签title的父标签
print(soup.p)
print(soup.p["class"])#第一个标签p的class属性
print(soup.a)
print(soup.find_all('a'))#所有标签a
print(soup.find(id='link3'))
