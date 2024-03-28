from models.__init__ import CONN, CURSOR

class Author:

    all = []


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = None

    @property
    def first_name(self):
        return self._first_name 
    
    @first_name.setter
    def first_name(self, first_name_parameter):
        if(isinstance(first_name_parameter, str)) and (len(first_name_parameter) >= 3):
            self._first_name = first_name_parameter
        else:
            raise ValueError("First Name must be a string greater than or equal to 3 characters!")
        

    @property
    def last_name(self):
        return self._last_name 
    
    @last_name.setter
    def last_name(self, last_name_parameter):
        if(isinstance(last_name_parameter, str)) and (len(last_name_parameter) >= 3):
            self._last_name = last_name_parameter
        else:
            raise ValueError("Last Name must be a string greater than or equal to 3 characters!")
        
    def __repr__(self):
        return f"<Author #{self.id}| First Name: {self.first_name}, Last Name: {self.last_name} >"
    

    @classmethod
    def create_table(cls):

        sql="""
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        
        sql = """
            DROP TABLE IF EXISTS authors;
        """
        CURSOR.execute(sql)

    def save(self):

        sql = """
            INSERT INTO authors (first_name, last_name)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Author.all.append(self)

    @classmethod
    def create(cls, first_name, last_name):

        author = cls(first_name, last_name)
        author.save()
        return author
    
    @classmethod
    def instance_from_db(cls, row):
        author = cls(row[1], row[2])
        author.id = row[0]
        return author
    
    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT * 
            FROM authors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    @classmethod
    def find_by_last_name(cls, last_name):

        sql = """
            SELECT *
            FROM authors
            WHERE last_name = ?
        """
        row = CURSOR.execute(sql, (last_name,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):

        sql = """
            UPDATE authors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.id))
        CONN.commit()
        
    def delete(self):

        sql = """   
            DELETE FROM authors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Author.all = [author for author in Author.all if author.id != self.id]

    def books(self):
        from models.book import Book

        sql = """
            SELECT *
            FROM books
            WHERE books.author_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Book.instance_from_db(row).title for row in rows]
    
    def author_reviews(self):
        from models.review import Review

        sql = """
            SELECT reviews.*
            FROM reviews
            JOIN books ON reviews.book_id = books.id
            WHERE books.author_id = ? 
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Review.instance_from_db(row) for row in rows]
