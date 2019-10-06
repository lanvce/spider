import requests
from lxml import etree

start_url='http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
def fetch(url):
    #请求下载网页
    r=requests.get(url)
    if r.status_code!=200:
        r.raise_for_status()
    return r.text.replace("\t",'')

def parse_university(link):
#处理大学详情页面

    selector=etree.HTML(fetch(link))
    data={}
    data['name']=selector.xpath('//div[@id="wikiContent"]/h1/text()')[0]#去掉列表[]符号
    table=selector.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table')
    if table:
        table=table[0]
        keys=table.xpath('.//td[1]/p/text()')

        cols=table.xpath('.//td[2]')
        values=[' '.join(col.xpath('.//text()')) for col in cols]

        if len(keys)!=len(values):
            return None
        data.update(zip(keys,values))
        #print(data)
        return data
#处理数据
def process_data(data):
    if data:
        print(data)
    #else:
     #   print("data无数据")

if __name__=='__main__':
    #请求入口页面
    selector = etree.HTML(fetch(start_url))
    #提前列表页面链接
    links = selector.xpath('//div[@id="content"]//tr[position()>1]/td[2]/a/@href')
    #print(type(links))

    for link in links:
        if not link.startswith('http://www.qianmu.org'):
            link = 'http://www.qianmu.org/%s' % link
        #提取详情页信息
        data=parse_university(link)
        #处理信息
        process_data(data)