import scrapy
import json

from tiki.items import HTMLCrawlerItem, APICrawlerItem
from tiki.common.utils import *
from tiki.common.constants import *


class TikiCrawlerSpider(scrapy.Spider):
    name = 'tiki_crawler'
    start_urls = ['https://www.tiki.vn']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handle_cli_arguments()
        self.current_page = 1
        self.product_number = 0
        self.product_counter = 0
        self.stop_paging = False

    def start_requests(self):
        if self.category is not None:
            url = TIKI_HOME_URL
            callback = self.parse_category_list

        if self.keyword is not None:
            url = TIKI_SEARCH_URL.format(
                self.keyword,
                self.sort_type
            )
            callback = self.get_product_pages

        yield scrapy.Request(url, callback=callback)

    def parse_category_list(self, response):
        category_names = response.xpath(CATEGORY_NAME_XPATH).getall()
        category_urls = response.xpath(CATEGORY_URL_XPATH).getall()
        assert self.category in category_names \
            and self.category not in UNSUPPORTED_CATEGORIES, \
            "Invalid input category!"

        for name, url in zip(category_names, category_urls):
            if self.category == name:
                target_url = url
                break

        # This param helps enabling pagination in Tiki categories
        target_url += f'?sort={self.sort_type}'

        yield scrapy.Request(url=target_url, callback=self.get_product_pages)

    def get_product_pages(self, response):
        if not self.stop_paging:
            for page_url in response.xpath(PRODUCT_PAGES_XPATH).getall():
                yield scrapy.Request(url=page_url,
                                     callback=self.parse_product_lists)

    def parse_product_lists(self, response):
        for product_url in response.xpath(PRODUCT_ITEM_XPATH).getall():
            if self.product_counter == self.num_products:
                self.stop_paging = True
                break
            self.product_counter += 1

            if self.parser_type == 'html':
                product_html_url = TIKI_HOME_URL + product_url
                yield scrapy.Request(url=product_html_url,
                                     callback=self.parse_product_html)
            else:
                product_id = get_product_id(product_url)
                product_api_url = PRODUCT_API.format(product_id)

                yield scrapy.Request(url=product_api_url,
                                     callback=self.parse_product_api)

    def parse_product_api(self, response):
        self.product_number += 1
        product_data = json.loads(response.text)

        title = product_data['name']
        price = product_data['price']
        url = product_data['short_url']
        description = product_data['short_description']
        thumbnail_url = product_data['thumbnail_url']

        total_image_urls = []
        total_image_urls.append(thumbnail_url)

        if product_data['images'] is not None:
            image_urls = get_image_urls(
                product_data['images'])
            total_image_urls += image_urls

        if 'configurable_products' in product_data:
            variant_infos = get_variant_infos(
                product_data['configurable_products'])
            for variant_info in variant_infos:
                total_image_urls.append(variant_info['variant_url'])

                # Remove this key for cleaner output
                del variant_info['variant_url']
        else:
            variant_infos = None

        image_infos = get_image_infos(total_image_urls)

        yield APICrawlerItem(
            product_number=self.product_number,
            title=title,
            price=price,
            url=url,
            description=description,
            variants=variant_infos,
            image_urls=image_infos
        )

    def parse_product_html(self, response):
        self.product_number += 1

        title = response.xpath(PRODUCT_TITLE_XPATH).get()
        current_price = response.xpath(PRODUCT_CURRENT_PRICE_XPATH).get()
        original_price = response.xpath(PRODUCT_ORIGINAL_PRICE_XPATH).get()
        discount_rate = response.xpath(PRODUCT_DISCOUNT_RATE_XPATH).get()
        image_urls = response.xpath(PRODUCT_IMAGE_URLS_XPATH).getall()
        comments = response.xpath(PRODUCT_COMMENTS_XPATH).getall()
        description = response.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
        detail_info = response.xpath(PRODUCT_DETAIL_INFO_XPATH).getall()
        sub_category = response.xpath(PRODUCT_SUBCATEGORY_XPATH).getall()

        detail_info = ' - '.join(detail_info)
        sub_category = ' -> '.join(sub_category)
        image_infos = get_image_infos(image_urls)

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
            image_urls=image_infos,
        )

    def handle_cli_arguments(self):
        self.keyword = getattr(self, 'keyword', None)
        self.category = getattr(self, 'category', None)
        self.parser_type = getattr(self, 'parser_type', 'api')
        self.sort_type = getattr(self, 'sort_type', 'popular')
        self.num_products = int(getattr(self, 'num_products', 50))

        assert self.sort_type in ['popular', 'top_seller',
                                  'newest', 'asc', 'desc'], \
            "Invalid product sort type!"
        assert self.parser_type in ['html', 'api'], \
            "Invalid product parser type"
        assert self.keyword is not None or self.category is not None, \
            "Must input `keyword` argument or `category` argument!"
        assert self.keyword is None or self.category is None, \
            "Cannot input both `keyword` argument and `category` argument!"

        if self.keyword is not None:
            self.keyword = '+'.join(self.keyword.split(' '))
        if self.sort_type == 'desc' or self.sort_type == 'asc':
            self.sort_type = 'price%2C' + self.sort_type
