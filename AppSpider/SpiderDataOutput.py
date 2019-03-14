#coding:utf-8
import codecs
class SpiderDataOutput(object):
    def __init__(self):
        self.path=r'C:\Users\1\Desktop\python_code\ApiCrawler\APISpider\ximalaya.html'
        self.output_head()

    def output_head(self):
        '''
        将HTML头写进去
        :return:
        '''
        fout=codecs.open(self.path,'w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()
        
    def output_album(self,data):
        '''
        将专辑写入HTML文件中
        :param path: 文件路径
        :return:
        '''
        if data==None:
            return
        fout=codecs.open(self.path,'a',encoding='utf-8')
        fout.write("<p>%s----%s</p>"%(data["albumId"],data["albumName"]))
        fout.close()
        
        
    def output_track(self,datas):
        '''
        将曲目写入HTML文件中
        :param path: 文件路径
        :return:
        '''
        if datas==None:
            return
        fout=codecs.open(self.path,'a',encoding='utf-8')
        for data in datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['trackId'])
            fout.write("<td>%s</td>"%data['trackName'])
            fout.write("<td>%s</td>"%data['trackLink'])
            fout.write("</tr>")
        fout.close()

    def output_end(self):
        '''
        输出HTML结束
        :param path: 文件存储路径
        :return:
        '''
        fout=codecs.open(self.path,'a',encoding='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
        
if __name__ == "__main__":
    data = [{'trackLink': u'http://audio.xmcdn.com/group33/M02/61/52/wKgJTFmcIpDgzXtdAHIX5sWlaRE152.mp3', 'trackId': 55463323, 'trackName': u'\u300a\u6709\u54f2\u7406\u7684\u4eba\u300b\u5cb3\u4e91\u9e4f \u5b59\u8d8a'}]
    DataOutput = SpiderDataOutput()
    DataOutput.output_track(data)
    DataOutput.ouput_end()
    
