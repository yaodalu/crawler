#coding:utf-8
from bs4 import BeautifulSoup
from HtmlDownloader import HtmlDownloader
import codecs

class HtmlParser(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        
    def _get_people_num(self,new_url):
        people_html = self.downloader.download(new_url)
        people_soup = BeautifulSoup(people_html,'lxml')
        num = people_soup.find('a',{'class':'rating_people'}).find('span').string
        return num
    
    def parser(self,html):
        '''
        用于解析网页内容抽取数据
        :param html: 下载的网页内容
        :return:返回数据
        '''
        book_list = []
        
        list_soup = BeautifulSoup(html,'lxml')
        for book_info in list_soup.findAll('dd'):
            title = book_info.find('a', {'class':'title'}).string.strip()
            desc = book_info.find('div', {'class':'desc'}).string.strip()
            desc_list = desc.split('/') 
            book_url = book_info.find('a', {'class':'title'}).get('href')
            try:
                author_info = u'作者/译者： ' + u'/'.join(desc_list[0:-3])
            except:
                author_info =u'作者/译者： 暂无'
            try:
                pub_info = u'出版信息： ' + u'/'.join(desc_list[-3:])
            except:
                pub_info = u'出版信息： 暂无'
            try:
                rating = book_info.find('span', {'class':'rating_nums'}).string.strip()
            except:
                rating=u'0.0'
            try:
                people_num = self._get_people_num(book_url) 
                people_num = people_num.strip(u'人评价')
            except:
                people_num =u'0'

            book_list.append([title,rating,people_num,author_info,pub_info])
        return book_list


    
   
if __name__ =='__main__':
    f = codecs.open(r'C:\Users\1\Desktop\python code\douBanRankCrawler\file\rank.html',encoding = 'utf-8')
    html = f.read()
    htmlparser = HtmlParser()
    book_list=htmlparser.parser(html)
    #print book_list
   
