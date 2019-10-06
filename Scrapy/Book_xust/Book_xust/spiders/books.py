# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['lib.xust.edu.cn']
    start_urls = ['http://61.150.69.38:8080/browse/cls_browsing.php']

    def parse(self, response):
        r=response.xpath('//strong/text()').extract_first()
        # v=r.decode('GBK')
        yield{
           'title': r
        }
