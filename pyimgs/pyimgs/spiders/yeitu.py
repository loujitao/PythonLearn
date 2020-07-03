# -*- coding: utf-8 -*-
import scrapy


class YeituSpider(scrapy.Spider):
    name = 'yeitu'
    allowed_domains = ['yeitu.com']
    # start_urls = ['http://yeitu.com/']
    start_urls = ['https://www.yeitu.com/tag/wangyuchun/']

    def parse(self, response):
       url_list = response.xpath("//div[@id='tag_box']/div/a")
       # print(len(url_list))
       for a in url_list:
           detail_url = a.xpath("./@href").extract_first()
           # print(detail_url)
           yield scrapy.Request(
               detail_url,
               callback=self.detail_parse
           )

    def detail_parse(self, response):
        pass