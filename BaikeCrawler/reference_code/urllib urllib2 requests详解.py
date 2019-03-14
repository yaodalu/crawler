# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib

'''
#GET请求
url = "http://www.zhihu.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"}
req = urllib2.Request(url,headers)
response = urllib2.urlopen()
html = response.read()

#POST请求
url = 'http://www.xxxxxxx.com/login'
postdata = {'username':'YLin',\
            'password':'1234'}
data = urllib.urlencode(postdata)#编码？username=YLin&password=1234 urllib2没有
req = urllib2.Request(url,data) #请求体里包含url,data,headers,请求头里包含 User-agent,refer,contentType
response = urllib2.urlopen(req) #urlopen 参数 context,url,timeout
html = response.read()


#cookie自动处理
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com')
print response
for item in cookie:
    print item.name+':'+item.value

#自定义Cookie???
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie','email='+'xxxxxxx@163.com'))
req = urllib2.Request('http://www.zhihu.com')
response = opener.open(req)
print response.headers
retdata = response.read()
'''

#Proxy代理
proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8087'})
opener = urllib2.build_opener([proxy])
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.zhihu.com')
print response.read()
