import sqlite3
from fetch_data import fetch_movie_data

def store_movie_data(movie_data):
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            imdb_id TEXT UNIQUE,
            release_date TEXT
        )
    """)

    for movie in movie_data:
        c.execute("""
            INSERT INTO movies (title, imdb_id, release_date) VALUES (?, ?, ?)
            ON CONFLICT(imdb_id) DO UPDATE 
            SET title = excluded.title, release_date = excluded.release_date
        """, (movie['Movie'], movie['IMDB ID'], movie['Release Date']))

    conn.commit()
    conn.close()

movie_data = fetch_movie_data()
store_movie_data(movie_data)
