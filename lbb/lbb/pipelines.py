# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class LbbPipeline:
    def open_spider(self, spider):
        self.file = open("/home/bladestone/lbb.csv", "wb")
        self.exporter = CsvItemExporter(self.file,
        fields_to_export=["schoolName", "currentBatch", "totalNumberInPlan"])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

# pip install OpenPyxl  -i https://pypi.tuna.tsinghua.edu.cn/simple
from openpyxl import Workbook
class LbbExcelPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['新闻标题', '新闻链接', '来源网站', '发布时间', '相似新闻', '是否含有网站名'])

    def process_item(self, item, spider):  # 工序具体内容
        line = [item['title'], item['link'], item['source'], item['pub_date'], item['similar'],
                item['in_title']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('F:/pyData/lbb/tuniu.xlsx')  # 保存xlsx文件
        return item

    # def close_spider(self, spider):
    #     self.wb.save('/home/alexkh/tuniu.xlsx')