__author__ = 'js'

# -*- coding: utf-8 -*-
import scrapy
import os.path
from items import TrainItem


class DomzSpider(scrapy.Spider):

    name = "jandan"
    allow_domain = ['jandan.net']
    start_urls = [
        "http://jandan.net/ooxx"
    ]



    def parse(self, response):

        cPage = response.xpath("//span[@class='current-comment-page']/text()").extract()[0][1:-1]
        for p in range(0,int(cPage)):
            url = "http://jandan.net/ooxx/page-{}#comments".format(p)
            yield scrapy.Request(url=url, callback=self.parseBeauty, meta={"page":p})


    def parseBeauty(self,response):

        bPictures = response.xpath("//a[@class='view_img_link']/@href").extract()
        for url in bPictures:
            item = TrainItem()
            item['image_urls'] = url
            yield item

