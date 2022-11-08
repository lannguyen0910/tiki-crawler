import scrapy
import os
from ..constants import *
from ..items import HTMLCrawlerItem


class TikiCrawlingSpider(scrapy.Spider):
    name = 'html_crawler'
    start_urls = ['https://www.tiki.vn']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_number = 0
        (self.sort_type, self.num_products) = self.handle_cli_arguments()

    def start_requests(self):
        url = "https://tiki.vn"
        callback = self.parse_category_list

        if self.keyword is not None:
            url = "https://tiki.vn/search?q={}&sort={}&limit={}".format(
                self.keyword, self.sort_type, self.num_products)
            callback = self.parse_product_list

        yield scrapy.Request(url, callback=callback)

    def parse_product_list(self, response):
        for i in range(self.num_products):
            product = response.xpath(PRODUCT_ITEM_XPATH.format(i+1))
            product_url = "https://tiki.vn" + product.attrib['href']
            if isinstance(product_url, str):
                yield scrapy.Request(url=product_url,
                                     callback=self.parse_product)

    def parse_category_list(self, response):
        category_names = response.xpath(CATEGORY_NAME_XPATH).getall()
        category_urls = response.xpath(CATEGORY_URL_XPATH).getall()
        assert self.category in category_names, "Invalid input category!"

        for name, url in zip(category_names, category_urls):
            if self.category == name:
                target_url = url
                break

        yield scrapy.Request(url=target_url, callback=self.parse_product_list)

    def parse_product(self, response):
        self.product_number += 1

        title = response.xpath(PRODUCT_TITLE_XPATH).get()
        current_price = response.xpath(PRODUCT_CURRENT_PRICE_XPATH).get()
        original_price = response.xpath(PRODUCT_ORIGINAL_PRICE_XPATH).get()
        discount_rate = response.xpath(PRODUCT_DISCOUNT_RATE_XPATH).get()
        image_urls = response.xpath(PRODUCT_IMAGE_URLS_XPATH).getall()
        comments = response.xpath(PRODUCT_COMMENTS_XPATH).getall()
        description = response.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
        detail_info = ' - '.join(
            response.xpath(PRODUCT_DETAIL_INFO_XPATH).getall())
        sub_category = ' -> '.join(
            response.xpath(PRODUCT_SUBCATEGORY_XPATH).getall())

        images = []
        for url in image_urls:
            filename = os.path.basename(url)
            images.append(
                {'image_url': url,
                 'image_name': filename,
                 'folder_name': self.product_number})

        yield HTMLCrawlerItem(
            product_number=self.product_number,
            title=title,
            url=response.url,
            current_price=current_price,
            original_price=original_price,
            discount_rate=discount_rate,
            sub_category=sub_category,
            detail_info=detail_info,
            description=description,
            comments=comments,
            image_urls=images,
        )

    def handle_cli_arguments(self):
        self.keyword = getattr(self, 'keyword', None)
        self.category = getattr(self, 'category', None)
        sort_type = getattr(self, 'sort_type', None)
        num_products = int(getattr(self, 'num_products', None))

        assert sort_type in [None, 'default', 'top_seller',
                             'newest', 'asc', 'desc'], \
            "Invalid product sort type!"
        assert self.keyword is not None or self.category is not None, \
            "Must input `keyword` argument or `category` argument!"
        assert self.keyword is None or self.category is None, \
            "Cannot input both `keyword` argument and `category` argument!"

        if self.keyword is not None:
            self.keyword = '+'.join(self.keyword.split(' '))
        if num_products is None:
            num_products = 50
        if sort_type is None:
            sort_type = 'default'
        elif sort_type == 'desc' or sort_type == 'asc':
            sort_type = 'price%2C' + sort_type

        return (sort_type, num_products)
