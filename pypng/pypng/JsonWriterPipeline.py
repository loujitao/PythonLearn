# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open(spider.settings.get("SAVE_FILE"), "wb")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
         line = json.dumps(dict(item), ensure_ascii=False)+"\n"

         line = bytes(line, encoding='utf-8')

         self.file.write(line)
         return item
