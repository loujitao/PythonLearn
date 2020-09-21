# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class MyFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):  # 下载BT文件
        if not('bt_url' in item):
            return
        return [Request(item.get("bt_url"),
                        meta={'bt_guo': item['bt_guo'],
                              'bt_title': item['bt_title'],
                              'bt_name': item['bt_name'], }
                        )]

    def file_path(self, request, response=None, info=None):
        bt_guo = request.meta['bt_guo']
        bt_title = request.meta['bt_title']
        bt_name = request.meta['bt_name']
        dir_name = bt_guo+"/"+bt_title+"/"+bt_name
        return dir_name

class MyImgPipeline(FilesPipeline):
    def get_media_requests(self, item, info):  # 下载图片
        for image_url in item['bt_img']:
            yield Request(image_url,
                          meta={'bt_guo': item['bt_guo'],
                                'bt_title': item['bt_title'],})

    def file_path(self, request, response=None, info=None):
        bt_guo = request.meta['bt_guo']
        bt_title = request.meta['bt_title']
        kind_name = bt_guo + "/" + bt_title
        split_url = str(request.url).split('/')
        file_name = split_url[-1]
        return '%s/%s' % (kind_name, file_name)