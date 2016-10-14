# -*- coding: utf-8 -*-
from utils import conn
from sqlalchemy.exc import IntegrityError
from app.model import Beautys
from yunupload.upload import upqiniu





class TrainPipeline(object):

    def __init__(self):

        self.db = conn()
        pass


    def process_item(self,item,spider):

        beauty = item
        baby = Beautys(url=beauty["image_urls"].split("/")[-1], page=beauty["page"])
        self.db.add(baby)

        try:
            self.db.commit()
            upqiniu(baby.url)
            return item
        except IntegrityError as e:
            self.db.rollback()
            return item



