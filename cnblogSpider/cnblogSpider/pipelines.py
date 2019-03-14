# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class CnblogspiderPipeline(object):
    def __init__(self):
        self.f = open(r"D:\Program Files\scrapyProject\cnblogSpider\data\papers.json",'wb')
        
    def process_item(self, item, spider): 
        self.f.write(json.dumps(dict(item))+',\n')
        return item

    
