from app import app
from random import choice
from string import printable
from os import getenv


class Config:
    app.config['SECRET_KEY'] = ''.join(choice(printable) for i in range(50))
    app.config['DEBUG'] = True
    SQLALCHEMY_DATABASE_URI = getenv('DB_URI')
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
