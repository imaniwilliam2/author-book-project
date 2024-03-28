from models.author import Author
from models.book import Book
from models.review import Review

from models.__init__ import CONN, CURSOR

if __name__ == "__main__":
    Author.create_table()
    Book.create_table()
    Review.create_table()

    CURSOR.execute("DELETE FROM authors")
    CURSOR.execute("DELETE FROM books")
    CURSOR.execute("DELETE FROM reviews")
    CONN.commit()

    Author.create("Sarah", "J. Maas")
    Author.create("James", "Patterson")
    Author.create("Natasha", "Preston")
    Author.create("Tia", "Williams")


    Book.create("ACOTAR", "Sarah Maas", "Fantasy", 1)
    Book.create("ACOMAF", "Sarah Maas", "Fantasy", 1)
    Book.create("ACOWAR", "Sarah Maas", "Fantasy", 1)
    Book.create("Humans Bow", "James Patterson", "Fiction", 2)
    Book.create("The Cellar", "Natasha Preston", "Thriller", 3)

    Review.create("ACOWAR", 5, "Such a good read!", 2)
    Review.create("ACOWAR", 3, "Could have more action..", 2)
    Review.create("Humans Bow", 4, "So True!", 4)
    Review.create("The Cellar", 5, "This book left me with goosebumps!", 5)
    Review.create("ACOMAF", 5, "Must read fantasy book!", 2)
    Review.create("ACOMAF", 5, "I need the next book!", 2)
    Review.create("Humans Bow", 2, "Kinda lame!", 4)


    
    