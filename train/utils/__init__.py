__author__ = 'LGrok'

from app import create_app
import json

def updatedb():
    """

    :return:
    """
    app = create_app()
    db = app.db
    with open('../Beauty.jl', "r") as bFile:
        for baby in json.load(bFile):
            pass