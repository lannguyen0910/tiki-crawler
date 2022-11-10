<h1 align="center">Tiki Crawler with Scrapy</h1>


## Install dependencies
```
pip install -r requirements.txt
cd tiki
```
If you cannot install Scrapy on MacOS, please refer to this [link](https://docs.scrapy.org/en/latest/intro/install.html) for proper guide.


## Run Scrapy crawler
### Crawl by keyword
```python
scrapy crawl <spider_name> -o <output_file_path>.<file_format> \
                            -s IMAGES_STORE=<image_saved_path> \
                            -s FEED_EXPORT_INDENT=<indentation_for_json> \
                            -s USER_AGENT=<user_agent> \
                            -a keyword=<your_keyword> \
                            -a sort_type=<product_list_sort_type> \
                            -a num_products=<number_of_product_to_crawl>
```
Ex:
```python
scrapy crawl tiki_crawler -o ./data/data.json -s IMAGES_STORE=./data/images -a keyword="laptop chơi game" -a sort_type=top_seller -a num_products=80
```
### Crawl by category
```python
scrapy crawl <spider_name> -o <output_file_path>.<file_format> \
                            -s IMAGES_STORE=<image_saved_path> \
                            -s FEED_EXPORT_INDENT=<indentation_for_json> \
                            -s USER_AGENT=<user_agent> \
                            -a category=<category_name> \
                            -a sort_type=<product_list_sort_type> \
                            -a num_products=<number_of_product_to_crawl>
```
Ex:
```python
scrapy crawl tiki_crawler -o ./data/data.json -s IMAGES_STORE=./data/images -a category="Đồ Chơi - Mẹ & Bé" -a sort_type=top_seller -a num_products=80
```
Note: The program only supports categories from ```examples/category_names.txt```.

## Additional Information
- If you cannot crawl data, go to http://myhttpheader.com/. Copy your "user-agent" and paste it to ```USER_AGENT``` variable in file ```tiki/tiki/settings.py```.