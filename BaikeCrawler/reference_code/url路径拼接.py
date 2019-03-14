# -*- coding: utf-8 -*-
import urlparse
import posixpath
#posixpath.normpath()作用

def myjoin(base,url):
    newUrl = urlparse.urljoin(base,url)
    arr = urlparse.urlparse(newUrl)
    path = posixpath.normpath(arr[2])
    return urlparse.urlunparse((arr.scheme,arr.netloc,path,arr.params,arr.query,arr.fragment))

base1 = 'http://www.bagtree.com/'
url1 = '../../themes/bagtree_2011/images/pinzhi.gif'
print myjoin(base1,url1)

base2 = 'http://info.ceo.hc360.com/list/qygl-ldl.shtml'
url2 = '/2011/11/250020188368.shtml'
print myjoin(base2,url2)

base3 = 'http://info.ceo.hc360.com/2012/07/190833206838.shtml'
url3 = '190833206838-2.shtml'
print myjoin(base3,url3)
