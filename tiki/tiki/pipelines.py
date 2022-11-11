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

    def media_downloaded(self, response, request, info):
        try:
            return super(TikiImagesPipeline, self).media_downloaded(response, request, info)
        except FileException as e:
            print(e)


class DuplicatesPipeline:
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['id'])
            return item


class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open('items.jsonl', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
