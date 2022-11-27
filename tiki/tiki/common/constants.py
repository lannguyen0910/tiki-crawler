PRODUCT_ITEM_XPATH = "//*[@class = 'product-item' and not (@rel='nofollow')]/@href"
PRODUCT_PAGES_XPATH = "//*[@data-view-label='{}' and not (@class='hidden-page') and not (@class='disabled')]/@href"
CATEGORY_NAME_XPATH = "//*[@class='styles__FooterSubheading-sc-32ws10-5 cNJLWI']/a/text()"
CATEGORY_URL_XPATH = "//*[@class='styles__FooterSubheading-sc-32ws10-5 cNJLWI']/a/@href"
PRODUCT_TITLE_XPATH = "//*[@class='header']//*[@class='title']/text()"
PRODUCT_CURRENT_PRICE_XPATH = "//*[@class='product-price__current-price']/text()"
PRODUCT_ORIGINAL_PRICE_XPATH = "//*[@class='product-price__list-price']/text()"
PRODUCT_DISCOUNT_RATE_XPATH = "//*[@class='product-price__discount-rate']/text()"
PRODUCT_IMAGE_URLS_XPATH = "//*[@data-view-id='pdp_main_view_photo']//*/img/@src"
PRODUCT_DETAIL_INFO_XPATH = "//*[@class='content has-table']/table/tbody/tr/td/text()"
PRODUCT_SUBCATEGORY_XPATH = "//*[@class='breadcrumb']/a/span/text()"
PRODUCT_DESCRIPTION_XPATH = "//*[@class='content']/div/div/p/text()"
PRODUCT_OPTION_XPATH = "//*[@class='left']//*[@data-view-id='pdp_main_select_configuration_item']"
TIKI_HOME_URL = "https://tiki.vn"
TIKI_SEARCH_URL = "https://tiki.vn/search?q={}&sort={}"
UNSUPPORTED_CATEGORIES = ["Thực Phẩm Tươi Sống"]
CATEGORY_API = "https://tiki.vn/api/v2/products?category={}&sort={}&limit={}"
PRODUCT_API = "https://tiki.vn/api/v2/products/{}"

NEW_CATEGORY_NAME_XPATH = "//*[@class='styles__StyledCategory-sc-17y817k-1 iBByno']/p/a/text()"
NEW_CATEGORY_URL_XPATH = "//*[@class='styles__StyledCategory-sc-17y817k-1 iBByno']/p/a/@href"
UNSUPPORTED_SUBCATEGORIES = ["Trái Cây",
                             "Thịt, Trứng",
                             "Cá, thuỷ hải sản",
                             "Rau củ quả",
                             "Thực phẩm Việt",
                             "Sữa, bơ, phô mai",
                             "Đông lạnh, mát",
                             "Dầu ăn, gia vị",
                             "Gạo, mì, nông sản",
                             "Đồ hộp, đóng gói",
                             "Bia, đồ uống",
                             "Thực phẩm chay",
                             "Dành cho trẻ em",
                             "Bánh kẹo, giỏ quà",
                             "Thức ăn, đồ thú cưng",
                             "Chăm sóc cá nhân",
                             "Chăm sóc nhà cửa"]
