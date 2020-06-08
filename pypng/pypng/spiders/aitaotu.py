# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class AitaotuSpider(scrapy.Spider):
    name = 'aitaotu'
    allowed_domains = ['aitaotu.com', 'img.aitaotu.cc']
    start_urls = ['https://www.aitaotu.com/sjbz/']

    # 1、tag标签的地址URL
    def parse(self, response):
        m_list = response.xpath("//div[@class='ai-l-cls']/a")
        for m in m_list:
            item = {}
            item["tag_href"] = m.xpath("./@href").extract_first()
            #大分类的名字    一级目录
            item["tag_title"] = m.xpath("./@title").extract_first()
            # print(item)
            # 记录商品详情页
            yield scrapy.Request(
                "https://www.aitaotu.com" + item["tag_href"],
                callback=self.parse_list,
                meta={"item": deepcopy(item)}
            )

    # 2、作品列表的地址URL
    def parse_list(self, response):
        item = response.meta["item"]
        m_list = response.xpath("//div[@class='item_b clearfix']/div/span/a")
        for m in m_list:
            item["page_href"] = m.xpath("./@href").extract_first()
            # 某作品的名字    二级目录
            item["page_title"] = m.xpath("./text()").extract_first()
            # 记录商品详情页
            yield scrapy.Request(
                "https://www.aitaotu.com" + item["page_href"],
                callback=self.parse_detail,
                meta={"item": deepcopy(item)}
            )
        # 本类下，下一页的图集列表url
        next_page = response.xpath("//div[@id='pageNum']/a[contains(text(),'下一页')]/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(
                "https://www.aitaotu.com"+next_page,
                callback=self.parse_list,
                meta={"item": deepcopy(item)}
            )

    # 3、单作品详情的地址URL
    def parse_detail(self, response):
        item = response.meta["item"]
        # # 详情页是单张时
        # item["img_url"] = response.xpath("//div[@id='big-pic']/p/a/img/@src").extract_first()
        # item["img_name"] = item["img_url"].split("/")[-1]
        # yield item

        # #  详情页是多张时
        a_list = response.xpath("//div[@id='big-pic']/p/a/img/@src").extract()
        for a in a_list:
            item["img_url"] = a
            item["img_name"] = a.split("/")[-1]
            # print(item)
            yield item

        next_page = response.xpath("//div[@class='pages']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(
                "https://www.aitaotu.com" + next_page,
                callback=self.parse_detail,
                meta={"item": deepcopy(item)}
            )

