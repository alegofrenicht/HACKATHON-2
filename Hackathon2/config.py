from app import app
from random import choice
from string import printable


class Config:
    app.config['SECRET_KEY'] = ''.join(choice(printable) for i in range(50))
    app.config['DEBUG'] = True

    db_info = {'host': 'localhost',
               'database': 'app_database',
               'psw': 'Microlab2gavno9',
               'user': 'postgres',
               'port': '5432'}
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
