# -*- coding: utf-8 -*-
#协程是一种用户级的轻量级线程
#协程拥有自己的寄存器上下文和栈。
#协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈
#因此协程能保留上一次调用的状态
from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import threading
from gevent.pool import Pool


def run_task(url):
    print 'Visit --> %s on thread %s' %(url,threading.currentThread().name)
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print "%d bytes received form %s." %(len(data),url)
    except Exception,e:
        print e

if __name__ == "__main__":
    urls = ['https://github.com/','https://www.python.org/','http://www.cnblogs.com/']
    #创建协程
    #三个协程属于一个线程
    #greenlets = [gevent.spawn(run_task,url) for url in urls]
    #启动协程
    #gevent.joinall(greenlets)

    #创建协程池
    pool = Pool()
    results = pool.map(run_task,urls)
    print results
