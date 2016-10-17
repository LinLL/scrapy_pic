__author__ = 'js'

# -*- coding: utf-8 -*-
import scrapy
import logging
from items import TrainItem
from pipelines import TrainPipeline
from app.model import Beautys


class DomzSpider(scrapy.Spider):

    name = "jandan"
    allow_domain = ['jandan.net']
    start_urls = [
        "http://jandan.net/ooxx"
    ]
    pipe = TrainPipeline()

    def parse(self, response):

        cPage = response.xpath("//span[@class='current-comment-page']/text()").extract()[0][1:-1]
        for p in range(1, int(cPage)+1):
            if self.pipe.db.query(Beautys).filter(Beautys.page==p).count() < 10:
                url = "http://jandan.net/ooxx/page-{}#comments".format(p)
                yield scrapy.Request(url=url, callback=self.parseBeauty, meta={"page":p})


    def parseBeauty(self, response):

        bPictures = response.xpath("//a[@class='view_img_link']/@href").extract()
        page_num = self.pipe.db.query(Beautys).filter(Beautys.page==response.meta["page"]).count()
        if page_num<len(bPictures):
            page_list = self.pipe.db.query(Beautys.url).filter(Beautys.page==response.meta["page"]).all()
            for name in bPictures:
                if (name.split("/")[-1],) not in page_list:
                    item = TrainItem()
                    item['image_urls'] = name
                    item['page'] = response.meta["page"]
                    yield item

