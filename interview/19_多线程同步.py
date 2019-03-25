# -*- coding: utf-8 -*-
#使用Thread对象的Lock和RLock可以实现线程同步，这两个对象都有acquire和release方法
#LOCK对象，如果一个线程连续两次发出acquire请求，第一次acquire之后，没有release,就会发生死锁
#RLOCK对象允许一个线程多次对其进行acquire操作，自动release

import threading

myLock = threading.RLock()
num = 0
class myThread(threading.Thread):
    def __init__(self,name):
        super(myThread,self).__init__()
        self.name = name

    def run(self):
        global num
        while True:
            myLock.acquire()
            print '%s locked, Number: %d' %(threading.currentThread().name,num)
            if num>=4:
                myLock.release()
                print '%s released, Number: %d' %(threading.currentThread().name,num)
                break
            num +=1
            print '%s released, Number: %d' %(threading.currentThread().name,num)
            myLock.release()

if __name__ == "__main__":
    thread1 = myThread('Thread1')
    thread2 = myThread('Thread2')
    thread1.start()
    thread2.start()
