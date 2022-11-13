# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HTMLCrawlerItem(scrapy.Item):
    product_number = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    current_price = scrapy.Field()
    original_price = scrapy.Field()
    discount_rate = scrapy.Field()
    sub_category = scrapy.Field()
    detail_info = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class APICrawlerItem(scrapy.Item):
    product_number = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    variants = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
