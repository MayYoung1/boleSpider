# -*- coding: utf-8 -*-
import re
import scrapy
from jobbole.items import JobboleItem

class JobboleSpiderSpider(scrapy.Spider):
    name = 'jobbole_spider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        post_urls = response.xpath('//a[@class="archive-title"]/@href').getall()
        for post_url in post_urls:
            # print(post_url)
            yield scrapy.Request(url=post_url, callback=self.jobbole_parse)
        next_urls = response.css('.next.page-numbers::attr(href)').extract_first('')
        if next_urls:
            yield scrapy.Request(url=next_urls, callback=self.parse)

    def jobbole_parse(self, response):
        date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').getall()[0].strip()
        publish_time = re.sub('·', '', date)
        category = ''.join(response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').getall()[0])
        origin_link = response.xpath('//div[@class="copyright-area"]/a/@href').get()
        origin_author = response.xpath('//div[@class="copyright-area"]/a/text()').get()
        content = response.xpath('////div[@class="entry"]').getall()
        title = response.xpath('//div[@class="entry-header"]/h1/text()').get()
        item = JobboleItem(publish_time=publish_time, category=category, origin_link=origin_link, title=title,
                           origin_author=origin_author, content=content,)
        yield item

