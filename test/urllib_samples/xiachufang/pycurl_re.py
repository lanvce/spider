import os
import re
from pycurl import Curl
from urllib.parse import urlparse
from io import BytesIO


#用curl和正则方法爬取下厨房图片 后面内容与resquests_bs4类似 省略
buffer=BytesIO()
c=Curl()
c.setopt(c.URL,'http://www.xiaochufang.com/')
c.setopt(c.WRITEDATA,buffer)
c.perform()
c.close()

body=buffer.getvalue()
text=body.decode('utf-8')
print(text)


img_list=re.findall(r'src=\"(http://i2\.chuimg\.com/\w+\.jpg)',text)

img_dir=os.path.join(os.curdir,'images')
#if not os.path.isdir(img_dir):
 #   os.mkdir(img_dir)

for img in img_list:
    o=urlparse(img)
    filename=o.path[1:].split('@')[0]
    filepath=os.path.join(img_dir,filename)
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))
    url='%s://%s/%s'%(o.scheme,o.netloc,filename)
    print(url)
    with open (filepath,'wb') as f:
        c=Curl()
        c.setopt(c.URL,url)
        c.setopt(c.WRITEDATA,f)
        c.perform()
        c.close()

