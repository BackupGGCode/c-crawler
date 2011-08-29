# -*- coding: utf-8 -*-
'''
Example of Usage
'''

import common
from ccrawler import CCrawler
from selector import HtmlSelector

import logging
logger = common.logger(name=__name__, filename='ccrawler.log', level=logging.DEBUG)

class DummySpider:
    start_urls = ['http://www.blueidea.com/photo/gallery/']
    #start_urls = ['http://www.baidu.com', 'http://www.google.com', 'http://www.google.hk']
    workers = 100
    timeout = 8

    def parse(self, response):
        hxs = HtmlSelector(response.body)
        '''
        Usage re
        '''
        '''
        itemlist = hxs.re('<td class=\'td10\'>��.*?<\/td>')
        for item in itemlist:
            title = item.re('<a[^>]*[^>]*>(.*)[^<]*<\/a>')[0]
            print title.encode('gbk', 'backslashreplace')
        '''
        '''
        Usage xpath
        '''
        itemlist = hxs.select('//tr[@class!="listTitle"]/td[@nowrap]')
        for item in itemlist:
            title = item.select('a/text()').extract()[0]
            link = item.select('a/@href')
            print dir(link)
            #title.encode('gb2312', 'backslashreplace')

    def process_item(self, item):
        for i in item:
            print i

class a:
    pass


spider = DummySpider()
crawler = CCrawler(spider)
crawler.start()

