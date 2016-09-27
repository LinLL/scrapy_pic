import requests
import json
import tempfile
from qiniu import put_stream,Auth,put_file
from multiprocessing import Pool
from utils import conn

access_key = 'zb_bs-lr17r7P3zdUVDLFl0Iyk0olJEOKpBX9zRD'
secret_key = 'GhiUZq-N1lFoPXnxgGySz26jwoKPM69JwYyDnMT7'


bucket_name = 'fanba'


def upload(path):


    with open(path,'r') as beauties:
    
        babys = json.load(beauties)
        pool = Pool(8)
        pool.map(upqiniu,babys)
        pool.close()
        pool.join()


def upqiniu(baby):

    url = "http://ww3.sinaimg.cn/large/{}".format(baby["url"])
    upname = url.split("/")[-1]
    if "gif" in upname:
        return
    bfile = requests.get(url).content
    size = len(bfile)

    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, upname, 3600)
    with tempfile.TemporaryFile() as temp:
        temp.write(bfile)
        temp.seek(0)
        ret, info = put_stream(up_token=token, key=upname, file_name=upname, data_size=size,
                               mime_type='application/octet-stream', input_stream=temp)

if __name__=="__main__":
    upload("../Beauty.jl")