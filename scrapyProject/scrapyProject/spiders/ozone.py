import scrapy
from scrapyProject.items import ScrapyprojectItem

class OzoneSpider(scrapy.Spider):
    name = 'ozone'
    allowed_domains = ['ozone.bg']
    start_urls = ['https://www.ozone.bg/gaming/console-and-accessories/']

    def extractInfo(self, response):
 #      item = ScrapyprojectItem()
        item = {
            "name": response.xpath(''' //*[@id="products-list"]/div[2]/a/span[3]/span/text() ''').getall()
        }

        yield item
      
    def parse(self, response):
        i = 2
        yield scrapy.Request("https://www.ozone.bg/gaming/console-and-accessories/?p=" + str(i), callback=self.extractInfo)
        i = i + 1