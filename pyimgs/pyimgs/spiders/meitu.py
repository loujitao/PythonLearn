# -*- coding: utf-8 -*-
import scrapy
import  logging

logger=logging.getLogger(__name__)


class MeituSpider(scrapy.Spider):
    name = 'meitu'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['http://www.meitulu.com/']

    def parse(self, response):

        pass
