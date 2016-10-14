__author__ = 'LGrok'

from app.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




def conn(path=SQLALCHEMY_DATABASE_URI):
        engine = create_engine(path)
        Session  = sessionmaker(bind=engine)
        return Session()