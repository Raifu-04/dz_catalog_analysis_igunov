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

#================================ЭТАП 1================================

def average_rating(movies):
    count = 0
    total = 0
    for i in range(0, len(movies)):         # Прохожусь по элементам списка.
        for j in movies[i]:                 # Прохожусь по ключам словаря.
            if j == 'rating':
                total += movies[i][j]       # Суммирую все значения ключа.
                count += 1
    res = round(total / count, 1)
    return res

#print(average_rating(movies))


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

#print(catalog_age_stats(movies))


def duration_in_hours(minutes):
    hour = minutes // 60
    minute = minutes % 60

    return f'{hour}ч {minute}м'

#print(duration_in_hours(45))

#================================ЭТАП 2================================

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating < 9 and rating >= 7:
        return "хорошо"
    else:
        return "средне" if (rating < 7 and rating >= 5) else "слабо"



def decade_label(year):
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
        print('\t', i["title"])
    else:
        continue

count = 0
while count < len(movies):
    if movies[count]["rating"] > 9:
        print(f'\nШедевр: {movies[count]["title"]}')
        break
    count += 1
else:
    print("\n" + "Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for i in movies:
        if i["duration_min"] > threshold:
            count += 1
        else:
            continue
    return count

print(count_long_movies(movies))


#================================ЭТАП 4================================

def normalize_title(title):
    list_title = title.split(' ') 
    new_list_title = []
    for i in range(0, len(list_title)):
        new_list_title.append(str(list_title[i][0].upper()) + str(list_title[i][1::]))  #Первый символ каждого элемента делаю заглавной и объединяю с оствшимися, после чего добавляю новую строку в новый список.
    movie = ' '.join(new_list_title)        #Объединяю элементы списка с пробелом между ними.
    return movie

def make_slug(title):
    return normalize_title(title).lower().replace(' ', '-')     #Делаю все буквы строчными и заменяю пробел на тире.

print(make_slug("Silent Hours"))

def format_report_line(movie):
    for i in movies:
        if i == movie:  #Если названия фильмов совпадают, выпалняется блок действий.
            d_genres = list(i["genres"])    #Жанры фильма преобразуются из кортежа в список.
            d_genres.sort()
            str_genres = ', '.join(d_genres)    #Жанры объединятся запятой между ними
            return f'"{i["title"]}" ({i["year"]}) — {i["rating"]}/10, {duration_in_hours(i["duration_min"])}, жанры: {str_genres}.'

print(format_report_line(movies[1]))


#================================ЭТАП 5================================

def titles_sorted_by_rating(movies):
    sorted_list = sorted(movies, key=lambda m: m["rating"], reverse=True)
    list_movie = []
    for i in sorted_list:
        list_movie.append(i["title"])
    return list_movie

def top_n_by_rating(movies, n=3):
    list_top = []
    sorted_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)
    for i in range(0, n):
        list_top.append((sorted_rating[i]['title'], sorted_rating[i]['rating']))
    return list_top


#================================ЭТАП 6================================

def count_by_genre(movies):
    result = {}
    
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    
    return result



def actor_filmography(movies):
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


dict_rating = {i["title"]: i["rating"] for i in movies if i["rating"] > average_rating(movies)}
        