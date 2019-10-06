# -*- coding: utf-8 -*-
import scrapy


class UsnewsSpider(scrapy.Spider):
    name = 'usnews'
    #允许爬的链接写在里面
    allowed_domains = ['http://www.qianmu.org']
    start_urls = ['http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D']

    def parse(self, response):
#解析链接 并提取 extract返回的永远是一个列表
        links = response.xpath('//div[@id="content"]//tr[position()>1]/td[2]/a/@href').extract()
        # print(type(links))

        for link in links:
            if not link.startswith('http://www.qianmu.org'):
                link = 'http://www.qianmu.org/%s' % link
                #继续跟随link 然后请求link 成功之后会调用callback函数处理
            yield response.follow(link,self.parse_university)

    def parse_university(response):
    #处理大学详情页面


        data={}
        data['name']=response.xpath('//div[@id="wikiContent"]/h1/text()')[0]#去掉列表[]符号
        table=response.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table')
        if table:
            table=table[0]
            keys=table.xpath('.//td[1]/p/text()')

            cols=table.xpath('.//td[2]')
            #当确定解析出来的内容只有一个 可使用extract_first()提取
            values=[' '.join(col.xpath('.//text()').extract_first()) for col in cols]

            if len(keys)!=len(values):

                data.update(zip(keys,values))
    #yield出去的数据 会被框架进行下一步处理
    #如果没有 则会打印到控制台
        yield data