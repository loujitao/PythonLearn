# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class LbbPipeline:
    def open_spider(self, spider):
        self.file = open("/home/bladestone/enrolldata.csv", "wb")
        self.exporter = CsvItemExporter(self.file,
        fields_to_export=["schoolName", "currentBatch", "totalNumberInPlan"])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
