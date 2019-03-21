import requests

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent = 'ting_6.5.3(DUK-AL20,Android22)'
        headers = {"User-Agent":user_agent}
        r = requests.get(url,headers = headers)
        if r.status_code == 200:
            return r.text
        return None
    
