import sqlite3
import mysql.connector
from config import DATABASE_CONFIG

def initialize_sqlite():
    if DATABASE_CONFIG['type'] == 'sqlite':
        connection = sqlite3.connect(DATABASE_CONFIG['database'])
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS photos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL
            )
            """
        )
        connection.commit()
        cursor.close()
        connection.close()

initialize_sqlite()

def get_connection():
    if DATABASE_CONFIG['type'] == 'sqlite':
        return sqlite3.connect(DATABASE_CONFIG['database'])
    else:
        return mysql.connector.connect(
            host=DATABASE_CONFIG.get('host', ''),
            user=DATABASE_CONFIG.get('user', ''),
            password=DATABASE_CONFIG.get('password', ''),
            database=DATABASE_CONFIG.get('database', '')
        )


def get_all_photos():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM photos"
    try:
        cursor.execute(query)
        photos = cursor.fetchall()
    except sqlite3.OperationalError:
        photos = []  # Return an empty list if the table doesn't exist
    finally:
        cursor.close()
        connection.close()
    return photos

def add_photo(title, url):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO photos (title, url) VALUES (?, ?)" if DATABASE_CONFIG['type'] == 'sqlite' else "INSERT INTO photos (title, url) VALUES (%s, %s)"
    cursor.execute(query, (title, url))
    connection.commit()
    cursor.close()
    connection.close()
