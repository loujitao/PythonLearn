# -*- coding: utf-8 -*-
import scrapy


class LebbSpider(scrapy.Spider):
    name = 'lebb'
    allowed_domains = ['www.lebanban.com']
    start_urls = ['https://www.lebanban.com/course/search?categoryId=70777&courseType=1']

    # https: // www.lebanban.com / course / play.json?traceId = 58654858722

    def parse(self, response):
        pass
