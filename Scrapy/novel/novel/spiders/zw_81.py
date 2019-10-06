# -*- coding: utf-8 -*-
import scrapy


class Zw81Spider(scrapy.Spider):
    name = 'zw_81'
    allowed_domains = ['zwdu.com']
    start_urls = ['https://www.zwdu.com/book/10304/1841836.html']

    def parse(self, response):
        title=response.xpath('//h1/text()').extract_first()
        #text不是字符串
        content=' '.join(response.xpath('//div[@id="content"]/text()').extract()).replace('     ','\n')

        next_page=response.xpath('//div[@class="bottem2"]/a[3]/@href').extract_first()

        yield {
            'title':title,
            'content':content
        }
        if next_page.find('.html')!=-1:
            yield  scrapy.Request(response.urljoin(next_page),callback=self.parse)

