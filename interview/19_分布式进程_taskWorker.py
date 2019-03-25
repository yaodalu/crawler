# -*- coding: utf-8 -*-
import Queue
from multiprocessing.managers import BaseManager
import time

class QueueManager(BaseManager):
    pass

#将本地队列在网络上进行注册，暴露给其他进程
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#绑定服务器端口

m = QueueManager(address = ('127.0.0.1',8001),authkey = b'qiye')

#连接服务器
m.connect()

#获取网络上的队列
task = m.get_task_queue()
result = m.get_result_queue()

while(not task.empty()):
    image_url = task.get(True,timeout = 5)
    print('run task download %s ...' %image_url)
    time.sleep(1)
    result.put('%s---->success'%image_url)

print ('worker.exit.')
