# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import scrapy

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FileException
from scrapy.pipelines.images import ImagesPipeline


class TikiImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        folder_name = item.get('product_number', 0)
        for image in item.get('image_urls', []):
            yield scrapy.Request(image["image_url"],
                                 meta={'image_name': image["image_name"],
                                       'folder_name': folder_name})

    def file_path(self, request, response=None, info=None):
        return f"{request.meta['folder_name']}/{request.meta['image_name']}"
