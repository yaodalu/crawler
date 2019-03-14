# -*- coding: gbk -*-
#法1：源代码是gbk打头，代码中的str'作者'，需要用decode('gbk')->unicode
#法2：str'作者'，写作u'作者'
import sys
import time
import urllib
import urllib2
import requests
import numpy as np
from bs4 import BeautifulSoup
from openpyxl import Workbook
import ssl
import re

book_list=[]
book_tag_lists = [u'算法']
    
with open (r'C:\Users\1\Desktop\python code\Crawler\file\book.txt','r') as f:
    bookStr = f.read().decode('UTF-8')#str->unicode 为什么此处是UTF-8解码 GBK报错 Multitype byte

soup = BeautifulSoup(bookStr,'lxml')
list_soup = soup.find('div', {'class': 'mod book-list'})

for book_info in list_soup.findAll('dd'): 
    title = book_info.find('a', {'class':'title'}).string.strip()#unicode
    desc = book_info.find('div', {'class':'desc'}).string.strip()#unicode
    desc_list = desc.split('/')#unicode
    book_url = book_info.find('a', {'class':'title'}).get('href')#str

    try:
        author_info = u'作者/译者：' + u'/'.join(desc_list[0:-3])
    except:
        author_info =u'作者/译者： 暂无'
   # finally:
   #    print (author_info)
   #    print isinstance(author_info,unicode)
    
    try:
        pub_info = u'出版信息： ' + u'/'.join(desc_list[-3:])
    except:
        pub_info = u'出版信息： 暂无'
        
    try:
        rating = book_info.find('span', {'class':'rating_nums'}).string.strip()
    except:
        rating=u'0.0'
     
    #try:
     #   people_num = get_people_num(book_url) 
      #  people_num = people_num.strip(u'人评价')
    #except:
    people_num =u'0'

    book_list.append([title,rating,people_num,author_info,pub_info])
print book_list[0][3]


