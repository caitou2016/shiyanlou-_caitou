# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class RespositoriesSpider(scrapy.Spider):
    name = 'respositories'
#    allowed_domains = ['github.com']
 #   start_urls = ['http://github.com/']

#    def parse(self, response):
#        pass

    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmp.format(i) for i in range(1,5))
    def parse(self,response):
        for course in response.xpath('//div[@class="d-inline-block mb-1"]'):
            yield ShiyanlougithubItem({
                'name':course.xpath('.//h3/a/text()').re_first('^\s*(.*)'),
                'update_time':course.xpath('..//div[@class="f6 text-gray mt-2"]/relative-time').re_first('<relative-time datetime="(.*)"')
            
                })
