# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re

#下载美女图片的pipeline
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
        dir_name = request.meta['page_title']
        dir_name = re.sub("[.!/_,$%^*(+\"\']+|[+—！，。？、~@#￥%…&*（）]+", "", dir_name)
        dir_name = dir_name.replace(" ", "_")
        jpg_name = request.meta['img_name']
        jpg_path = dir_name+"/"+jpg_name
        return jpg_path

    def item_completed(self, results, item, info):
        item['img_name'] = [ v['path'] for k,v in results if k ]
        return  item

#下载装修图片的pipeline
class ImgTagDownLoadPipeline(ImagesPipeline):
    # DEFAULT_IMAGES_URLS_FIELD = 'image_urls'
    # DEFAULT_IMAGES_RESULT_FIELD = 'images'

    DEFAULT_IMAGES_URLS_FIELD = 'img_url'
    DEFAULT_IMAGES_RESULT_FIELD = 'img_name'

    def  get_media_requests(self, item, info):
        #单张图片的时候
        return [Request(item.get("img_url"),
                        meta={'tag_title': item['tag_title'],
                              'page_title': item['page_title'],
                              'img_name': item['img_name'], }
                        )]

    def file_path(self, request, response=None, info=None):
        tag_name = request.meta['tag_title']
        dir_name = request.meta['page_title']
        dir_name = tag_name+"/"+dir_name
        dir_name = re.sub("[\s]+", "", dir_name)
        # dir_name = dir_name.replace(" ", "_")
        jpg_name = request.meta['img_name']
        jpg_path = dir_name+"/"+jpg_name
        return jpg_path

    def item_completed(self, results, item, info):
        item['img_name'] = [ v['path'] for k,v in results if k ]
        return  item


class  MmlslImgDownPipeline(ImagesPipeline):
    DEFAULT_IMAGES_URLS_FIELD = 'img_url'
    DEFAULT_IMAGES_RESULT_FIELD = 'img_name'

    def get_media_requests(self, item, info):
        #多张图片的时候
        return [Request(url,
                        meta={'img_title': item["img_title"]}
                        ) for url in item.get("img_url")]

    def file_path(self, request, response=None, info=None):
        dir_name = request.meta['img_title']
        dir_name = re.sub("[.!/_,$%^*(+\"\']+|[+—！，。？:：、~@#￥%…&*（）]+", "", dir_name)
        split_url = str(request.url).split('/')
        file_name = split_url[-1]
        return '%s/%s' % (dir_name, file_name)

    def item_completed(self, results, item, info):
        item['img_name'] = [v['path'] for k, v in results if k ]
        return item