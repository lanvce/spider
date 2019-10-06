# -*- coding: utf-8 -*-
import scrapy


class UsnewsSpider(scrapy.Spider):
    name = 'usnews'
    allowed_domains = ['http://www.qianmu.org']
    start_urls = ['http://http://www.qianmu.org/']

    def parse(self, response):
        pass
