from models.__init__ import CONN, CURSOR

class Book:
    all = []

    def __init__(self, title, author, genre, author_id):
        self.title = title
        self.author = author
        self._genre = genre
        self._author_id = author_id
        self.id = None

    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, title_parameter):
        if(isinstance(title_parameter, str)) and (len(title_parameter) > 3):
            self._title = title_parameter
        else:
            raise ValueError("Title must be a string greater than 3characters!")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author_parameter):

        if(isinstance(author_parameter, str)) and (5 <= len(author_parameter) <= 50):
            self._author = author_parameter
        else:
            raise ValueError("Author must be a string between 5 and 50 characters!")
        


    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre_parameter):
        if(isinstance(genre_parameter, str)) and (len(genre_parameter)):
            self._genre = genre_parameter
        else:
            raise ValueError("Genre must be a string greater than 0 characters!")

    @property
    def author_id(self):
        return self._author_id
    
    @author_id.setter
    def author_id(self, author_id_paramter):

        from models.author import Author
        
        if (isinstance(author_id_paramter, int)) and Author.find_by_id(author_id_paramter):
            self._author_id = author_id_paramter
        else:
            raise ValueError("Author ID must be an integer in the database!")
        
    def __repr__(self):
        return f"<Book #{self.id}| Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Author ID: {self.author_id}>"
    

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            author_id INTEGER)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(self):

        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)

    def save(self):

        sql = """
            INSERT INTO books (title, author, genre, author_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.genre, self.author_id,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Book.all.append(self)


    @classmethod
    def create(cls, title, author, genre, author_id):

        book = cls(title, author, genre, author_id)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        book = cls(row[1], row[2], row[3], row[4])
        book.id = row[0]
        return book
    
    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row).title for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    @classmethod
    def find_by_title(cls, title):
        sql = """   
            SELECT *
            FROM books
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, genre = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.author, self.genre, self.author_id, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        if self in Book.all:
            Book.all.remove(self)
            
    def authors(self):
        from models.author import Author

        sql = """
            SELECT *
            FROM authors
            INNER JOIN books
            ON authors.id = books.author_id
            WHERE books.author_id = ?
        """

        row = CURSOR.execute(sql, (self.author_id,)).fetchone()

        if row:
            return Author.instance_from_db(row)
        else:
            return None
        
    def reviews(self):

        from models.review import Review

        sql = """
            SELECT *
            FROM reviews
            WHERE reviews.book_id = ? 
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Review.instance_from_db(row).text for row in rows]
