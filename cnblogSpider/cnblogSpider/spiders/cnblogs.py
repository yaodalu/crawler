# -*- coding: utf-8 -*-
import scrapy
from cnblogSpider.items import CnblogspiderItem
from scrapy import Selector

class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    #allowed_domains = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    def parse(self, response):
        pageList = response.xpath('//div[@class="day"]')
        
        for page in pageList:
            item = CnblogspiderItem()
            item["url"] = page.xpath('./div[2]/a/@href').extract()[0]
            item["title"] = page.xpath('./div[2]/a/text()').extract()[0]
            item["time"] = page.xpath('./div[1]/a/text()').extract()[0]
            item["content"] = page.xpath('./div[3]/div/text()').extract()[0]
            yield item
            
        next_page =  Selector(response).re(u'<a href="(\S*)">下一页</a>')[0]
        if next_page:
            yield scrapy.Request(url=next_page,callback = self.parse)
