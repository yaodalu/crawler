#python3
import urllib.request
import re
import os 

def imageCrawler(url,topath):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request .urlopen (req,timeout = 0.5)
    infoStr = response.read().decode('utf-8')

    re_image = re.compile ('img width="200" height="200" src="(.*?)" alt=',flags = re.M)
    imageList = re_image.findall(infoStr)
    for i in range(len(imageList)):
        path = os.path.join (topath,str(i)+'.jpg')
        newUrl = 'http:'+imageList[i]
        urllib.request.urlretrieve(newUrl,filename=path)
    
url='http://search.yhd.com/p/c5020-mbname-b/a-s1-v0-p1-price-d0-pid-pt50000083549-pl1-m0-k'
topath = r'C:\Users\1\Desktop\python code\Crawler\file'
imageCrawler(url,topath)



