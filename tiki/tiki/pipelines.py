# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class TikiImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image in item['image_urls']:
            yield scrapy.Request(image["image_url"], meta={'image_name': image["image_name"],
                                                           'folder_name': image["folder_name"]})

    def file_path(self, request, response=None, info=None):
        return f"{request.meta['folder_name']}/{request.meta['image_name']}"
