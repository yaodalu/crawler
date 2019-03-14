# -*- coding: utf-8 -*-
#python3
import urllib.request
import ssl
import re

info = ''
def ajaxCrawler(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"}
    req=urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response=urllib.request.urlopen(req,context=context,timeout=1.5)
    jsonStr = response.read().decode('utf-8')
    return jsonStr
   
for i in range(5):
    url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start='+str(i*20)+'&limit=20'
    info += ajaxCrawler(url)

#windows 新文件的编码默认gbk
#with open(r'C:\Users\1\Desktop\python code\Crawler\file\file.txt','w',encoding='utf-8') as f:
#       f.write(info)

re_title = re.compile('"title":"(.*?)",')
print(re_title.findall(info))
print(len(re_title.findall(info)))
'''
"title": "肖申克的救赎",
'''
