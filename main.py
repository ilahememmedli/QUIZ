import requests
import pymysql
import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345',
    db='MySQL',
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

MOVIE=input('Film daxil edin:')

API_KEY='5d9df2b8'

url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"

response = requests.get(url)
data = response.json()

if data['Response'] == 'True':
    movie_title=data.get('Title')
    released=data.get('Released')
    genre=data.get('Genre')
    director=data.get('Director')

    print(f"Title: {movie_title}")
    print(f"Released: {released}")
    print(f"Genre: {genre}")
    print(f"Director: {director}")
else:
    print('Bu film databasede movcud deyil')

def insert_into_movie(title,released,genre,director):
    with connection:
        with connection.cursor() as cursor:
            sql= "INSERT INTO MySQL.Movie_info(title,released,genre,director) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (title,released,genre,director))
        connection.commit()
insert_into_movie(movie_title,released,genre,director)