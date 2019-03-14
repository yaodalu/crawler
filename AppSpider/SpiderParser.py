#coding:utf-8
import json
import jsonpath
from SpiderDownloader import SpiderDownloader


class SpiderParser(object):

    def get_kw_album(self, response):
        '''
        获取分类下的曲目
        :param response:
        :return:
        '''
        try:
            album_json = json.loads(response, encoding="utf-8") #dict
            album_info = []

            itemList = []
            itemList = jsonpath.jsonpath(album_json,'$..item')
            for item in itemList:
                if item.has_key("id"):
                    album_id = item["id"]
                    album_name= item["title"]
                    album_info.append({'albumId':album_id ,'albumName':album_name})
            return album_info
        except Exception,e:
            print e
      

    def get_kw_track(self,response):
        '''
        获取某一曲目的详细信息
        :param response:
        :return:
        '''
        try:
            track_json = json.loads(response, encoding="utf-8")
            track_info=[]
            trackList = track_json["data"]["tracks"]["list"]
            for track in trackList:
                track_id = track["trackId"]
                track_name= track["title"]
                track_link = track["playUrl64"]
                track_info.append({'trackId':track_id ,'trackName':track_name,'trackLink':track_link})
            return track_info
        except Exception,e:
            print e
    
       

if __name__ == "__main__":
    Downloader = SpiderDownloader()
    Parser = SpiderParser()
    album_url = 'http://search.ximalaya.com/front/v1?appid=0&condition=relation&core=chosen&device=android&deviceId=ce47d0d4-7391-3be3-a5f7-1f8b683321ab&kw=%E5%B2%B3%E4%BA%91%E9%B9%8F&live=true&network=wifi&operator=0&page=1&paidFilter=false&picVersion=13&plan=c&rows=20&scale=2&search_version=1.4&spellchecker=true&version=6.5.3'
    track_url = 'http://mobile.ximalaya.com/mobile/v1/album/ts-1552364593682?ac=WIFI&albumId=11219576&device=android&isAsc=true&isQueryInvitationBrand=true&pageId=1&pageSize=20&pre_page=0&source=0&supportWebp=true'
    print Parser.get_kw_track(Downloader.download(track_url))

