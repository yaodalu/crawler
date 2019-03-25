# -*- coding: utf-8-*-
import random
import time,threading

def thread_run(urls):
    print "Current %s is running..."%threading.current_thread().name
    for url in urls:
        print '%s......%s'%(threading.current_thread().name,url)
        time.sleep(random.random())
    print "Current %s ends..."%threading.current_thread().name

print '%s is running...'%threading.currentThread().name

#通过threading.Thread()方法创建实例
t1 = threading.Thread(target = thread_run,name = 'Thread1',args = (['url1','url2','url3'],))#注意传入的args是一个tuole
t2 = threading.Thread(target = thread_run,name = 'Thread2',args = (['url4','url5','url6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print '%s ends...'%threading.currentThread().name
