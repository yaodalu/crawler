# -*- coding: utf-8 -*-
import codecs

class HtmlOutput(object):
    def __init__(self):
        self.path = r'D:\test_0321\ximalayaSpider\ximalaya.html'
        self.output_head()

    def output_head(self):
        '''
        将HTML头写进去
        '''
        fout = codecs.open(self.path,'w',encoding = 'utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.close()

    def output_album(self,data):
        '''
        将专辑写入HTML文件中
        '''
        if data == None:
            return
        fout =  codecs.open(self.path,'a',encoding = 'utf-8')
        fout.write("<p>%s----%s" %(data['albumId'],data['albumName']))
        fout.close()

    def output_track(self,datas):
        '''
        将曲目写入HTML文件中
        '''
        if datas == None:
            return
        fout =  codecs.open(self.path,'a',encoding = 'utf-8')
        fout.write("<table>")
        for data in datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %data['trackId'])
            fout.write("<td>%s</td>" %data['trackName'])
            fout.write("<td>%s</td>" %data['trackLink'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</p>")
        fout.close()

    def output_end(self):
        '''
        输出HTML尾
        '''
        fout=codecs.open(self.path,'a',encoding='utf-8')
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
