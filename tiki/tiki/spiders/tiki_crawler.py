import json
import scrapy
from scrapy.exceptions import CloseSpider

from tiki.common import constants
from tiki.items import HTMLCrawlerItem, APICrawlerItem
from tiki.utils.getter import get_category_id, get_product_id, get_variant_infos, get_image_urls, get_image_infos


class TikiCrawlerSpider(scrapy.Spider):
    name = 'tiki_crawler'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handle_cli_arguments()
        self.next_page_number = 2
        self.product_number = 0
        self.product_counter = 0
        self.stop_paging = False

    def start_requests(self):
        if self.category is not None:
            url = constants.TIKI_HOME_URL
            callback = self.parse_category_list

        if self.keyword is not None:
            url = constants.TIKI_SEARCH_URL.format(
                self.keyword,
                self.sort_type
            )
            callback = self.parse_product_lists

        yield scrapy.Request(url, callback=callback)

    def parse_category_list(self, response):
        category_names = response.xpath(constants.CATEGORY_NAME_XPATH).getall()
        category_urls = response.xpath(constants.CATEGORY_URL_XPATH).getall()
        assert self.category in category_names and self.category not in constants.UNSUPPORTED_CATEGORIES, \
            "Invalid input category!"

        for name, url in zip(category_names, category_urls):
            if self.category == name:
                target_url = url
                break

        category_id = get_category_id(target_url)
        url = constants.CATEGORY_API.format(
            category_id,
            self.sort_type,
            self.num_products
        )
        yield scrapy.Request(url=url,
                             callback=self.parse_category_api)

    def parse_category_api(self, response):
        category_data = json.loads(response.text)['data']
        for category in category_data:
            category_id = category['id']
            product_url = constants.PRODUCT_API.format(category_id)
            yield scrapy.Request(url=product_url,
                                 callback=self.parse_product_api)

    def parse_product_lists(self, response):
        if response.status == 404:
            raise CloseSpider('Product pages not found!')

        for product_url in response.xpath(constants.PRODUCT_ITEM_XPATH).getall():
            assert product_url is not None, "Sorry, no products were found to match your selection!"
            if self.product_counter == self.num_products:
                self.stop_paging = True
                break
            self.product_counter += 1

            if self.parser_type == 'html':
                product_html_url = constants.TIKI_HOME_URL + product_url
                yield scrapy.Request(url=product_html_url,
                                     callback=self.parse_product_html)
            else:
                product_id = get_product_id(product_url)
                product_api_url = constants.PRODUCT_API.format(product_id)
                yield scrapy.Request(url=product_api_url,
                                     callback=self.parse_product_api)

        if not self.stop_paging:
            page_url = response.xpath(
                constants.PRODUCT_PAGES_XPATH.format(self.next_page_number)).getall()[0]
            self.next_page_number += 1
            yield scrapy.Request(url=page_url,
                                 callback=self.parse_product_lists)

    def parse_product_api(self, response):
        self.product_number += 1
        product_data = json.loads(response.text)

        id = product_data['id']
        title = product_data['name']
        price = product_data['price']
        url = product_data['short_url']
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
            id=id,
            title=title,
            price=price,
            url=url,
            variants=variant_infos,
            image_urls=image_infos
        )

    def parse_product_html(self, response):
        self.product_number += 1

        url = response.url
        id = get_product_id(url)
        title = response.xpath(constants.PRODUCT_TITLE_XPATH).get()
        current_price = response.xpath(
            constants.PRODUCT_CURRENT_PRICE_XPATH).get()
        original_price = response.xpath(
            constants.PRODUCT_ORIGINAL_PRICE_XPATH).get()
        discount_rate = response.xpath(
            constants.PRODUCT_DISCOUNT_RATE_XPATH).get()
        image_urls = response.xpath(
            constants.PRODUCT_IMAGE_URLS_XPATH).getall()
        description = response.xpath(
            constants.PRODUCT_DESCRIPTION_XPATH).getall()
        detail_info = response.xpath(
            constants.PRODUCT_DETAIL_INFO_XPATH).getall()
        sub_category = response.xpath(
            constants.PRODUCT_SUBCATEGORY_XPATH).getall()

        detail_info = ' - '.join(detail_info)
        sub_category = ' -> '.join(sub_category)
        image_infos = get_image_infos(image_urls)

        yield HTMLCrawlerItem(
            product_number=self.product_number,
            id=id,
            title=title,
            url=url,
            current_price=current_price,
            original_price=original_price,
            discount_rate=discount_rate,
            sub_category=sub_category,
            detail_info=detail_info,
            description=description,
            image_urls=image_infos,
        )

    def handle_cli_arguments(self):
        self.keyword = getattr(self, 'keyword', None)
        self.category = getattr(self, 'category', None)
        self.parser_type = getattr(self, 'parser_type', 'api')
        self.sort_type = getattr(self, 'sort_type', 'popular')
        self.num_products = int(getattr(self, 'num_products', 50))

        assert self.sort_type in ['popular', 'top_seller', 'newest', 'asc', 'desc'], \
            "Invalid product sort type!"
        assert self.parser_type in ['html', 'api'], \
            "Invalid product parser type!"
        assert self.keyword is not None or self.category is not None, \
            "Must input `keyword` argument or `category` argument!"
        assert self.keyword is None or self.category is None, \
            "Cannot input both `keyword` argument and `category` argument!"

        if self.keyword is not None:
            self.keyword = '+'.join(self.keyword.split(' '))
        if self.sort_type == 'desc' or self.sort_type == 'asc':
            self.sort_type = 'price%2C' + self.sort_type
