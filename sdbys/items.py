# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SdbysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    #姓名
    xueli = scrapy.Field()
    #学历
    zhuanye = scrapy.Field()
    #专业
    school = scrapy.Field()
    #院校
    year = scrapy.Field()
    #毕业年度
    sex = scrapy.Field()
    #姓别
    time = scrapy.Field()
    #发布时间
    guid = scrapy.Field()
    #guid



