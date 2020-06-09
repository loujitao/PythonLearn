# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import re

class YppptSpider(scrapy.Spider):
    name = 'ypppt'
    allowed_domains = ['ypppt.com', 'youpinppt.com', 'pan.baidu.com']
    start_urls = ['http://www.ypppt.com/moban/']

    def parse(self, response):
        tag_urllist = response.xpath("//div[@class='wrapper']/ul/li/a[@class='p-title']")
        for tag in tag_urllist:
            item = {}
            dir_name = tag.xpath("./text()").extract_first()
            item["file_title"] = re.sub("[\s,.:]+", "", dir_name)
            next_url = "http://www.ypppt.com/" + tag.xpath("./@href").extract_first()
            yield scrapy.Request(
                next_url,
                callback=self.down_page,
                meta={"item": deepcopy(item)}
            )

        # 本类下，下一页的图集列表url
        next_page = response.xpath("//div[@class='page-navi']/a[contains(text(),'下一页')]/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(
                "http://www.ypppt.com/moban/" + next_page,
                callback=self.parse
            )

    def down_page(self, response):
        item = response.meta["item"]
        next_url = "http://www.ypppt.com" + response.xpath("//div[@class='infoss']/div/a[@class='down-button']/@href").extract_first()
        yield scrapy.Request(
            next_url,
            callback=self.file_url,
            meta={"item": deepcopy(item)}
        )

    def file_url(self, response):
        item = response.meta["item"]
        item["file_urls"] = []
        file_url = response.xpath("//ul[@class='down clear']/li/a/@href").extract_first()
        if file_url.startswith('http'):
            pass
        else:
            file_url = "http://www.ypppt.com" + file_url
        item["file_urls"].append(file_url)
        # print(item)
        yield item