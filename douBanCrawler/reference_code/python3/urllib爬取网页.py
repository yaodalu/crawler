# -*- coding: utf-8 -*-
#python3
import urllib.request
import ssl

context = ssl._create_unverified_context()
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
#newUrl = urllib.request.unquote(url) wd解密
response = urllib.request.urlopen(url,context=context) 

data = response.read()


with open(r"C:\Users\1\Desktop\code\Crawler\file\file.html",'wb') as f:
    f.write(data)

######retrieve直接将爬取内容存到文档#########
#urllib.request.urlretrieve(url,filename=r'C:\Users\1\Desktop\code\Crawler\file\file.html')
