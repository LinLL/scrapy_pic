import os
##### GENERATE SECRET KEY #####
with open('.secret_key', 'ab+') as secret:
    secret.seek(0)  # Seek to beginning of file since a+ mode leaves you at the end and w+ deletes the file
    key = secret.read()
    if not key:
        key = os.urandom(64)
        secret.write(key)
        secret.flush()

##### SERVER SETTINGS #####
SECRET_KEY = key
DEBUG = True
HOST = "127.0.0.1"
SECRET_KEY =  key

SQLALCHEMY_DATABASE_URI = "sqlite:///fanfan.db"