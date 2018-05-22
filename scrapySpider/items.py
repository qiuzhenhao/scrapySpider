# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    label = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
    level = scrapy.Field()
    student_count = scrapy.Field()
    introduction = scrapy.Field()
    img_arr = scrapy.Field()
    image_paths = scrapy.Field()


