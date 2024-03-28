from models.__init__ import CONN, CURSOR

class Review:

    all = []


    def __init__(self, book_title, rating, text, book_id):
        self.book_title = book_title
        self._rating = rating
        self.text = text
        self._book_id = book_id
        self.id = None


    @property
    def book_title(self):
        return self._book_title
    
    @book_title.setter
    def book_title(self, book_title_parameter):
        if(isinstance(book_title_parameter, str)):
            self._book_title = book_title_parameter
        else:
            raise ValueError("Book title must be a string!")
        


    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if(isinstance(rating_parameter, int)) and (0 <= rating_parameter <= 5):
            self._rating = rating_parameter
        else:
            raise ValueError("Rating must between a integer between 0 and 5!")
        

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_parameter):
        if(isinstance(text_parameter, str)):
            self._text = text_parameter
        else:
            raise ValueError("Text must be a string!")

    
    @property
    def book_id(self):
        return self._book_id
    
    @book_id.setter
    def book_id(self, book_id_paramter):

        from models.book import Book
        
        if (isinstance(book_id_paramter, int)) and Book.find_by_id(book_id_paramter):
            self._book_id = book_id_paramter
        else:
            raise ValueError("Book ID must be an integer in the database!")
        

    @property
    def book_id(self):
        return self._book_id
    
    @book_id.setter
    def book_id(self, book_id_paramter):

        from models.book import Book
        
        if (isinstance(book_id_paramter, int)) and Book.find_by_id(book_id_paramter):
            self._book_id = book_id_paramter
        else:
            raise ValueError("Author ID must be an integer in the database!")
        

    def __repr__(self):
        return f"<Review #{self.id}| Book Title: {self.book_title}, Rating: {self.rating}, Text: {self.text}, Book ID: {self.book_id}>"
    
        



   
    @classmethod
    def create_table(cls):

        sql="""
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            book_title TEXT,
            rating INTEGER,
            text TEXT,
            book_id INTEGER)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)

    def save(self):

        sql = """
            INSERT INTO reviews (book_title, rating, text, book_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.book_title, self.rating, self.text, self.book_id,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Review.all.append(self)

    @classmethod
    def create(cls, book_title, rating, text, book_id):

        review = cls(book_title, rating, text, book_id)
        review.save()
        return review
    
    @classmethod
    def instance_from_db(cls, row):
        review = cls(row[1], row[2], row[3], row[4])
        review.id = row[0]
        return review
    
    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM reviews
        """
        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT * 
            FROM reviews
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    @classmethod
    def find_by_rating(cls, rating):

        sql = """
            SELECT *
            FROM reviews
            WHERE rating = ?
        """
        row = CURSOR.execute(sql, (rating,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):

        sql = """
            UPDATE reviews
            SET book_title = ?, rating = ?, text = ?, book_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.book_title, self.rating, self.text, self.book_id, self.id))
        CONN.commit()
        
    def delete(self):

        sql = """   
            DELETE FROM reviews
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Review.all = [review for review in Review.all if review.id != self.id]

    def book(self):

        from models.book import Book

        sql = """
            SELECT *
            FROM books
            INNER JOIN reviews
            ON books.id = reviews.book_id
            WHERE reviews.book_id = ? 
        """
        row = CURSOR.execute(sql, (self.id,)).fetchone()

        if row:
            return Book.instance_from_db(row)
        else:
            return None
