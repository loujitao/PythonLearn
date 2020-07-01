# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LbbItem(scrapy.Item):
    schoolName = scrapy.Field()
    currentBatch = scrapy.Field()
    totalNumberInPlan = scrapy.Field()
    majorName = scrapy.Field()
    categoryName = scrapy.Field()
    numberInPlan = scrapy.Field()
    note = scrapy.Field()
