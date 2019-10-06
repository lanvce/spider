from lxml import etree
import requests

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

selector=etree.HTML(html_doc)
#去除页面所有链接
links=selector.xpath('//p[@class="story"]/a/@href')
for link in links:
    print(link)

r=requests.get('http://iguye.com/books.xml')
se=etree.HTML(r.text)
print(se.xpath('book'))
print(se.xpath('//book'))