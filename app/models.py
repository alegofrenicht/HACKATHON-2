from app import db


class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    movies = db.relationship('Movie', backref='user', lazy='select')

    def add_to_watchlist(self, movie_id):
        movie = Movie.query.get(movie_id)
        new_movie = movie
        if movie:
            self.movies.append(new_movie)
            db.session.add(self)
            db.session.commit()

    def remove_from_watchlist(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            self.movies.remove(movie)
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    release_date = db.Column(db.Date, nullable=True)
    poster = db.Column(db.String(100), nullable=True)
    language = db.Column(db.String(100), nullable=True)
    director = db.Column(db.String(200), nullable=True)
    genre = db.Column(db.String(200), nullable=True)
    overview = db.Column(db.Text, nullable=True)
    runtime = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('app_user.id'))
    similar_movies = db.relationship('SimilarMovie', backref='movie', lazy='select')

    def __repr__(self):
        return '<Movie {}>'.format(self.title)


class SimilarMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    def __repr__(self):
        return '<SimilarMovie {}>'.format(self.title)

