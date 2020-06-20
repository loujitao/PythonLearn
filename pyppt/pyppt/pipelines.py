# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# class PypptPipeline:
#     def process_item(self, item, spider):
#         print(item)
#         return item

from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
class MyFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):  # 下载图片
        for image_url in item['filepath']:
            yield Request(image_url)

    def file_path(self, request, response=None, info=None):
        split_url = str(request.url).split('/')
        file_name = split_url[-1]
        return file_name
        # return 'full/%s' % file_name