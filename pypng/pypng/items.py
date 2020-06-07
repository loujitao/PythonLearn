# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PypngItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    page_href = scrapy.Field()
    page_title = scrapy.Field()
    imgs = scrapy.Field()
