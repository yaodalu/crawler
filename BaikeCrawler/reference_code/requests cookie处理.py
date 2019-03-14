# -*- coding: utf-8-*-
import requests
#获取cookie字段的值
headers = headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
r = requests.get('http://www.baidu.com',headers=headers)
#for cookie in r.cookies.keys():
    #print cookie + ':' + r.cookies.get(cookie)
'''
H_PS_PSSID:28230_1455_21124_18559_28131_26350_28267_27245_22160
delPer:0
BDSVRTM:0
BD_HOME:0
'''

#自定义Cookie值
#cookies = {'name':'qiye','age':'10'}
#另一种构造词典的方式
#cookies = dict(name = 'qiye',age = '10')
#print cookies
#print isinstance(cookies,dict)
#cookies写在请求头中
#r = requests.get('http://www.baidu.com',headers = headers,cookies = cookies)
#print r.content

#session？？？
