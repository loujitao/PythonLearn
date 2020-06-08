# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class AtuSpider(scrapy.Spider):
    name = 'atu'
    allowed_domains = ['aitaotu.com','img.aitaotu.cc']
    start_urls = ['https://www.aitaotu.com/tag/miaotangyinghua.html']

# def get_tag():
#     # 1、tag标签的地址URL
#     tag_list = response.xpath("//div[@id='sp-nav-newc']/ul/li")
#     for tag in tag_list:
#         item = {}
#         item["tag_href"] = "https://www.aitaotu.com" + tag.xpath("./a[@class='over']/@href").extract_first()
#         item["tag_name"] = tag.xpath("./a[@class='over']/text()").extract_first()

    # 2、某个品牌下，单个图集的URL列表
    def parse(self, response):
            m_list=response.xpath("//div[@id='mainbody']/ul/li")
            for m in m_list:
                item={}
                item["page_href"] = m.xpath("./a[@class='Pli-litpic']/@href").extract_first()
                item["page_title"] = m.xpath("./a[@class='Pli-litpic']/@title").extract_first()
                item["img_url"]=[]
                # print(item)
                # 记录商品详情页
                yield scrapy.Request(
                    "https://www.aitaotu.com" + item["page_href"],
                    callback=self.parse_list,
                    meta={"item": deepcopy(item)}
                )
            # 本类下，下一页的图集列表url
            next_page = response.xpath("//div[@id='pageNum']/span/a[contains(text(),'下一页')]/@href").extract_first()
            if next_page is not None:
                yield scrapy.Request(
                    "https://www.aitaotu.com"+next_page,
                    callback=self.parse
                )

    def parse_list(self, response):
        item=response.meta["item"]
        item["img_url"] = response.xpath("//div[@id='big-pic']/p/a/img/@src").extract_first()
        item["img_name"] = item["img_url"].split("/")[-1]
        yield item

        next_page = response.xpath("//div[@class='pages']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(
                "https://www.aitaotu.com" + next_page,
                callback=self.parse_list,
                meta={"item": deepcopy(item)}
            )



