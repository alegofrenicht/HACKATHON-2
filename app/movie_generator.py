from app.models import Movie
from random import choice


def generator():
    generated = [Movie.query.filter_by(id=choice(range(1, 3997))).first() for _ in range(9)]
    return generated
