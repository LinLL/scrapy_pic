# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from app.model import Beautys
import json




class TrainPipeline(object):

    def __init__(self):
        engine = create_engine("sqlite:///app/fanfan.db")
        Session  = sessionmaker(bind=engine)
        self.db = Session()
        pass


    def process_item(self, item, spider):

        for beauty in  item.beautys:

            baby = Beautys(url=beauty["image_urls"].split("/")[-1], page=beauty["page"])
            self.db.add(baby)

            try:
                self.db.commit()
                return item
            except IntegrityError as e:
                self.db.rollback()



