# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#  CrawlSpider自动翻页功能
class AitaotuSpider(CrawlSpider):
    name = 'aitaotu'
    allowed_domains = ['aitaotu.com']
    start_urls = ['https://www.aitaotu.com/tag/miaotangyinghua.html']

    rules = (
        #分类 列表页的地址
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='sp-nav-newc']/ul/li/a[@class='over']")), follow=True),
        #单页面的路径  //*[@id="mainbodypul"]/li[1]/a
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainbody']/ul/li/a[@class='Pli-litpic']")), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
