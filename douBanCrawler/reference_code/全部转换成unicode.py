# -*- coding: gbk -*-
#��1��Դ������gbk��ͷ�������е�str'����'����Ҫ��decode('gbk')->unicode
#��2��str'����'��д��u'����'
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
book_tag_lists = [u'�㷨']
    
with open (r'C:\Users\1\Desktop\python code\Crawler\file\book.txt','r') as f:
    bookStr = f.read().decode('UTF-8')#str->unicode Ϊʲô�˴���UTF-8���� GBK���� Multitype byte

soup = BeautifulSoup(bookStr,'lxml')
list_soup = soup.find('div', {'class': 'mod book-list'})

for book_info in list_soup.findAll('dd'): 
    title = book_info.find('a', {'class':'title'}).string.strip()#unicode
    desc = book_info.find('div', {'class':'desc'}).string.strip()#unicode
    desc_list = desc.split('/')#unicode
    book_url = book_info.find('a', {'class':'title'}).get('href')#str

    try:
        author_info = u'����/���ߣ�' + u'/'.join(desc_list[0:-3])
    except:
        author_info =u'����/���ߣ� ����'
   # finally:
   #    print (author_info)
   #    print isinstance(author_info,unicode)
    
    try:
        pub_info = u'������Ϣ�� ' + u'/'.join(desc_list[-3:])
    except:
        pub_info = u'������Ϣ�� ����'
        
    try:
        rating = book_info.find('span', {'class':'rating_nums'}).string.strip()
    except:
        rating=u'0.0'
     
    #try:
     #   people_num = get_people_num(book_url) 
      #  people_num = people_num.strip(u'������')
    #except:
    people_num =u'0'

    book_list.append([title,rating,people_num,author_info,pub_info])
print book_list[0][3]


