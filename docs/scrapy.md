Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

Scrapy was originally designed for web scraping, it can also be used to extract data using APIs or as a general purpose web crawler. That's why I exploited Scrapy power by using these two different approaches. After one week, although I didn't use all features supported by Scrapy, I really think Scrapy is very powerful and recommend anyone who wants to build a crawler system to use it.

## Spider
Spiders are classes that you define and that Scrapy uses to scrape information from a website (or a group of websites). Here I write code to make requests and get responses to scrape some data. The output data is normally defined in ```items.py```. 

## Item
The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. Spiders may return the extracted data as items, Python objects that define key-value pairs.

Scrapy supports multiple types of items. You can just define an item by using ```scrapy.Field()```. 

## Item pipeline
After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it through several components that are executed sequentially.

Each item pipeline is a Python class that implements a simple method. They receive an item and perform an action over it, also deciding if the item should continue through the pipeline or be dropped and no longer processed. 

Here I use item pipeline that handles downloaded images' path. Also checking for duplicates (and dropping them).

## References
- https://docs.scrapy.org/en/latest/intro/overview.html
- https://docs.scrapy.org/en/latest/intro/tutorial.html