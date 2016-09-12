from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Beautys(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(70))
    loves = db.Column(db.Integer)

    def __init__(self, name, url, loves=0):
        self.name = name
        self.url = url
        self.loves = loves

    def __repr__(self):
        return "<Beautys {} , url:{}, loves:{}>".format(self.name, self.url, self.loves)

