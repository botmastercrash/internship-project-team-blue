import scrapy
from scrapyProject.items import scrapyProjectItem

class OzoneSpider(scrapy.Spider):
    name = 'ozone'
    allowed_domains = ['ozone.bg']
    start_urls = ['https://www.ozone.bg/gaming/console-and-accessories/']

    def extractInfo(self, response):
        item = scrapyProjectItem()
        item = {
            "name": response.xpath(''' //*[@id="products-list"]/div/a/span[3]/span/text() ''')
        }

        yield item
      
    def parse(self, response):
        i = 2
        yield scrapy.Request("https://www.ozone.bg/gaming/console-and-accessories/?p=" + str(i), callback=self.extractInfo)
        i = i + 1