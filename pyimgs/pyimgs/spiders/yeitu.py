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
       next_list = response.xpath("//div[@id='pages']/span/following-sibling::a[text()!='下一页']/@href").extract_first()
       if next_list is not None:
           yield scrapy.Request(
               next_list,
               callback=self.parse
           )

    def detail_parse(self, response):
        item = {}
        item['title'] = response.xpath("//div[@id='title']/h1/text()").extract_first()
        item['url'] = response.xpath("//div[@class='img_box']/a/img/@href").extract_first()
        next_page = response.xpath("//div[@id='pages']/span/following-sibling::a/text()").extract_first()
        if next_page == '下一页':
            item['url'] = response.xpath("//div[@class='img_box']/img/@href").extract_first()
        next_url = response.xpath("//div[@id='pages']/span/following-sibling::a[text()!='下一页']/@href").extract_first()
