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
            item = ShiyanlougithubItem()
           # yield ShiyanlougithubItem({
            item['name'] = course.xpath('.//h3/a/text()').re_first('^\s*(.*)')
            item['update_time'] = course.xpath('..//div[@class="f6 text-gray mt-2"]/relative-time').re_first('<relative-time datetime="(.*)"')
            
           #     })
            reo_url = response.urljoin(course.xpath('.//h3/a/@href').extract_first())
            request = scrapy.Request(reo_url,callback=self.parse_cbr)
            request.meta['item'] = item
            yield request

    def parse_cbr(self,response):
        item = response.meta['item']
        results = response.xpath('//ul[@class="numbers-summary"]/li/a/span/text()').re('\n\s*(.*)\n\s*')
       # commits_list = []
       # branches_list = []
       # releases_list = []
       # item['commits'] = commits_list.append(results[0].replace(',',''))
       # item['branches'] = branches_list.append(results[1].replace(',',''))
       # item['releases'] = releases_list.append(results[2].replace(',',''))
        item['commits'] = results[0].replace(',','')
        item['branches'] = results[1].replace(',','')
        item['releases'] = results[2].replace(',','')
        yield item
