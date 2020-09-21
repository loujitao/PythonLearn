# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy
import requests

class BtjiaSpider(scrapy.Spider):
    name = 'btimg'
    allowed_domains = ['3btjia.com', 'btbttpic.com', '1btjia.com']
    start_urls = ['http://www.3btjia.com/forum-index-fid-8.htm']

    def parse(self, response):
        tag_urllist = response.xpath("//div[@id='threadlist']/table//tr/td/a[2]")
        # print(len(tag_urllist))
        for tag in tag_urllist:
            item = {}
            title = tag.xpath("./text()").extract_first()
            title = re.sub("[.!?/_,:$%^*(+\"\']+|[+—！，。？【】★<>《》：“”、~@#￥%…&*（）]+", "", title)
            item["bt_title"] = title
            detail_url = tag.xpath("./@href").extract_first()
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail,
                meta={"item": deepcopy(item)}
            )
        # 下一页的列表url
        next_page = response.xpath("//div[@class='page']/a[contains(text(),'▶')]/@href").extract_first()
        # print(next_page)
        if next_page is not None:
            yield scrapy.Request(
                next_page,
                callback=self.parse
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item['bt_guo'] = 'imgs'
        item['bt_img'] = []
        img_list = response.xpath("//div[@class='message']/img")
        for img in img_list:
            img_url = img.xpath("./@src").extract_first()
            if img_url.startswith('http'):
                if img_url.startswith('http://'):
                    img_url = re.sub("http://", "https://", img_url)
                item['bt_img'].append(img_url)

        rar = response.xpath("//div[@class='attachlist']/table/tr/td/a[@class='ajaxdialog']/@href").extract_first()
        if rar is not None:
            # print(rar)
            bt_url = re.sub("-ajax-1", "", rar)
            bt_url = re.sub("-dialog-", "-download-", bt_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                'Host': 'www.3btjia.com',
                'Upgrade-Insecure-Requests': '1',
                'Connection': 'keep-alive',
            }
            html = requests.get(bt_url, headers=headers, allow_redirects=False)
            item['bt_url'] = html.headers['Location']
            bt_name = response.xpath("//div[@class='attachlist']/table/tr/td/a[@class='ajaxdialog']/text()").extract_first()
            item['bt_name'] = re.sub("[!?/_,:$%^*(+\"\']+|[+—！，。？：【】★<>《》“”、~@#￥%…&*（）]+", "", bt_name)
        # print(item)
        yield item