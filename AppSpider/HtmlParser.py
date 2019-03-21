# -*- coding: utf-8 -*-
from HtmlDownloader import HtmlDownloader
import jsonpath
import json
class HtmlParser(object):
    def get_kw_album(self,response):
        '''
        获取分类下的专辑
        '''
        try:
            album_dict= json.loads(response)
            album_info = []

            itemList = jsonpath.jsonpath(album_dict,'$..item')
            for item in itemList:
                if item.has_key("id"):
                    album_info.append({'albumId':item['id'],'albumName':item['title']})
            return album_info
        except Exception,e:
            print e

    def get_kw_track(self,response):
        '''
        获取某一专辑的详细信息
        '''
        try:
            track_dict = json.loads(response)
            track_info = []
            trackList = track_dict['data']['tracks']['list']
            for track in trackList:
                track_info.append({'trackId':track["trackId"],'trackName':track["title"],'trackLink':track["playUrl64"]})
            return track_info
        except Exception,e:
            print e

if __name__ == "__main__":
    Downloader = HtmlDownloader()
    Parser = HtmlParser()
    album_url = 'http://search.ximalaya.com/front/v1?appid=0&condition=relation&core=chosen&device=android&deviceId=ce47d0d4-7391-3be3-a5f7-1f8b683321ab&kw=%E5%B2%B3%E4%BA%91%E9%B9%8F&live=true&network=wifi&operator=0&page=1&paidFilter=false&picVersion=13&plan=c&rows=20&scale=2&search_version=1.4&spellchecker=true&version=6.5.3'
    track_url = 'http://mobile.ximalaya.com/mobile/v1/album/ts-1552364593682?ac=WIFI&albumId=11219576&device=android&isAsc=true&isQueryInvitationBrand=true&pageId=1&pageSize=20&pre_page=0&source=0&supportWebp=true'
    


