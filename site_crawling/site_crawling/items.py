# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ChampionsLeagueItem(scrapy.Item):
    # Định nghĩa các trường dữ liệu bạn cần thu thập
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
