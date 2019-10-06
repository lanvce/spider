from bs4 import BeautifulSoup


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

soup=BeautifulSoup(html_doc,'html.parser')
print(soup)
#打印出标准html格式
#print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
#列出a的所有属性
print(soup.a.attrs)
print(soup.a.attrs['href'])
#判断是否有class属性
print(soup.a.has_attr('class'))



print(list(soup.p.children)[0].text)
print(soup.find_all('a'))




for link in soup.find_all('a'):
# print('网址：',link.get('href'))
    print('网址：',link.attrs['href'])

#获取文本
print(soup.get_text())

