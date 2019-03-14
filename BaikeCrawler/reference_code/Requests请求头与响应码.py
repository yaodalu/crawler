# -*- coding: utf-8 -*-
import requests
#请求头
headers = headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
r = requests.get('http://www.baidu.com',headers = headers)
print r.content

#响应码和响应头
if r.status_code == requests.codes.ok:
    print r.status_code 
    print r.headers #包含set-cookie
    print r.headers.get('content-type')
else:
    r.raise_for_status 
