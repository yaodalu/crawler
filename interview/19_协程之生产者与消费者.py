#-*-coding:utf-8
def consumer():
    status = True
    while True:
        n = yield status
        print(u"我拿到了{}！".format(n))
        if n== 3:
            status = False

def producer(consumer):
    n = 5
    while n >0:
        yield consumer.send(n)
        n -=1

if __name__ == "__main__":
    c = consumer()
    c.send(None)
    p = producer(c)
    for status in p:
        if status == False:
            print(u"我只要3,4,5就行")
            break
    print(u"程序结束")
