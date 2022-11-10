PRODUCT_ITEM_XPATH = \
    "//*[@class = 'product-item' and not (@rel='nofollow')]/@href"
# PRODUCT_PAGES_XPATH = \
#     "//*[@data-view-label='{}']/@href"
PRODUCT_PAGES_XPATH = \
    "//*[@data-view-id='product_list_pagination_item'" \
    "and not (@class='hidden-page') and not (@class='disabled')]/@href"
CATEGORY_NAME_XPATH = \
    "//*[@class='styles__FooterSubheading-sc-32ws10-5 cNJLWI']/a/text()"
CATEGORY_URL_XPATH = \
    "//*[@class='styles__FooterSubheading-sc-32ws10-5 cNJLWI']/a/@href"
PRODUCT_TITLE_XPATH = \
    "//*[@class='header']//*[@class='title']/text()"
PRODUCT_CURRENT_PRICE_XPATH = \
    "//*[@class='product-price__current-price']/text()"
PRODUCT_ORIGINAL_PRICE_XPATH = \
    "//*[@class='product-price__list-price']/text()"
PRODUCT_DISCOUNT_RATE_XPATH = \
    "//*[@class='product-price__discount-rate']/text()"
PRODUCT_IMAGE_URLS_XPATH = \
    "//*[@data-view-id='pdp_main_view_photo']//*/img/@src"
PRODUCT_COMMENTS_XPATH = \
    "//*[@class='review-comment__content']/text()"
PRODUCT_DETAIL_INFO_XPATH = \
    "//*[@class='content has-table']/table/tbody/tr/td/text()"
PRODUCT_SUBCATEGORY_XPATH = \
    "//*[@class='breadcrumb']/a/span/text()"
PRODUCT_DESCRIPTION_XPATH = \
    "//*[@class='content']/div/div/p/text()"
PRODUCT_OPTION_XPATH = \
    "//*[@class='left']//*[@data-view-id='pdp_main_select_configuration_item']"

PRODUCT_DETAIL_API = "https://api.tiki.vn/product-detail/api/v2/products/170098844"
PRODUCT_SEARCH_API = "https://tiki.vn/api/v2/products?limit={}&q={}"
CATEGORY_API = "https://api.tiki.vn/v2/categories/1815"
DIGITAL_DEVICE_API = "https://tiki.vn/api/v2/products?category=8215&urlKey=thiet-bi-am-thanh-va-phu-kien/"

PRODUCT_API = "https://tiki.vn/api/v2/products/{}"

TIKI_HOME_URL = \
    "https://tiki.vn"
TIKI_SEARCH_URL = \
    "https://tiki.vn/search?q={}&sort={}"

UNSUPPORTED_CATEGORIES = ["Thực Phẩm Tươi Sống"]
