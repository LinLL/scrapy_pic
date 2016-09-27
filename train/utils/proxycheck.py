import requests
import threading
from utils.GetProxy import GetProxy



proxys = GetProxy().get()

real_proxys = []

def proxyCheck():
    while proxys.empty() is False:
        line = proxys.get()
        if len(line) == 0: break
        protocol, proxy = line.split('=')
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
                   }
        proxies = {"http":"http://"+proxy}

        try:
            res = requests.get("http://www.jandan.net/", proxies=proxies, timeout=3, headers=headers)

            if  res.status_code==200:
                real_proxys.append(proxy)
        except Exception as e:
            pass


def run():

    all_thread = []
    for i in range(50):
        t = threading.Thread(target=proxyCheck)
        all_thread.append(t)
        t.start()

    for t in all_thread:
        t.join()
    return ["http://{}".format(proxy) for proxy in real_proxys]

if __name__=="__main__":
    print(run())