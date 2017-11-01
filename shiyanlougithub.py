import scrapy


class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou_github_spider'

    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmp.format(i) for i in range(1,5))

    def parse(self,response):
        for course in response.xpath('//div[@class="d-inline-block mb-1"]'):
            yield{
                'name':course.xpath('.//h3/a/text()').re_first('^\s*(.*)'),
                'update_time':course.xpath('..//div[@class="f6 text-gray mt-2"]/relative-time').re_first('<relative-time datetime="(.*)"')
                }


