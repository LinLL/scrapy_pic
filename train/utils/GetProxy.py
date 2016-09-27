from bs4 import BeautifulSoup
import urllib,sys,threading,requests,base64,re
from multiprocessing.dummy import Pool
from queue import Queue
import codecs

class GetProxy(object):

    lock = threading.Lock()
    pages = range(1,20)
    pa = re.compile(r'(rot13\(")([\w=]+)')
    proxys = Queue()
    pool = Pool(30)


    def proxyPage(self, page):
        headers = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
        try:
            req = requests.get('https://www.cool-proxy.net/proxies/http_proxy_list/page:{page}/sort:score/direction:desc'.format(page=page), headers=headers)
        except requests.exceptions.ConnectionError as e:
            pass
        html_doc = req.text
        soup = BeautifulSoup(html_doc,'lxml')
        trs = soup.find_all(class_="time")
        trs = [item.find_parent() for item in trs]
        for tr in trs:
            tds = tr.find_all('td')
            ip = self.pa.search(tds[0].string).group(2)
            ip = base64.b64decode(codecs.decode(ip,'rot13')).decode()
            port = tds[1].text.strip()
            protocol = "HTTP"
            if protocol == 'HTTP' or protocol == 'HTTPS':
                proxy = '%s=%s:%s' % (protocol, ip, port)
                self.proxys.put(proxy)


    def get(self, pages=pages):
        """
        Get proxy from cool-proxy
        :param pages: range of page
        :return: (Queue) the queue of proxys
        """
        try:
            self.pool.map(self.proxyPage,pages)
        except urllib.error.HTTPError as e:
            self.run(e.geturl().split('/')[-1])
        return self.proxys


