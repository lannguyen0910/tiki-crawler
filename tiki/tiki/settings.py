# Scrapy settings for tiki project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tiki'

SPIDER_MODULES = ['tiki.spiders']
NEWSPIDER_MODULE = 'tiki.spiders'


# Crawl responsibly by identifying yourself on the user-agent
USER_AGENT = "Chrome/107.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Stored text file under utf-8 format
FEED_EXPORT_ENCODING = 'utf-8'

# Amount of spaces used to indent the output on each level
# Set to 0 for compact representation and faster export
FEED_EXPORT_INDENT = 0

# Image stored path
IMAGES_STORE = './data/imgs'

# Only log informational messages
LOG_LEVEL = 'INFO'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tiki.pipelines.TikiImagesPipeline': 1,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
