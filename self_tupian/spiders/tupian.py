# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# scrapy crawl tupian
from self_tupian.items import SelfTupianItem

class TupianSpider(CrawlSpider):
    name = 'tupian'
    allowed_domains = ['90tu.com']
    start_urls = ['https://www.90tu.com/xingganmeinv/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.90tu.com/xingganmeinv/\d+_?\d.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        num1 = response.css('#nums i::text').get()
        num2 = response.css('#nums b::text').get().replace('/','_')
        num = num1 + num2
        name = response.css('.content h1::text').get() + '-' + num
        url  = response.css('.spanlr p a img::attr(src)').get()
        item = SelfTupianItem(images=f'{name}',image_urls=url)
        yield item