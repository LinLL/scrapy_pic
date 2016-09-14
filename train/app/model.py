from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Beautys(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(70), unique=True)
    loves = db.Column(db.Integer)
    page = db.Column(db.Integer)

    def __init__(self, url, page, loves=0):

        self.url = url
        self.loves = loves
        self.page = page

    def __repr__(self):
        return "<Beautys , url:{}, loves:{}, page:{}>".format( self.url, self.loves ,self.page)

