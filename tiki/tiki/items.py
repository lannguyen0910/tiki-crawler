# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HTMLCrawlerItem(scrapy.Item):
    product_number = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    current_price = scrapy.Field()
    original_price = scrapy.Field()
    discount_rate = scrapy.Field()
    sub_category = scrapy.Field()
    detail_info = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    comments = scrapy.Field()
