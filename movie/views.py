import datetime

movie_bucket = []
user_bucket = []
review_bucket = []
seen = set()


def movie_review():
    add_movies()
    add_users()
    add_reviews()

    top_rated_movie_by_given_year(2006, False)
    top_rated_movie_by_given_year(2006, True)

    top_rated_movie_by_given_genre("Drama")
    top_rated_movie_by_avg_review_score(2006)

    return


def top_rated_movie_by_given_year(year, critics_preferred):
    max_rating = 0
    top_rated_movie = ''
    for movie in movie_bucket:
        if year in movie.values():
            if critics_preferred:
                critics = [user['user_name'] for user in user_bucket if user['critic']]
                rating = sum([review['rating'] for review in review_bucket if
                              review['movie'] == movie['name'] and review['user'] in critics and review[
                                  'reviewed_by_critic']])
            else:
                rating = sum([review['rating'] for review in review_bucket if review['movie'] == movie['name']])
            if rating > max_rating:
                max_rating = rating
                top_rated_movie = movie['name']

    print(top_rated_movie, "-", max_rating, "ratings")
    pass


def top_rated_movie_by_given_genre(genre):
    top_rating = 0
    top_rated_movie = ''
    for movie in movie_bucket:
        if genre in movie.values():
            rating = sum([review['rating'] for review in review_bucket if review['movie'] == movie['name']])
            if rating > top_rating:
                top_rating = rating
                top_rated_movie = movie['name']

    print(top_rated_movie, "-", top_rating, "ratings")

    pass


def top_rated_movie_by_avg_review_score(year):
    rating = 0
    total_reviews = 0
    for movie in movie_bucket:
        if year in movie.values():
            total_reviews = total_reviews + len([review for review in review_bucket if review['movie'] == movie['name']])
            rating = rating + sum([review['rating'] for review in review_bucket if review['movie'] == movie['name']])

    print(rating/total_reviews, "ratings")
    pass


def add_movies():
    add_movie("Don", 2006, "Action")
    add_movie("Tiger", 2021, "Drama")
    add_movie("Dhadak", 2007, "Drama")
    add_movie("Padmavat", 2006, "Comedy")
    add_movie("Lunchbox", 2015, "Drama")
    add_movie("Kabir Singh", 2015, "Romance")
    add_movie("Guru", 2006, "Action")
    add_movie("Metro", 2006, "Comedy")
    add_movie("Houseful", 2015, "Comedy")
    add_movie("Kurban", 2001, "Romance")
    add_movie("Apne", 2008, "Romance")
    pass


def add_users():
    add_user("SRK", False)
    add_user("Salman", False)
    add_user("Deepika", False)
    pass


def add_reviews():
    add_review("SRK", "Don", 2),
    add_review("SRK", "Padmavat", 8),
    add_review("Salman", "Don", 5),
    add_review("Deepika", "Don", 9),
    add_review("Deepika", "Guru", 6),
    add_review("SRK", "Don", 10),
    add_review("SRK", "Lunchbox", 6),
    add_review("SRK", "Tiger", 5),
    add_review("SRK", "Metro", 7),
    pass


def add_movie(name, year, genre):
    movie_bucket.append({'name': name,
                         'year': year,
                         'genre': genre})
    pass


def add_user(user, is_critic):
    user_bucket.append({'user_name': user, 'critic': is_critic, 'review_count': 0})
    pass


def add_review(user, movie, rating):
    try:
        review = {'user': user, 'movie': movie, 'rating': rating, 'reviewed_by_critic': False}
        for movies in movie_bucket:
            if movie in movies.values():
                review_items = tuple(review.items())

                if movies['year'] > datetime.datetime.today().year:
                    raise Exception("Movie yet to be released")

                if any(review_items[0] in i for i in seen):
                    if any(review_items[1] in i for i in seen):
                        raise Exception("Multiple reviews are not allowed")

                    user_record = next(item for item in user_bucket if item["user_name"] == user)
                    user_record['review_count'] = user_record['review_count'] + 1

                    if user_record['review_count'] == 3:
                        user_record['critic'] = True

                    if user_record['critic']:
                        review['rating'] = review['rating'] * 2
                        review['reviewed_by_critic'] = True

                seen.add(review_items)
                review_bucket.append(review)
    except Exception as e:
        print(e)

    pass
