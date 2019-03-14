#coding:utf-8
import requests
import chardet
import urllib

class HtmlDownloader(object):
    def download(self,url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers,timeout = 2)
        if r.status_code==200:
            r.encoding = chardet.detect(r.content)['encoding'] #自动检测编码
            return r.text #返回r.text而不是r.content，是为了统一成unicode
        return None

if __name__ == "__main__":
    url =   'https://www.douban.com/tag/'+urllib.quote('算法')+'/book?start='+str(2*15)
    htmldownloader = HtmlDownloader()
    htmldownloader.download(url)
   
