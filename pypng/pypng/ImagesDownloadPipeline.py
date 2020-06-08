# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class ImagesDownLoadPipeline(ImagesPipeline):
    # DEFAULT_IMAGES_URLS_FIELD = 'image_urls'
    # DEFAULT_IMAGES_RESULT_FIELD = 'images'

    DEFAULT_IMAGES_URLS_FIELD = 'img_url'
    DEFAULT_IMAGES_RESULT_FIELD = 'img_name'

    def  get_media_requests(self, item, info):
        #单张图片的时候
        return [Request(item.get("img_url"),
                        meta={'page_title': item['page_title'],
                              'img_name': item['img_name'] }
                        )]
       # #多张图片的时候
       #  return [Request(url,
       #                  meta={'img_name': name}
       #                  ) for url, name in item.get("img_urls")
       #          ]

    def file_path(self, request, response=None, info=None):
        dir_name=request.meta['page_title']
        jpg_name=request.meta['img_name']
        jpg_path=dir_name+"/"+jpg_name
        return jpg_path

    def item_completed(self, results, item, info):
        item['img_name'] = [ v['path'] for k,v in results if k ]
        return  item