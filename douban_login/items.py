# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanLoginItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 节目形式
    program_form = scrapy.Field()
    # 短评链接
    shortComment_link = scrapy.Field()
    # 影评链接
    filmReview_link = scrapy.Field()
    # 图片链接
    image_link = scrapy.Field()
    # 电影人员链接
    movieStaff_link = scrapy.Field()
    # 豆瓣评分
    movie_rating = scrapy.Field()
    # 评分人数
    movie_NumRatingPeople = scrapy.Field()
    # 链接地址
    movie_linkAddress = scrapy.Field()
    # 电影导演
    movie_director = scrapy.Field()
    # 电影编剧
    movie_screenwriter = scrapy.Field()
    # 电影主演
    movie_starring = scrapy.Field()
    # 电影类型
    movie_type = scrapy.Field()
    # 制片国家/地区
    movie_productionCountry = scrapy.Field()

