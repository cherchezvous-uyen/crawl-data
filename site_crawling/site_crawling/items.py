# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class VnexpressSpider(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    category= scrapy.Field()
    comments= scrapy.Field()
