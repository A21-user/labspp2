movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]
#1#
def is_high_score(movie):
    return movie["imdb"] > 5.5


print(is_high_score(movies[0]))  # Usual Suspects (7.0) -> True
print(is_high_score(movies[7]))  # Bride Wars (5.4) -> False

#2#
def high_score_movies(movies):
    result = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            result.append(movie)
    return result

good_movies = high_score_movies(movies)

for m in good_movies:
    print(m["name"], "-", m["imdb"])

#3#

def movies_by_category(movies, category_name):
    return [movie for movie in movies if movie["category"].lower() == category_name.lower()]

romance_movies = movies_by_category(movies, "Romance")

for m in romance_movies:
    print(m["name"], "-", m["imdb"])

#4#
def average_imdb(movies):
    total = 0
    for movie in movies:
        total += movie["imdb"]
    return total / len(movies)

print("Average IMDB score:", round(average_imdb(movies), 2))

#5#
def average_imdb_by_category(movies, category_name):
    scores = [m["imdb"] for m in movies if m["category"].lower() == category_name.lower()]
    return sum(scores) / len(scores) if scores else 0
