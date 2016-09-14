from flask import Blueprint, render_template, redirect, url_for
from app.model import db, Beautys
import random,json

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


@fanfan.route("/api/<action>")
def api(action):
    if action == "action":
        count = db.session.query(Beautys).count()
        seek = random.randint(0,count)
        beautys = db.session.query(Beautys.url).filter(Beautys.id>seek).limit(10).all()
        return json.dumps(beautys)
    return redirect(url_for('index'))