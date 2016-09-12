from flask import Flask
from sqlalchemy_utils import create_database,database_exists

def create_app(config="app.config"):

    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config)


        from app.model import Beautys,db
        if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']) and not app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
            create_database(app.config['SQLALCHEMY_DATABASE_URI'])

        db.init_app(app)
        db.create_all()
        app.db = db

        from app.fanfan import fanfan
        app.register_blueprint(fanfan)

        return app