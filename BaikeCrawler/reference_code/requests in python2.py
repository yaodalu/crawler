# -*- coding: utf-8 -*-
import requests
import urlparse

#Get请求
r = requests.get('http://www.baidu.com')
#print r
#print r.content

#Post请求
postdata = {'key':'value'}
r = requests.post('http://www.xxxx.com/login',data = postdata)
#print r.content

#带param的Get请求
playload = {'keywords':'blog:qiyeboy','pageindex':1}
r = requests.get('http://zzk.cnblogs.com/s/blogpost',params = playload)
#print r.url
#print urlparse.urlparse(r.url)
#print isinstance(r.url,unicode)
#print isinstance(r.url.encode('utf-8'),str)
#ParseResult(scheme=u'https', netloc=u'zzk.cnblogs.com', path=u'/s/blogpost', params='', query=u'keywords=blog%3Aqiyeboy&pageindex=1', fragment='')

