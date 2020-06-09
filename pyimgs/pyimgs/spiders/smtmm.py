# -*- coding: utf-8 -*-
import scrapy
import time
from copy import deepcopy

# https://www.95mm.net

class MeituSpider(scrapy.Spider):
    name = 'smtmm'
    allowed_domains = ['smtmm.win']
    start_urls = ['https://smtmm.win/']
    # https://smtmm.win/type/{1-6}/?page={1-?}

    #1、获取所有标题页URL
    def parse(self, response):
        tag_urllist = response.xpath("//div[@class='sitenav']/ul/li/a")
        for tag in tag_urllist:
            item = {}
            item["tag_title"] = tag.xpath("./text()").extract_first()
            item["tag_url"] = "https://smtmm.win"+tag.xpath("./@href").extract_first()
            # print(list_url )
            yield scrapy.Request(
                item["tag_url"],
                callback=self.parse_list,
                meta={"item": deepcopy(item)}
            )

    #2、获取单分类下所有URL列表
    def parse_list(self, response):
        item = response.meta["item"]        #/html/body/section/div[1]/div/article[1]/h2/a[2]
        imgs_list = response.xpath("//div[@class='excerpts']/article/a[@class='thumbnail']")
        # print(len(imgs_list))
        for imgs in imgs_list:
            # 上面定位不到h2标签，很奇怪？所以这里无法获取套图的名称
            # item["img_title"] = imgs.xpath("./text()").extract_first()
            detail_url= imgs.xpath("./@href").extract_first()
            item["imglist_url"] = "https://smtmm.win"+detail_url
            # print(item)
            yield scrapy.Request(
                item["imglist_url"],
                callback=self.parse_detail,
                meta={"item": deepcopy(item)}
            )

        # 本类下，下一页的图集列表url
        next_page = response.xpath("//div[@class='pagination pagination-multi']/ul/li[@class='next-page']/a/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(
                 item["tag_url"]+next_page,
                callback=self.parse_list,
                meta={"item": deepcopy(item)}
            )

    # 3、获取单分类下所有img
    def parse_detail(self, response):
        item = response.meta["item"]
        item["img_title"] = response.xpath("//div[@class='container']/h1/text()").extract_first()
        imgs_list = response.xpath("//article[@class='article-content']/p/img")
        item["img_url"]=[]
        for imgs in imgs_list:
            img_url = "https://smtmm.win"+imgs.xpath("./@data-original").extract_first()
            item["img_url"].append(img_url)
            print(item)
            # yield  item