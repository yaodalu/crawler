# -*- coding: utf-8 -*-
#requests库与urllib相比，不需要导入ssl，即可爬取https网页
import requests


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
r = requests.get(url,headers = headers) 
print r.status_code #html状态码
print r.encoding #html编码类型
print r.text  #html内容

