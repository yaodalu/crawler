# -*- coding: utf-8-*-
import requests
from lxml import etree
import chardet
import json
import codecs
import threading
from Queue import Queue

class threadCrawl(threading.Thread):
    '''
    请求线程:网络IO
    '''
    def __init__(self,threadName,pageQueue,dataQueue):
        super(threadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
    def run(self):
        print "启动采集线程： "+self.threadName
        while not CRAWL_EXIT:
                 try:
                     page = self.pageQueue.get(False)
                     url =  'https://movie.douban.com/top250?start=' + str(page*25)
                     user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                     headers={'User-Agent':user_agent}
                     r = requests.get(url,headers = headers)
                     if r.status_code==200:
                         r.encoding = chardet.detect(r.content)['encoding'] 
                         self.dataQueue.put(r.text)
                 except:
                     pass
        print  "结束采集线程： "+self.threadName


class threadParse(threading.Thread):
    '''
    解析存储线程:磁盘IO
    '''
    def __init__(self,threadName,dataQueue,lock,f):
        super(threadParse,self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.lock = lock
        self.f = f
    def run(self):
        print "启动解析线程： "+self.threadName
        while not PARSE_EXIT:
            try:
                r = self.dataQueue.get(False)
                html = etree.HTML(r)
                nodeList = html.xpath('//div[@class="info"]')
                for node in nodeList:
                    movie = {}
                    movie["title"] = node.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
                    bodylist  = node.xpath('.//div[@class="bd"]/p/text()')
                    movie["body"] = bodylist[0].strip()+bodylist[1].strip()
                    movie["rank"] = node.xpath('.//div[@class="star"]/span[2]/text()')[0]
                    movie["viewer"] = node.xpath('.//div[@class="star"]/span[4]/text()')[0]
                    if node.xpath('.//p[@class="quote"]/span/text()'):
                        movie["quote"] = node.xpath('.//p[@class="quote"]/span/text()')[0]
                    else:
                        movie["quote"] = ""
                    with self.lock:
                        self.f.write(json.dumps(dict(movie),ensure_ascii=False)+',\n')
            except:
                pass
        print "结束解析线程： "+self.threadName
        
PARSE_EXIT = False
CRAWL_EXIT = False

def main():
    start = time.time()
    pageQueue = Queue(10)
    for i in range(0,10):
        pageQueue.put(i)
    dataQueue = Queue()
    f = codecs.open(r'C:\Users\1\Desktop\python_code\performanceCrawler\movie.json','a',encoding = 'utf-8')
    lock = threading.Lock()

    crawlThreads = [] #?
    crawlList = ["crawl-1","crawl-2","crawls-3"]
    
    parseThreads = []
    parseList = ["parse-1","parse-2","parse-3"]

    for threadName in crawlList:
        thread = threadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        crawlThreads.append(thread)
    for threadName in parseList:
        thread = threadParse(threadName,dataQueue,lock,f)
        thread.start()
        parseThreads.append(thread)

    while not pageQueue.empty():
        pass
    global CRAWL_EXIT   
    CRAWL_EXIT = True
    for thread in crawlThreads:
        thread.join()
        print "1"
        
    while not dataQueue.empty():
        pass
    global PARSE_EXIT   
    PARSE_EXIT = True
    for thread in parseThreads:
        thread.join()
        print "2"
        
    with lock:
        #关闭文件？
         f.close()
    end = time.time()
    print "经过 %s" %(format(end-start))
    print "谢谢使用！"
    
        
if __name__ =="__main__":
    main()
