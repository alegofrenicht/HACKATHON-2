from app import app
from random import choice
from string import printable


class Config:
    app.config['SECRET_KEY'] = ''.join(choice(printable) for i in range(50))
    app.config['DEBUG'] = True
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = "postgresql://alegofrenicht:jIdI1TF6x5h9YR9x0wIjo7FNbn9R5Uah@dpg-ci28kiu7avj2t331kri0-a.frankfurt-postgres.render.com/app_database_mce7"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
