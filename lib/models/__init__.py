import sqlite3

CONN = sqlite3.connect('author_books.db')
CURSOR = CONN.cursor()
