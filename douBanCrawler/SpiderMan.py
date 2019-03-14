#coding:utf-8
from URLManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
        
    def crawlOneTag(self,book_tag):
        page_num = 0
        book_list = []        
        while page_num <= 2:
            try:
                new_url = self.manager.get_new_url(page_num,book_tag)
                html = self.downloader.download(new_url)
                book_list += self.parser.parser(html)
            except Exception as e:
                print("crawl failed")
            page_num += 1
        return book_list

    def crawlAllTags(self,book_tag_lists,topath):
        book_lists = []
        for book_tag in book_tag_lists:
            book_list = self.crawlOneTag(book_tag)
            book_list=sorted(book_list,key=lambda x:x[1],reverse=True)
            book_lists.append(book_list)
        self.output.output(book_lists,book_tag_lists,topath)

if __name__=="__main__":
    #book_tag_lists = ['心理','判断与决策','算法','数据结构','经济','历史']
    book_tag_lists = ['算法','数据结构']
    #book_tag_lists = ['传记','哲学','编程','创业','理财','社会学','佛教']
    #book_tag_lists = ['思想','科技','科学','web','股票','爱情','两性']
    #book_tag_lists = ['计算机','机器学习','linux','android','数据库','互联网']
    #book_tag_lists = ['数学']
    #book_tag_lists = ['摄影','设计','音乐','旅行','教育','成长','情感','育儿','健康','养生']
    #book_tag_lists = ['商业','理财','管理']  
    #book_tag_lists = ['名著']
    #book_tag_lists = ['科普','经典','生活','心灵','文学']
    #book_tag_lists = ['科幻','思维','金融']
    #book_tag_lists = ['个人管理','时间管理','投资','文化','宗教']
    topath = r'C:\Users\1\Desktop\python code\douBanRankCrawler\file'
    spider_man = SpiderMan()
    spider_man.crawlAllTags(book_tag_lists,topath)
