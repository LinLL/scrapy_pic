__author__ = 'js'

# -*- coding: utf-8 -*-
import scrapy
import logging
from items import TrainItem,BeautyItems
from pipelines import TrainPipeline
from app.model import Beautys


class DomzSpider(scrapy.Spider):

    name = "jandan"
    allow_domain = ['jandan.net']
    start_urls = [
        "http://jandan.net/ooxx"
    ]



    def parse(self, response):

        cPage = response.xpath("//span[@class='current-comment-page']/text()").extract()[0][1:-1]

        pipe = TrainPipeline()
        for p in range(1,int(cPage)+1):
            if pipe.db.query(Beautys).filter(Beautys.page==p).first():
                continue
            url = "http://jandan.net/ooxx/page-{}#comments".format(p)
            yield scrapy.Request(url=url, callback=self.parseBeauty, meta={"page":p})


    def parseBeauty(self,response):

        bPictures = response.xpath("//a[@class='view_img_link']/@href").extract()
        items = BeautyItems()
        for num,url in enumerate(bPictures):
            item = TrainItem()
            item['image_urls'] = url
            item['page'] = response.meta["page"]
            items.beautys.append(item)

        return items

