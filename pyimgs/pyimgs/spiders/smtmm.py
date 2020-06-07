# -*- coding: utf-8 -*-
import scrapy
import time
from copy import deepcopy

class MeituSpider(scrapy.Spider):
    name = 'smtmm'
    allowed_domains = ['smtmm.win/']
    start_urls = ['https://smtmm.win/']
    # start_urls = ['https://smtmm.win/type/1/']
    # https://smtmm.win/type/{1-6}/?page={1-?}

    def parse(self, response):
        page_urllist = response.xpath("//div[@class='excerpts']/article/a[@class='thumbnail']/h2/a[@href]")
        for page in page_urllist:
            item = {}
            item["href"] = "https://smtmm.win" + page.xpath("@href").extract_first()
            item["text"] = page.xpath("text()").extract_first()
            yield item
        next_url="https://smtmm.win/type/1/"+response.xpath("//div[@class='pagination pagination-multi']/ul/li[@class='next-page']/a/@href").extract_first()
        yield scrapy.Request(next_url,callback=self.parse,dont_filter=False)
            #实际图片地址：
        #https://smtmm.win   /static/images/mm131/20200604/5515/14.jpg

        #https://smtmm.win/article/{52623- 52453}/
        #10*17