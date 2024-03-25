from models.__init__ import CONN, CURSOR

class Book:
    all = []

    def __init__(self, title, author, rating, author_id):
        self.title = title
        self.author = author
        self.rating = rating
        self.author_id = author_id
        self.id = None

    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, title_parameter):
        if(isinstance(title_parameter, str)) and (len(title_parameter) > 3):
            self._title = title_parameter
        else:
            raise ValueError("Title must be a string greater than 4 characters!")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author_parameter):

        from models.author import Author

        if(isinstance(author_parameter, str)) and (5 <= len(author_parameter) <= 50):
            self._author = author_parameter
        else:
            raise ValueError("Author must be a string between 5 and 50 characters!")
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if(isinstance(rating_parameter, int)) and (0 <= rating_parameter <= 6):
            self._rating = rating_parameter
        else:
            raise ValueError("Rating must be an integer between 0 and 6!")
        
    @property
    def author_id(self):
        return self._author_id
    
    @author_id.setter
    def author_id(self, author_id_paramter):
        if(isinstance(author_id_paramter, int)):
            self._author_id = author_id_paramter
        else:
            raise ValueError("Author ID must be an integer!")
        
    def __repr__(self):
        return f"<Book #{self.id}| Title: {self.title}, Author: {self.author}, Rating: {self.rating}, Author ID: {self.author_id}>"
    

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            rating INTEGER,
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
            INSERT INTO books (title, author, rating, author_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.rating, self.author_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Book.all.append(self)


    @classmethod
    def create(cls, title, author, rating, author_id):
        book = cls(title, author, rating, author_id)
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

        cls.all = [cls.instance_from_db(row) for row in rows]
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
        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, rating = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.author, self.rating, self.author_id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Book.all = [book for book in Book.all if book.id != self.id]

    def author(self):
        from models.author import Author

        sql = """
            SELECT authors.id, authors.name
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