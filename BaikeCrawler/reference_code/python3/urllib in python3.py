import urllib.request
import urllib.parse
import urllib.error

#urllib.request.quote()
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
#print (urllib.request.unquote(url)) #wd解码

#urllib.request.urlretrieve()
#url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
#urllib.request.urlretrieve(url,filename=r'C:\Users\1\Desktop\file.html')

#urllib.request.urlopen()
#print (urllib.request.urlopen(url).read())

#urllib.parse.urlencode()
#postdata = {'user':'YLin','password':'1234'}
#print (urllib.parse.urlencode(postdata)) #password=1234&user=YLin

#urllib.parse.urljoin()
#url1 = 'https://movie.douban.com/'
#url2 = '/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
#print (urllib.parse.urljoin(url1,url2))

#urllib.parse.urlparse()
print (urllib.parse.urlparse(url)) 

#urllib.request.Request()

#urllib.request.urlopen()

#urllib.error.URLError

#urllib.error.HTTPError
