# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class TikiImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        folder_name = item.get('product_number', 0)
        for image in item.get('image_urls', []):
            yield scrapy.Request(image["image_url"],
                                 meta={'image_name': image["image_name"],
                                       'folder_name': folder_name})

    def file_path(self, request, response=None, info=None, *, item=None):
        return f"{request.meta['folder_name']}/{request.meta['image_name']}"

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")

        adapter = ItemAdapter(item)
        adapter['images'] = image_paths
        del adapter['image_urls']

        return item


class RemoveDuplicatesPipeline:
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['id'])
            return item
