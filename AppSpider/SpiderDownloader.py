#coding:utf-8
import requests
class SpiderDownloader(object):

    def download(self,url):
        if url is None:
            return None
        user_agent = 'ting_6.5.3(DUK-AL20,Android22)'
        headers={'User-Agent':user_agent}
        r = requests.get(url,headers=headers)
        if r.status_code==200:
            return r.text
        return None
        #return r.content

if __name__ == '__main__':
    url = 'http://search.ximalaya.com/front/v1?appid=0&condition=relation&core=chosen&device=android&deviceId=ce47d0d4-7391-3be3-a5f7-1f8b683321ab&kw=%E5%B2%B3%E4%BA%91%E9%B9%8F&live=true&network=wifi&operator=0&page=1&paidFilter=false&picVersion=13&plan=c&rows=20&scale=2&search_version=1.4&spellchecker=true&version=6.5.3'
    downloader = SpiderDownloader()
    print downloader.download(url)


