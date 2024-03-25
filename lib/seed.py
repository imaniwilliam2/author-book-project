from models.author import Author
from models.book import Book

from models.__init__ import CONN, CURSOR

if __name__ == "__main__":
    Author.create_table()
    Book.create_table()

    CURSOR.execute("DELETE FROM authors")
    CURSOR.execute("DELETE FROM books")
    CONN.commit()

    Author.create("Sarah", "J. Maas")
    Author.create("James", "Patterson")
    Author.create("Natasha", "Preston")

    Book.create("ACOTAR", "Sarah Maas", 5, 1)
    Book.create("Humans Bow", "James Patterson", 3, 2)
    Book.create("The Cellar", "Natasha Preston", 5, 3)
    