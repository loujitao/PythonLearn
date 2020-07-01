# -*- coding: utf-8 -*-
import scrapy


class LebbSpider(scrapy.Spider):
    name = 'lebb'
    allowed_domains = ['www.lebanban.com']
    start_urls = ['http://www.lebanban.com/']

    # https: // www.lebanban.com / course / play.json?traceId = 58654858722

    def parse(self, response):
        pass
