# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst
from w3lib.html import remove_tags



def lower(item):
    return item.lower()
def remove_quotes(item):
    return item.replace("'","")



class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #item_text=scrapy.Field(
    #   input_processor=MapCompose(remove_tags),
    #    output_processor=TakeFirst()
    #)
    cmp_name=scrapy.Field(
        input_processor=MapCompose(remove_quotes,lower)
        #output_processor=TakeFirst()
    )
    tsc=scrapy.Field(
        #input_processor=MapCompose(remove_tags),
        #output_processor=TakeFirst()
    )
    res=scrapy.Field(
        #input_processor=MapCompose(remove_tags),
        #output_processor=TakeFirst()
    )
    net=scrapy.Field(
        #input_processor=MapCompose(remove_tags),
        #output_processor=TakeFirst()
    )
    debt=scrapy.Field(
        #input_processor=MapCompose(remove_tags),
        #output_processor=TakeFirst()
    )
    years=scrapy.Field(
        input_processor=MapCompose(remove_quotes)
        #output_processor=TakeFirst()
    )
    cmp_list=scrapy.Field(
        input_processor=MapCompose(remove_quotes,lower)
        #output_processor=TakeFirst()
    )

