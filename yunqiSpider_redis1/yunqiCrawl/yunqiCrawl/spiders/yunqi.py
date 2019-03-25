# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yunqiCrawl.items import YunqiBookListItem,YunqiBookDetailItem

class YunqiSpider(CrawlSpider):
    name = 'yunqi'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n30p1']

    rules = (
        Rule(LinkExtractor(allow=r'bk/so2/n30p\d+'), callback='parse_book_list', follow=True),
    )

    def parse_book_list(self,response):
        nodeList = response.xpath('//div[@class="book"]')
        for node in nodeList:
            bookListItem = YunqiBookListItem()
            
            bookListItem['novelId'] = node.xpath('.//div[@class="book_info"]/h3/a/@id').extract()[0].split("_")[-1]
            bookListItem['novelName'] = node.xpath('.//div[@class="book_info"]/h3/a/text()').extract()[0]
            bookListItem['novelLink'] = node.xpath('.//div[@class="book_info"]/h3/a/@href').extract()[0]
            bookListItem['novelAuthor'] = node.xpath('.//div[@class="book_info"]/dl[1]/dd[1]/a/text()').extract()[0]
            bookListItem['novelType'] = node.xpath('.//div[@class="book_info"]/dl[1]/dd[2]/a/text()').extract()[0]
            bookListItem['novelStatus'] = node.xpath('.//div[@class="book_info"]/dl[1]/dd[3]/text()').extract()[0]

            bookListItem['novelUpdateTime'] = node.xpath('.//div[@class="book_info"]/dl[2]/dd[1]/text()').extract()[0]

            bookListItem['novelWords'] = node.xpath('.//div[@class="book_info"]/dl[2]/dd[2]/text()').extract()[0]
            bookListItem['novelImageUrl'] = u'http:'+ node.xpath('./a/img/@src').extract()[0]

            yield bookListItem

            request = scrapy.Request(url=str(bookListItem['novelLink']),callback = self.parse_book_detail)
            request.meta['novelId'] = bookListItem['novelId'] #在子函数中用response.meta传递
            yield request
    
    def parse_book_detail(self,response):
        bookDetailItem = YunqiBookDetailItem()
        bookDetailItem["novelId"] = response.meta["novelId"]
        bookDetailItem["novelLabel"]  = response.xpath('//div[@class="tags"]/text()').extract()[0]

        node = response.xpath('//div[@id="novelInfo"]')

        #注意源代码中没有tbody标签
        bookDetailItem["novelAllClick"] = node.xpath('.//table/tr[2]/td[1]/text()').extract()[0]
        bookDetailItem["novelMonthClick"] = node.xpath('.//table/tr[3]/td[1]/text()').extract()[0]
        bookDetailItem["novelWeekClick"] = node.xpath('.//table/tr[4]/td[1]/text()').extract()[0]

        bookDetailItem["novelAllPopular"] = node.xpath('.//table/tr[2]/td[2]/text()').extract()[0]
        bookDetailItem["novelMonthPopular"] = node.xpath('.//table/tr[3]/td[2]/text()').extract()[0]
        bookDetailItem["novelWeekPopular"] = node.xpath('.//table/tr[4]/td[2]/text()').extract()[0]

        bookDetailItem["novelCommentNum"] = node.xpath('.//table/tr[5]/td[2]/text()').extract()[0]
        bookDetailItem["novelAllComm"] = node.xpath('.//table/tr[2]/td[3]/text()').extract()[0]
        bookDetailItem["novelMonthComm"] = node.xpath('.//table/tr[3]/td[3]/text()').extract()[0]
        bookDetailItem["novelWeekComm"] = node.xpath('.//table/tr[4]/td[3]/text()').extract()[0]

        yield bookDetailItem
        
