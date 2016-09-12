from flask import Blueprint, render_template
from app.model import db, Beautys
import random

fanfan = Blueprint('fanfan', __name__)

@fanfan.route("/index")
@fanfan.route("/")
def index():

    count = db.session.query(Beautys).count()
    print(count)
    seek = random.randint(0,count)
    beautys = db.session.query(Beautys.url).filter(Beautys.id>seek).limit(10).all()
    print(beautys)
    return render_template("index.html", beautys=beautys)