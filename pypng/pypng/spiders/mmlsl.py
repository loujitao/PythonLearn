# -*- coding: utf-8 -*-
import scrapy


class MmlslSpider(scrapy.Spider):
    name = 'mmlsl'
    allowed_domains = ['mmlsl.com', 'pic.mmlsl.com']
    start_urls = ['https://www.mmlsl.com/']

    def parse(self, response):
       a_list = response.xpath("//div[@id='masonry']/div/div/a")
       for a in a_list:
           detail_url = a.xpath("./@href").extract_first()
           yield scrapy.Request(
               detail_url,
               callback=self.parse_detail
           )

       next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
       if next_page is not None:
           yield scrapy.Request(
               next_page,
               callback=self.parse
           )

    def parse_detail(self, response):
        img_list = response.xpath("//div[@id='masonry']/div/img")
        item = {}
        item['img_url'] = []
        for img in img_list:
            url = img.xpath("./@data-original").extract_first()
            item['img_url'].append(url)

        title = response.xpath("//head/title/text()").extract_first()
        item['img_title'] = str(title).split(" ")[0]
        # print(item)
        yield item