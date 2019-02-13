# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleItem(scrapy.Item):
    publish_time = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    origin_link = scrapy.Field()
    origin_author = scrapy.Field()
    title = scrapy.Field()
