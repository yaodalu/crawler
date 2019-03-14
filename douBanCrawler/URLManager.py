#coding:utf-8
import urllib

class UrlManager(object):
    def __init__(self):
        self.old_urls = set()#已爬取URL集合
    def get_new_url(self,page_index,book_tag):
        '''
        获取一个指定book_tag和指定页数的URL
        :return:
        '''
        new_url = 'https://www.douban.com/tag/'+urllib.quote(book_tag)+'/book?start='+str(page_index*15)
        self.old_urls.add(new_url) 
        return new_url

    def old_url_size(self):
        '''
        获取已经爬取URL集合的大小
        :return:
        '''
        return len(self.old_urls)

if __name__ == '__main__':
    urlmanager = UrlManager()
    print urlmanager.get_new_url(1,'小说')
