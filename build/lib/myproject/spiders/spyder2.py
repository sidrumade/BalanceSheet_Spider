import scrapy
from myproject.items import MyprojectItem
from scrapy.loader import ItemLoader
import itertools

class MySpyder2(scrapy.Spider):
    name="spidy2"

    custom_settings = {
        'ITEM_PIPELINES': {
            'myproject.pipelines.MyprojectPipeline2': 300
        }
    }

    start_urls=['https://economictimes.indiatimes.com/indices/nifty_50_companies']

    def parse(self,response):
        myselector = response.css("div.dataList a::attr(title)").getall()
        l=ItemLoader(item=MyprojectItem(),selector=response)
        l.add_value('cmp_list',myselector)
        yield l.load_item()



        
            

