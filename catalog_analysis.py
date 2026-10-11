from math import ceil

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

#================================ЭТАП 1================================

def average_rating(movies):     # Возвращает среднюю оценку по каталогу
    count = 0
    total = 0

    for movie in movies:  
        if "rating" in movie:
            total += movie["rating"]
            count += 1
        
    res = round(total / count, 1)
    return res


def catalog_age_stats(movies, current_year=2026):       # Возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)
    old_movie = 0
    new_movie = 1000
    total = 0
    count = 0

    for movie in movies:
        if "year" in movie:
            if (current_year - movie["year"] ) > old_movie:
                old_movie = current_year - movie["year"] 
            if (current_year - movie["year"] ) < new_movie:
                new_movie = current_year - movie["year"] 
            total += current_year - movie["year"]
        count += 1

    average_yeare = ceil(total / count)
    res = (old_movie, new_movie, average_yeare)

    return res


def duration_in_hours(minutes):     # Переводит минуты в формат "2ч 35м"
    hour = minutes // 60
    minute = minutes % 60

    return f'{hour}ч {minute}м'


#================================ЭТАП 2================================

def rating_tier(rating):        # Возвращает категорию: "шедевр" (≥9), "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5)
    if rating >= 9:
        return "шедевр"
    elif rating < 9 and rating >= 7:
        return "хорошо"
    else:
        return "средне" if (rating < 7 and rating >= 5) else "слабо"



def decade_label(year):     # Возвращает метку "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015)
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"
        case _:
            return "неверная дата"


#================================ЭТАП 3================================

print("Фильмы НЕ жанра комедия:")
for i in movies:
    if "comedy" not in i["genres"]:
        print('  ', i["title"])          # Выводит названия всех фильмов, которые НЕ относятся к жанру "comedy"
    else:
        continue


count = 0
while count < len(movies):
    if movies[count]["rating"] > 9:     # Выводит первый фильм с рейтингом выше 9
        print(f'\nШедевр: {movies[count]["title"]}')
        break
    count += 1
else:
    print("\n" + "Шедевров не найдено")     # Если фильма такого нет, выводит "Шедевров не найдено"

def count_long_movies(movies, threshold=120):       # Возвращает количество фильмов длиннее threshold минут
    count = 0
    for i in movies:
        if i["duration_min"] > threshold:
            count += 1

    return count


#================================ЭТАП 4================================

def normalize_title(title):     # Возвращает строку формата Title Case (каждое слово с заглавной буквы)
    list_title = title.split(' ') 
    new_list_title = []
    for i in range(0, len(list_title)):
        new_list_title.append(list_title[i][0].upper() + list_title[i][1::])
    movie = ' '.join(new_list_title)
    return movie

def make_slug(title):       # Возвращает нормализованное название в «слаг» вида the-quiet-algorithm
    return normalize_title(title).lower().replace(' ', '-')


def format_report_line(movie):      # Возвращает единую строку с описанием фильма
    for i in movies:
        if i == movie:
            d_genres = list(i["genres"])
            d_genres.sort()
            str_genres = ', '.join(d_genres)
            return f'"{normalize_title(i["title"])}" ({i["year"]}) — {i["rating"]}/10, {duration_in_hours(i["duration_min"])}, жанры: {str_genres}'
        

#================================ЭТАП 5================================

def titles_sorted_by_rating(movies):        # Возвращает список названий фильмов, отсортированных по убыванию рейтинга
    sorted_list = sorted(movies, key=lambda m: m["rating"], reverse=True)
    list_movie = []
    for i in sorted_list:
        list_movie.append(i["title"])
    return list_movie

def top_n_by_rating(movies, n=3):       # Возвращает список названий фильмов, отсортированных по убыванию рейтинга
    list_top = []
    sorted_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)
    for i in range(0, n):
        list_top.append((sorted_rating[i]['title'], sorted_rating[i]['rating']))
    return list_top


#================================ЭТАП 6================================

def count_by_genre(movies):     # Возвращает словарь {жанр: количество фильмов}
    result = {}
    
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1

    return result


def actor_filmography(movies):      # Возвращает словарь {актер: [список названий фильмов]}
    list_actor = []
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in list_actor:
                list_actor.append(actor)

    result = {}
    for actor in list_actor:
        list_movies = []
        for movie in movies:
            if actor in movie["actors"]:
                list_movies.append(movie["title"])
        result[actor] = list_movies

    return result

avg = average_rating(movies)
dict_rating = {i["title"]: i["rating"] for i in movies if i["rating"] > avg}     # Генератор словарь {title: rating} для фильмов с рейтингом выше среднего

#================================ЭТАП 7================================

def all_genres(movies):     # Возвращает множество всех уникальных жанров каталога
    genres_set = set()
    for movie in movies:
        genres_set = genres_set | movie["genres"]

    return genres_set


def common_actors(movie1, movie2):      # Возвращает множество актеров, снимавшихся в обоих фильмах
    res = set(movie1["actors"]) & set(movie2["actors"])
    return res


def genres_only_in_one(movies_a, movies_b):     # Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b
    set_genre_1 = set()

    for movie in movies_a:
        set_genre_1 = set_genre_1 | movie["genres"]

    set_genre_2 = set()

    for movie in movies_b:
        set_genre_2 = set_genre_2 | movie["genres"]

    result = set_genre_1 - set_genre_2 

    return result



#================================ЭТАП 8================================

def iter_high_rated(movies, min_rating=8.0):        # Функция-генератор, где yield лениво отдает фильмы с рейтингом не ниже min_rating
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

for movie in iter_high_rated(movies):       # Печатает сгенерированные фильмы из high_rated(movies, min_rating=8.0)
    print(format_report_line(movie))

total_sum = sum(m["duration_min"] for m in movies if m["rating"] > 7)       # Генераторное выражение считывающее суммарную длительность всех фильмов с рейтингом выше 7 в минутах
print(total_sum)


#================================ЭТАП 9================================

def build_report(movies):   # Консольный отчет
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f'Средний рейтинг: {average_rating(movies)}')
    print(f'Средний возраст фильмов: {catalog_age_stats(movies)[-1]} лет')

    top_movies = []     # Список топовых фильмов
    for movie in top_n_by_rating(movies):
        top_movies.append(movie[0])

    print("\nТоп-3 фильма:")

    for title in top_movies:
        for movie in movies:
            if movie["title"] == title:
                print(f'  {format_report_line(movie)}')
                break

    print("\nФильмов по жанрам:")

    for genre in sorted(count_by_genre(movies).items(), key=lambda x: (-x[1], x[0]), reverse=False):    # Проход по элементам отсортированным по значениям ключа парам (ключ, значение)
        print(f'  {genre[0]} — {genre[1]}')

    list_genres = sorted(all_genres(movies))
    print(f'\nВсе жанры каталога: {', '.join(list_genres)}')

build_report(movies)