# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class PypngPipeline:

    # def open_spider(self,spider):
    #     self.file=open(spider.settings.get("SAVE_FILE","./data.json"),"w")
    #
    # def close_spider(self,spider):
    #     self.file.close()

    def process_item(self, item, spider):
         print(item)
         return item
