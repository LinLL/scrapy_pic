__author__ = 'LGrok'

from app import create_app
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


def updatedb():
    """

    :return:
    """
    app = create_app()
    db = app.db
    with open('../Beauty.jl', "r") as bFile:
        for baby in json.load(bFile):
            pass

def conn(path="sqlite:///app/fanfan.db"):
        engine = create_engine(path)
        Session  = sessionmaker(bind=engine)
        return Session()