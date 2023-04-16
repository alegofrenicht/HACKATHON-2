from app.models import AppUser
import pandas as pd


def get_stats(user):
    user_from_db = AppUser.query.filter_by(username=user).first()
    added_movies = user_from_db.movies
    number_added = len(added_movies)
    parameters = ['release_date', 'genre', 'director', 'language', 'runtime']

    release_dates = [str(movie.release_date)[:4] for movie in added_movies]
    release_dates = [int(date) for date in release_dates]
    release_dates = int(sum(release_dates) / number_added)
    eras = list(range(1900, 2030, 10))
    for index in range(1, len(eras)):
        if eras[index - 1] <= int(release_dates) <= eras[index]:
            release_dates = f"{eras[index - 1]} - {eras[index]}"
            break
    genres = []
    list_genres = [genres.append(genre) for movie in added_movies for genre in movie.genre.split(', ')]
    genre = pd.Series(genres)[0]

    directors = []
    directors_dict = {}
    list_directors = [directors.append(director) for movie in added_movies for director in movie.director.split(', ')]
    for director in directors:
        directors_dict[director] = directors_dict.get(director, 0) + 1
    directors = max(directors_dict, key=directors_dict.get)

    languages = []
    list_languages = [languages.append(language) for movie in added_movies for language in movie.language.split(', ')]
    language = pd.Series(languages)[0]

    runtimes = [movie.runtime for movie in added_movies]
    runtime = int(sum(runtimes) / number_added)

    return [release_dates, genre, directors, language, runtime]







