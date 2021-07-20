# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OzoneItem(scrapy.Item):
    is_available = scrapy.Field();
    price = scrapy.Field();
