# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool
import os,time,random
'''
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
'''

def run_task(name):
    print 'Task %s (pid=%s) is running...' %(name, os.getpid())
    time.sleep(random.random()*3)
    print 'Task %s (pid=%s) end.' %(name, os.getpid())

if __name__ == "__main__":
    print 'Current process %s.' %os.getpid()
    p = Pool(processes =4) #请求大于进程数量4时，阻塞
    for i in range(5):
        p.apply_async(run_task,args=(i,))
    print 'Waiting for all subprocesses done...'
    #进程池不再增加新的进程
    p.close()
    p.join()
    print 'All subprocesses done.'
