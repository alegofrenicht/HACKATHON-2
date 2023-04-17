from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import datetime

app = Flask(__name__)
from config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


def populate_db():
    with app.app_context():
        with open('app\static\movies.json', 'rb') as f:
            data = json.load(f)
            for movie in data:
                directors = []
                genres = []
                for director in movie['directors']:
                    directors.append(director['name'])

                if type(movie['genres']) == list:
                    for genre in movie['genres']:
                        genres.append(genre)
                else:
                    genres.append(movie['genres'])

                try:
                    mov = models.Movie(
                                       title=movie['title'],
                                       release_date=datetime.datetime.strptime(movie['release_date'], '%Y-%m-%d').date(),
                                       poster=movie['poster_path'],
                                       language=movie['original_language'],
                                       director=', '.join(directors),
                                       genre=', '.join(genres),
                                       overview=movie['overview'],
                                       runtime=movie['runtime']
                                       )
                    for similar in movie['similar']:
                        sim_mov = models.SimilarMovie(title=similar['title'], movie=mov)
                        db.session.add(sim_mov)
                except KeyError:
                    pass
                db.session.add(mov)

            db.session.commit()
