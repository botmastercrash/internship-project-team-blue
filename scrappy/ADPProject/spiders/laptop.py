from sys import is_finalizing
import scrapy
import logging
from ADPProject.items import OzoneItem

class OzoneSpider(scrapy.Spider):
    name = 'ozone'
    allowed_domains = ['ozone.bg']
    start_urls = ['https://www.ozone.bg/gaming/console-and-accessories/']

    def extractInfo(self, response):
        item = OzoneItem()
        item = {
        "is_available": (response.xpath('''//*[@id="products-list"]/div[2]/a/span[3]/span/text()''').get().find("PlayStation 4") != -1),
        "price": response.xpath('''//*[@class="regular-price"]/span/text()[1]''').getall()
        }
      
    def parse(self, response):
        i = 2
        yield scrapy.Request("https://www.ozone.bg/gaming/console-and-accessories/?p=" + str(i), callback=self.extractInfo)
        i = i + 1
