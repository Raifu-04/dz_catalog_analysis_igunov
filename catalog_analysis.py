from math import*

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    count = 0
    total = 0
    for i in range(0, len(movies)):         # Прохожусь по элементам списка.
        for j in movies[i]:                 # Прохожусь по ключам словаря.
            if j == 'rating':
                total += movies[i][j]       # Суммирую все значения ключа.
                count += 1
    res = round(total / count, 1)
    return f'Средняя оценка по каталогу: {res}'

print(average_rating(movies))


def catalog_age_stats(movies, current_year=2026):
    old_movie = 0
    new_movie = 1000
    total = 0
    count = 0

    for i in range(0, len(movies)):                     # Прохожусь по элементам списка.
        for j in movies[i]:                             # Прохожусь по ключам словаря.
            if j == 'year':                             # Если ключ есть в словаре, проверяю по условию.
                if (current_year - movies[i][j]) > old_movie:
                    old_movie = current_year - movies[i][j]
                if (current_year - movies[i][j]) < new_movie:
                    new_movie = current_year - movies[i][j]
                total += current_year - movies[i][j]            # Сума всех возрастов фильмов.
        count += 1

    average_yeare = ceil(total / count)         # Округление среднего значения.
    res = [old_movie, new_movie, average_yeare]

    return tuple(res)

print(catalog_age_stats(movies))


def duration_in_hours(minutes):
    hour = minutes // 60
    minute = minutes % 60

    return f'{hour}ч {minute}м'

print(duration_in_hours(45))
    