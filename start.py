'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/6/8 15:10
@Software: PyCharm
@File    : start.py
'''
from scrapy import cmdline
cmdline.execute("scrapy crawl douban".split())