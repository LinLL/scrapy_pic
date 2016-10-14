import requests
from utils import conn
import tempfile
from qiniu import put_stream,Auth,BucketManager
from multiprocessing import Pool
from app.model import Beautys


access_key = 'zb_bs-lr17r7P3zdUVDLFl0Iyk0olJEOKpBX9zRD'
secret_key = 'GhiUZq-N1lFoPXnxgGySz26jwoKPM69JwYyDnMT7'


bucket_name = 'fanba'


def uploadBeautys():
    """
    To upload picture into qiniu storage server
    :param path:
    :return:
    """
    db = conn()
    beatuy_names = [elem[0] for elem in db.query(Beautys.url).all()]

    pool = Pool(8)
    pool.map(upqiniu,beatuy_names)
    pool.close()
    pool.join()

def inqiniu(name):
    """
    To determine whether the file on the server
    :param name: file name
    :return: boolean
    """
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    ret, info = bucket.stat(bucket_name, name)
    return ret is not None

def upqiniu(name):

    url = "http://ww3.sinaimg.cn/large/{}".format(name)

    if "gif" in name:
        return
    if inqiniu(name):
        return
    try:
        bfile = requests.get(url).content
    except requests.exceptions.ConnectionError as e:
        url = "http://ww2.sinaimg.cn/large/{}".format(name)
        bfile = requests.get(url).content

    size = len(bfile)

    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, name, 3600)
    with tempfile.TemporaryFile() as temp:
        temp.write(bfile)
        temp.seek(0)
        ret, info = put_stream(up_token=token, key=name, file_name=name, data_size=size,
                               mime_type='application/octet-stream', input_stream=temp)

if __name__=="__main__":
    db = conn()
    meizi = db.query(Beautys).filter(Beautys.page=='10').count()
    print(meizi)


