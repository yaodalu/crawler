#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return:返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'lxml',from_encoding='utf-8')#html.parser是Python自带的解析库
        new_urls = self._get_new_urls(page_url,soup)#方法前加_是为什么？不是库的外部接口，私有方法？
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data


    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup:soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标签
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url =urlparse.urljoin(page_url,new_url)
            #set添加元素不支持'+=',只能使用add()
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup:
        :return:返回有效数据
        '''
        data={}
        data['url']=page_url
        #find单个，findAll返回列表
        #因为class是关键词，所以加_
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        #title.get_text()得到是unicode的字符串，并且能够在多个子标签中获取
        #而title.string得到的是NavigableString，需要unicode(title.string)
        data['title']=title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        #获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary']=summary.get_text()#get_text是什么方法
        return data
