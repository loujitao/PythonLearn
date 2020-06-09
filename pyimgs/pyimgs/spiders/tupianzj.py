# -*- coding: utf-8 -*-
import scrapy


class TupianzjSpider(scrapy.Spider):
    name = 'tupianzj'
    allowed_domains = ['tupianzj.com']
    start_urls = ['http://tupianzj.com/']

    def parse(self, response):
        pass
