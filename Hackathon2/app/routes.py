from app import app, db
from flask import render_template, flash, redirect, url_for, session, request
from app.forms import LoginForm, RegisterForm
from app.models import AppUser, Movie, SimilarMovie
from random import choice
from app.movie_generator import generator
from app.stats_generator import get_stats


@app.route('/')
def index():  # creates main template with navigation bar
    return redirect(url_for('home'))


@app.route('/home', methods=("GET", "POST"))
def home():
    form = LoginForm()
    login = AppUser.query.filter_by(email=form.mail.data).first()
    movie = choice(Movie.query.all())
    if form.validate_on_submit():
        if login:
            session['user_name'] = login.username
            session['logged_in'] = True
            flash(f'Good to see you, {login.username}!')
            return redirect(url_for('watchlist', user=login.username))
        else:
            flash('Invalid username or password')
            return redirect(url_for('index'))

    return render_template('home.html', title='Sign In', form=form, movie=movie)


@app.route('/logout')
def logout():
    # remove the user ID from the session
    session.pop('user_name', None)
    session.pop('logged_in', None)
    flash('You were logged out', 'warning')
    return redirect(url_for('home'))


@app.route('/register', methods=("GET", "POST"))
def register():
    form = RegisterForm()
    user_from_db = AppUser.query.filter_by(email=form.mail.data).first()
    movie = choice(Movie.query.all())
    if form.validate_on_submit():
        if user_from_db:
            flash('User already exists')
            return redirect(url_for('register'))
        else:
            user = AppUser(username=form.username.data, email=form.mail.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form, movie=movie)


@app.route('/home/<user>')
def watchlist(user):
    user_from_db = AppUser.query.filter_by(username=user).first()
    movie = choice(Movie.query.all())
    quiz = True
    if session['logged_in'] is True:
        if user_from_db.movies:
            quiz = False
            movies = user_from_db.movies
            similar_movies = []
            for movie in movies:
                for similar_movie in movie.similar_movies:
                    mov = Movie.query.filter_by(title=similar_movie.title).first()
                    if similar_movie.title in {m.title for m in user_from_db.movies}:
                        continue
                    else:
                        similar_movies.append(mov)
            similar_movies = list(set(similar_movies))
            return render_template('watchlist.html', title='Watchlist', user=user_from_db, movie=movie, quiz=quiz,
                                   movies=movies, similar_movies=similar_movies)
        random_movies = generator()
        return render_template('watchlist.html', title='Watchlist', user=user_from_db, movie=movie, quiz=quiz, movies=random_movies)

    else:
        return redirect(url_for('home'))


@app.route('/home/add_movies', methods=('POST',))
def add_movies():
    user = session['user_name']
    selected_movies = request.json
    user_from_db = AppUser.query.filter_by(username=user).first()
    if session['logged_in'] is True:
        for movie_id in selected_movies:
            user_from_db.add_to_watchlist(int(movie_id))
        print('Redirecting to watchlist')
        return redirect(url_for('watchlist', user=user))
    else:
        return redirect(url_for('home'))


@app.route('/home/<user>/<movie_id>/remove_from_watchlist')
def remove_from_watchlist(user, movie_id):
    user_from_db = AppUser.query.filter_by(username=user).first()
    user_from_db.remove_from_watchlist(int(movie_id))
    return redirect(url_for('watchlist', user=user))


@app.route('/home/<user>/<movie_id>/add_to_watchlist')
def add_to_watchlist(user, movie_id):
    user_from_db = AppUser.query.filter_by(username=user).first()
    user_from_db.add_to_watchlist(int(movie_id))
    return redirect(url_for('watchlist', user=user))


@app.route('/statistics/<user>')
def statistics(user):
    user_from_db = AppUser.query.filter_by(username=user).first()
    movie = choice(Movie.query.all())
    if session['logged_in'] is True:
        stats = get_stats(user)
        return render_template('statistics.html', title='Statistics', user=user_from_db, movie=movie, stats=stats)
    else:
        return redirect(url_for('home'))
