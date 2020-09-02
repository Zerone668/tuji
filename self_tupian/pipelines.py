# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy import Request

class SelfTupianPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        yield Request(item['image_urls'],meta={'item': item['images']})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item
        path = item.split('-')
        pa1 = path[0]
        pa2 = path[1]
        print(pa1)
        print(pa2)
        if os.path.exists(pa1):
            os.mkdir(pa1)
        filename = f'{pa1}/{pa2}.jpg'
        return filename