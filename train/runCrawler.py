__author__ = 'js'

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())
process.crawl('jandan',domain='jandan.net')
#process.crawl('uspider',domain='eastturkistan.net')
process.start()