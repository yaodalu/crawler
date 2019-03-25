#coding:utf-8
import codecs
import time #生成的文件按照当前时间进行命名

#将爬取到的数据写成HTML格式
class DataOutput(object):

    def __init__(self):
        self.filepath = r'C:\Users\1\Desktop\python_code\distributionCrawler\ControlNode\baike_%s.html' %(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))#当地时间
        self.output_head(self.filepath) 
        self.datas=[]
        
    def store_data(self,data):#data与self.datas?
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_html(self.filepath) #缓冲写入

    def output_head(self,path):
        '''
        将HTML头写进去
        :return:
        '''
        fout = codecs.open(path,'w',encoding = 'utf-8')
        fout.write("<html>")
        fout.write(r'''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />''')
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_html(self,path):
        '''
        将数据写入HTML文件中
        :param path：文件路径
        :return:
        '''
        fout = codecs.open(path,'a',encoding = 'utf-8')
        for data in self.datas:
            fout.write("<tr>") #行
            fout.write("<td>%s</td>"%data['url']) #列
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")
        self.datas=[]
        fout.close()

    def output_end(self,path):
        '''
        输出HTML结束
        :param path:文件存储路径
        :return:
        '''
        fout = codecs.open(path,'a',encoding = 'utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

