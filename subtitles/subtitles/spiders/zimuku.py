# -*- coding: utf-8 -*-
import scrapy
from subtitles.items import SubtitlesItem

class ZimukuSpider(scrapy.Spider):
    name = 'zimuku'
    allowed_domains = ['www.zimuku.cn']
    def __init__(self, movie='test', *args, **kwargs):
        super(ZimukuSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://%s/search?q=%s' % (self.allowed_domains[0], movie)]
    def parse(self, response):
        movie_url_list = response.xpath('//div[@class="title"]/p[@class="tt clearfix"]/a/@href').extract()
        for movie_url in movie_url_list:
            yield scrapy.Request('http://%s%s' % (self.allowed_domains[0], movie_url), callback=self.parse_movie)

    def parse_movie(self, response):
        subtitle_url_list = response.xpath('//table[@id="subtb"]/tbody/tr/td[@class="first"]/a/@href').extract()
        for subtitle_url in subtitle_url_list:
            yield scrapy.Request('http://%s%s' % (self.allowed_domains[0], subtitle_url), callback=self.parse_subtitle)

    def parse_subtitle(self, response):
        item = SubtitlesItem()
        item['title'] = response.xpath('//div[@class="md_tt prel"]/h1/text()').extract()
        item['rate'] = response.xpath('//div[@id="scinfo"]/i/b/text()').extract()
        item['lang'] = response.xpath('//ul[@class="subinfo clearfix"]/li[1]/img/@alt').extract()
        item['type'] = response.xpath('//ul[@class="subinfo clearfix"]/li[2]/span/text()').extract()
        item['download_number'] = response.xpath('//ul[@class="subinfo clearfix"]/li[3]/text()').extract()
        item['download_url'] = response.xpath('//ul[@class="subinfo clearfix"]/li[last()]/div/a[@id="down1"]/@href').extract()
        yield item