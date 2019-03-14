# -*- coding: utf-8 -*-
import urllib
import urlparse
import urllib2

#urllib.quote() -> Python3 urllib.request.quote 3可以显示，2不可以
#url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
#urllib.unquote(url) 

#urllib.urlretrieve()->Python3 urllib.request.urlretrieve()效果相同
#urllib.urlretrieve(url,filename=r'C:\Users\1\Desktop\file.html')

#urllib.urlopen()->Python3 urllib.request.urlopen
#urllib.urlopen(url).read()

#urllib.urlencode() -> Python3 urllib.parse.urllencode() 效果相同
#postdata = {'user':'YLin','password':'1234'}
#urllib.urlencode(postdata) 




#urlparse.urljoin() -> Python3 urllib.parse.urljoin()效果相同
#url1 = 'https://movie.douban.com/'
#url2 = '/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
#urlparse.urljoin(url1,url2)

#urlparse.urlparse()-> Python3 urllib.parse.urlparse()效果相同
#解析url
#ParseResult(scheme='https', netloc='movie.douban.com', path='/typerank', params='', query='type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=', fragment='')
#urlparse.urlparse(url) 




#urllib2.urlopen()-> Python3 urllib.request.urlopen()效果相同 
#urllib2.Request -> Python3 urllib.request.Request()效果相同




#urllib2.HTTPError -> Python3 urllib.error.HTTPError效果相同
#urllib2.URLError -> urllib.error.URLError
