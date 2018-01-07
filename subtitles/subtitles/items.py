# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubtitlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    lang = scrapy.Field()
    type = scrapy.Field()
    download_number = scrapy.Field()
    download_url = scrapy.Field()
