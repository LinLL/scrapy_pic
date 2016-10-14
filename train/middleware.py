__author__ = 'js'
import random,logging
from scrapy.exceptions import NotSupported
import scrapy

logger = logging.getLogger(__name__)
class BandedError(Exception):
    pass

class RandomUA(object):
#DownloaderMiddleware

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ErrorRetry(object):
#SpiderMiddleware

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self,crawler):
        pass

    def process_response(self, request, response, spider):
        if response.status == 400 or response.status == 503:  # common case
            request.cookies = []
            return request
        else:
            return response

    # def process_spider_exception(self, response, exception, spider):
    #     if isinstance(exception, BandedError):
    #         logger.debug("Request repeat url:{} , header:{}".format(response.url,response.headers))
    #         return []



class ProxyMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('HTTP_PROXY'))

    def __init__(self, proxys):
        self.proxy = proxys

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxy)
