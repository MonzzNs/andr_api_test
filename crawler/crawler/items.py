# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from main.models import Post

class CrawlerItem(DjangoItem):
    django_model = Post()
# class CrawlerItem(scrapy.Item):
#     title = scrapy.Field()
#     cover = scrapy.Field()
#     rating =  scrapy.Field()
#     genres = scrapy.Field()
    # image_urls = scrapy.Field()
