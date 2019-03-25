# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import os,time,random

def proc_write(q,urls):
    print('Process %s is writing...' %os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...'%url)
        time.sleep(1)

def proc_read(q):
    print('Process %s is reading...' %os.getpid())
    url = q.get(True)
    print('Get %s from queue.'%url)


if __name__ =='__main__':
    #创建队列
    q = Queue()

    #创建进程
    procWriter1 = Process(target = proc_write,args=(q,['url1','url2','url3']))
    procWriter2 = Process(target = proc_write,args=(q,['url4','url5','url6']))
    procReader = Process(target = proc_read,args=(q,))

    #启动进程
    procWriter1.start()
    procWriter2.start()
    procReader.start()
    procWriter1.join()
    procWriter2.join()
    procReader.terminate()
    

 
