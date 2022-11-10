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


class APICrawlerItem(scrapy.Item):
    product_number = scrapy.Field()
    title = scrapy.Field()  # name
    url = scrapy.Field()    # short_url
    description = scrapy.Field()  # short_description
    price = scrapy.Field()  # price
    variants = scrapy.Field()  # configurable_products: list of dicts
    image_urls = scrapy.Field()
