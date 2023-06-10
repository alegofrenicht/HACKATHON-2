from app import app
from random import choice
from string import printable


class Config:
    app.config['SECRET_KEY'] = ''.join(choice(printable) for i in range(50))
    app.config['DEBUG'] = True
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Microlab2gavno9@localhost/app_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
