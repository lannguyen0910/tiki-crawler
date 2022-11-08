<h1 align="center">Tiki Crawler with Scrapy</h1>


## Install dependencies
Please install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) and reate a new working environment before running the below script.
```
pip install -r requirements.txt
cd tiki
```
If you cannot install Scrapy on MacOS, please refer to this [link](https://docs.scrapy.org/en/latest/intro/install.html) for proper guide.


## Run Scrapy crawler
### Crawl by keyword
```python
scrapy crawl <spider_name> -o <output_file_path>.<file_format> \
                            -a keyword=<your_keyword> \
                            -a sort_type=<product_list_sort_type> \
                            -a num_products=<number_of_product_to_crawl>
```
Ex:
```python
scrapy crawl html_crawler -o ./data/data_laptop.json \
                            -a keyword="laptop chơi game" \
                            -a sort_type=default \
                            -a num_products=50
```
### Crawl by category
```python
scrapy crawl <spider_name> -o <output_file_path>.<file_format> \
                            -a category=<category_name> \
                            -a sort_type=<product_list_sort_type> \
                            -a num_products=<number_of_product_to_crawl>
```
Ex:
```python
scrapy crawl html_crawler -o ./data/data_laptop.json \
                            -a keyword="Đồ Chơi - Mẹ & Bé" \
                            -a sort_type=default \
                            -a num_products=50
```
You can refer to ```category_names.txt``` to input category argument correctly. Otherwise the program will return assertion error.

## Additional Information
- Furthermore, you must configure the path of crawled images by changing ```IMAGES_STORE``` variable in ```tiki/tiki/settings.py``` file. The default path is ```tiki/data/imgs```
- If you cannot crawl data, go to http://myhttpheader.com/. Copy your "user-agent" and paste it to ```USER_AGENT``` variable in file ```tiki/tiki/settings.py```.