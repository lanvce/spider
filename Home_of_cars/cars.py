import requests
from lxml import etree


def fetch_links(url):
    res=requests.get(url).text
    return res


def in_page(url):
    r=requests.get(url).text
    re=etree.HTML(r)
    img_urls=re.xpath('//div[@class="x-loaded"]/img/@src')
    data=[]
    for img_url in img_urls:
        img_url='http:%s' %img_url
        data=data.append(img_url)
        return data




if __name__=='__main__':
    start_url = 'https://club.autohome.com.cn/jingxuan/104/1#pvareaid=3311563'
    r=fetch_links(start_url)
    selector=etree.HTML(r)
    links=selector.xpath('//div[@class="pic-box"]/a/@href')
    list=[str(link) for link in links]
    #
    # for url in list:
    #
    url='https:%s' % list[0]
    print(url)

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
         'AppleWebKit/537.36 (KHTML, like Gecko) ' \
         'Chrome/75.0.3770.142 Safari/537.36'

    headers = {
        'User-Agent': ua

    }

    r=requests.get(url,headers=headers)
    print(r.text)
    #     #print(in_page(link))

     #   r = requests.get(link).text
   # print(link)
        # re = etree.HTML(r)
        # img_urls = re.xpath('//div[@class="x-loaded"]/img/@src')
        # print(img_urls)




