__author__ = 'js'
import scrapy

class USpider(scrapy.Spider):

    name = 'uspider'
    allow_domain = ["eastturkistan.net"]
    start_urls=['http://www.eastturkistan.net/uyghurce/kitap/musteqilliq/',
                'http://www.eastturkistan.net//uyghurche/kitap/umitbar/']

    def parse(self, response):

        pages = response.xpath("//a/@href").extract()
        for page in pages:
            url = response.url+page
            yield scrapy.Request(url=url, callback=self.download)

    def download(self,response):

        filename = response.url.split('/')[-1]
        with open(filename,'wb') as f:
            f.write(response.body)
