#python3
import urllib.request
import ssl
import re


def pageCrawler(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req,context = context, timeout =1.5)
    infoStr = response.read().decode('utf-8')
    return infoStr

url = 'https://www.qiushibaike.com/text/page/2/'
info = pageCrawler(url)

re_total = re.compile ('<h2>.*?<span>.*?</span>',flags=re.S)
re_name = re.compile ('<h2>(.*?)</h2>',flags = re.S)
re_mes = re.compile ('<span>\n\n\n(.*?)\n\n</span>',flags = re.S)

dict={}
infoList = re_total.findall(info)


for count in range(len(infoList)):
  name = re_name.findall (infoList[count])
  name = name[0]
  mes = re_mes.findall (infoList[count])
  mes = mes[0]
  dict[name] = mes

print(dict)

