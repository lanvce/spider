import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

r=requests.get('http://www.xiachufang.com/')
soup=BeautifulSoup(r.text)
#print(soup)
#print(soup.select('img'))


img_list=[]
for img in soup.select('img'):
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])
#倒数两个是新浪图标
img_list=img_list[0:-2]
#print(img_list)
#初始化下载文件目录
img_dir=os.path.join(os.curdir,'images')
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)

for img in img_list:
    o=urlparse(img)
    filename=o.path[1:].split('@')[0]
    filepath=os.path.join(img_dir,filename)
    url='%s://%s/%s'%(o.scheme,o.netloc,filename)
    print(url)

    res=requests.get(url)
    with open(filepath,'wb') as f:
        for chunk in res.iter_content(1024):
            f.write(chunk)




#linux下一行命令爬取照片
#curl -s http://www.xiachufang.com/|grep -oP '(?<=src=\")http://i2\.chuimg\.com/\.jpg'|xargs -i curl --create-dir {} -o ./image/{}