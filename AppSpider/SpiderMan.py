#coding:utf-8
from SpiderDataOutput import SpiderDataOutput
from SpiderDownloader import SpiderDownloader
from SpiderParser import SpiderParser


class SpiderMan(object):

    def __init__(self):
        self.downloader = SpiderDownloader()
        self.parser = SpiderParser()
        self.output = SpiderDataOutput()
        
    def crawl(self,root_url):
        album_response = self.downloader.download(root_url)
        for album in self.parser.get_kw_album(album_response):
            self.output.output_album(album)
            track_url = 'http://mobile.ximalaya.com/mobile/v1/album/ts-1552364593682?ac=WIFI&albumId=%d&device=android&isAsc=true&isQueryInvitationBrand=true&pageId=1&pageSize=20&pre_page=0&source=0&supportWebp=true' %album['albumId']
            track_response = self.downloader.download(track_url)
            track_info = self.parser.get_kw_track(track_response)
            self.output.output_track(track_info)
        self.output.output_end()



if __name__ =="__main__":
    spider = SpiderMan()
    spider.crawl('http://search.ximalaya.com/front/v1?appid=0&condition=relation&core=chosen&device=android&deviceId=ce47d0d4-7391-3be3-a5f7-1f8b683321ab&kw=%E5%B2%B3%E4%BA%91%E9%B9%8F&live=true&network=wifi&operator=0&page=1&paidFilter=false&picVersion=13&plan=c&rows=20&scale=2&search_version=1.4&spellchecker=true&version=6.5.3')



