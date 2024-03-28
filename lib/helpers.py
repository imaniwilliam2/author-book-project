# lib/helpers.py

from models.author import Author
from models.book import Book
from models.review import Review


def initalization():
    Author.create_table()
    Book.create_table()

    Author.get_all()
    Book.get_all()


def exit_program():
    print("Happy Reading! Bye!")
    exit()

def author_data():
    while(True):
        author_menu()
        choice = input("Select an option from the menu: ")
        if(choice == "1"):
            get_author()
            break
        elif(choice == "2"):
            create_author()
            break
        elif(choice == "3"):
            update_author()
            break
        elif(choice == "4"):
            delete_author()
            break
        elif(choice == "5"):
            get_author_books()
            break
        elif(choice == "0"):
            break
        else:
            print("Invalid option! Please select from menu.\n")




def author_menu():
    print("\nAuthor Menu:")
    print("1: Retrieve Author Data")
    print("2: Add a New Author")
    print("3: Update an Author")
    print("4: Delete an Author")
    print("5: Retrieve an Author's books")
    print("0: Back to Main Menu\n")

def create_author():
    first_name = input("\nEnter a First Name for the New Author: ")
    last_name = input("Enter a Last Name for the New Author: ")
    new_author = Author.create(first_name, last_name)
    print("\nHere are the details for the New Author: ")
    print(new_author)
    choice =  input("\nPress 'return' to continue...")

def get_author():
    get_author_menu()
    choice = input("Select an option from the menu: ")

    while(True):
        if(choice == "1"):
            print("\n These are all the Authors in our Library:")
            for author in Author.all:
                print(author)
            choice = input("\nPress 'return' to continue...")
            break
        elif(choice == "2"):
            while(True):
                try: 
                    choice = input("\nEnter ID to search for Author: ")
                    choice = int(choice)
                    author = Author.find_by_id(choice)
                    if(author):
                        print("\nHere is the Author specified by ID:")
                        print(Author.find_by_id(choice))
                        choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nAuthor Not Found!")
                        choice = input("Would you like to try again? Y/N: ")
                        if(choice == 'N'):
                            break
                        elif(choice == 'Y'):
                            None
                        else:
                            print("\nInvalid input! Try Again")
                             
                except:
                    print("Invalid input! Try Again!")
                    choice = input("\nPress 'return' to continue...")

            break
        elif(choice == "3"):
            while(True):
                try:
                    choice = input("\nEnter Last Name to search for Author: ")
                    choice = str(choice)
                    author = Author.find_by_last_name(choice)
                    if(author):
                        print("\nHere is the Author specified by Last Name:")
                        print(Author.find_by_last_name(choice))
                        choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nAuthor Not Found!")
                        choice = input("Would you like to try again? Y/N: ")
                        if(choice == 'N'):
                            break
                        elif(choice == 'Y'):
                            None
                        else:
                            print("\nInvalid input! Try Again")

                except:
                    print("Invalid input! Try Again!")
                    choice = input("\nPress 'return' to continue...")


            break
        elif(choice == "0"):
            author_menu()
            choice = input("Select an option from the menu: ")
            break
        else:
            print("Invalid option! Please choose from menu.")



def get_author_menu():
    print("\nWould you like to get all the Authors or just one?")
    print("1: Get All Authors")
    print("2: Get One Author By ID")
    print("3: Get One Author By Last Name")
    print("0: Back to Author Menu\n")
    

def update_author():
    while(True):
        try:
            choice = input("\nEnter ID to update the Author: ")
            choice = int(choice)
            author = Author.find_by_id(choice)
            if(author):
                new_first_name = input("\nEnter a new First Name for the Author: ")
                new_last_name = input("Enter a new Last Name for the Author: ")
                author.first_name = new_first_name
                author.last_name = new_last_name
                author.update()
                print("\nHere is the updated Author information: ")
                print(author)
                choice = input("\nPress 'return' to continue...")
                break
            else:
                print("\nAuthor Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except Exception as e:
            print("Invalid input! Try Again:", e)


def delete_author():
    while(True):
        try:
            choice = input("\nEnter an ID to Delete the Author: ")
            choice = int(choice)
            author = Author.find_by_id(choice)
            if(author):
                author.delete()
                print("\nAuthor has been deleted!")
                choice = input("\nPress 'return' to continue...")
                break
            else:
                print("\nAuthor Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again!")
        except:
            print("\nInvalid input! Try Again!")

def get_author_books():
    while(True):
        try:
            choice = input("\nEnter an ID to get the Books written by Author: ")
            choice = int(choice)
            author = Author.find_by_id(choice)
            if(author):
                print(f"\nHere are the books for Author #{author.id}:")
                print(author.books())
                choice = input("\n Press 'return' to continue...")
                break
            else:
                print("\nAuthor Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except:
            print("\nInvalid input! Try Again!")
            choice = input("\n Press 'return' to continue...")












def book_data():
    while True:
        book_menu()
        choice = input("Select an option from the menu: ")
        if(choice == "1"):
            get_book()
            break
        elif(choice == "2"):
            add_book()
            break
        elif(choice == "3"):
            update_book()
            break
        elif(choice == "4"):
            delete_book()
            break
        elif(choice == "5"):
            get_book_author()
            break
        elif(choice == "6"):
            get_all_reviews()
        elif(choice == "0"):
            break
        else:
            print("\nInvaild option! Please select from menu.")

        

def book_menu():
    print("\nBook Menu:")
    print("1: Retrieve Book Data")
    print("2: Add A Book")
    print("3: Update a Book")
    print("4: Delete a Book")
    print("5: Retrieve a Books author")
    print("6: Retrieve all Reviews for a Book")
    print("0: Back to Main Menu\n")

def get_book_menu():
    print("\nWould you like to get all the Books or just one?")
    print("1: Get All Books")
    print("2: Get Book By ID")
    print("3: Get Book By Title")
    print("0: Back to Book Menu\n")



def get_book():
    get_book_menu()
    choice = input("Select an option from the menu: ")

    while(True):
        if(choice == "1"):
            print("\n These are all the Books in our Library:")
            for book in Book.all:
                print(book)
            choice = input("\nPress 'return' to continue...")
            break
        elif(choice == "2"):
            while(True):
                try: 
                    choice = input("\nEnter ID to search for Book: ")
                    choice = int(choice)
                    book = Book.find_by_id(choice)
                    if(book):
                        print("\nHere is the Book specified by ID:")
                        print(Book.find_by_id(choice))
                        choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nBook Not Found!")
                        choice = input("Would you like to try again? Y/N: ")
                        if(choice == 'N'):
                            break
                        elif(choice == 'Y'):
                            None
                        else:
                            print("\nInvalid input! Try Again")
                except Exception as e:
                    print("\nInvalid input! Try Again:", e)
                    choice = input("\nPress 'return' to continue...")
            break
        elif(choice == "3"):
            while(True):
                try:
                    choice = input("\nEnter Title to search for Book: ")
                    choice = str(choice)
                    book = Book.find_by_title(choice)
                    if(book):
                        print("\nHere is the Book specified by Last Name:")
                        print(Book.find_by_title(choice))
                        choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nBook Not Found!")
                        choice = input("Would you like to try again? Y/N: ")
                        if(choice == 'N'):
                            break
                        elif(choice == 'Y'):
                             None
                        else:
                            print("\nInvalid input! Try Again")
                except Exception as e:
                    print("\nInvalid input! Try Again:", e)
                    choice = input("\nPress 'return' to continue...")
            break
        elif(choice == "0"):
            book_menu()
            choice = input("Select an option from the menu: ")
            break
        else:
            print("\nInvalid option! Please select option from menu.")

def add_book():
    title = input("\nEnter a Title for the New Book: ")
    author = input("Enter a named Author for the New Book: ")
    rating = input("Enter a Rating for the New Book: ")
    author_id = input("Enter a Author ID for the New Book: ")
    new_book = Book.create(title, author, rating, author_id)
    print("\nHere is the details for your new book: ")
    print(new_book)
    choice =  input("\nPress 'return' to continue...")


def update_book():
    while(True):
        try:
            choice = input("\nEnter ID to update the Book: ")
            choice = int(choice)
            book = Book.find_by_id(choice)
            if(book):
                new_title = input("\nEnter a Title for the Book: ")
                new_author = input("Enter a Author for the Book: ")
                new_genre = input("Enter a Genre for the Book: ")
                new_author_id = input("Enter an Author ID for the Book: ")
                new_author_id = int(new_author_id)
                book.title = new_title
                book.author = new_author
                book.genre = new_genre
                book.author_id = new_author_id
                book.update()
                print("\nHere is the updated Book: ")
                print(book)
                choice = input("\nPress 'return' to continue...")
                break
            else:
                print("\nBook Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except Exception as e:
            print("\nInvalid input! Try Again:", e)



def delete_book():
    while(True):
        try:
            choice = input("\nEnter an ID to Delete the Book: ")
            choice = int(choice)
            book = Book.find_by_id(choice)
            if(book):
                book.delete()
                print("\nBook has been deleted!")
                choice = input("\nPress 'return' to continue...")
                break
            else:
                print("\nBook Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except:
            print("\nInvalid input! Try Again!")
            choice = input("\nPress 'return' to continue...")




    
def get_book_author():
    while(True):
        try:
            choice = input("\nEnter an Book ID to get the Author of a Book: ")
            choice = int(choice)
            book = Book.find_by_id(choice)
            if(book):
                print(f"\nHere is the Author for Book #{book.id}:")
                print(f"\n{book.authors()}")
                choice = input("\n Press 'return' to continue...")
                break
            else:
                print("\nBook Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except:
            print("\nInvalid input! Try Again!")
            choice = input("\n Press 'return' to continue...")


def get_all_reviews():
    while(True):
        try:
            choice = input("\nEnter an Book ID to get the Reviews of a Book: ")
            choice = int(choice)
            book = Book.find_by_id(choice)
            if(book):
                print(f"\nHere is the Reviews for Book #{book.id}:")
                print(f"\n{book.reviews()}")
                choice = input("\n Press 'return' to continue...")
                break
            else:
                print("\nBook Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except Exception as e:
            print("\nInvalid input! Try Again:", e)
            choice = input("\n Press 'return' to continue...")










def review_data():
    while True:
        review_menu()
        choice = input("Select an option from the menu: ")
        if(choice == "1"):
            get_review()
            break
        elif(choice == "2"):
            add_review()
            break
        elif(choice == "3"):
            update_review()
            break
        elif(choice == "4"):
            delete_review()
            break
        elif(choice == "5"):
            reviews_book()
        elif(choice == "0"):
            break
        else:
            print("\nInvaild option! Please select from menu.")

        

def review_menu():
    print("\nReview Menu:")
    print("1: Retrieve Review Data")
    print("2: Add A Review")
    print("3: Update a Review")
    print("4: Delete a Review")
    print("5: Get the Book referred to in Review")
    print("0: Back to Main Menu\n")

def get_review_menu():
    print("\nWould you like to get all the Reviews or just one?")
    print("1: Get All Reviews")
    print("2: Get Review By ID")
    print("3: Get Review By Rating")
    print("0: Back to Review Menu\n")


def get_review():
    get_review_menu()
    choice = input("Select an option from the menu: ")

    while(True):
        if(choice == "1"):
            print("\n These are all the Reviews of Books in our Library:")
            print(Review.get_all())
            choice = input("\nPress 'return' to continue...")
            break
        elif(choice == "2"):
            while(True):
                try: 
                    choice = input("\nEnter ID to search for Review: ")
                    choice = int(choice)
                    review = Review.find_by_id(choice)
                    if(review):
                        print("\nHere is the Review specified by ID:")
                        print(Review.find_by_id(choice))
                        choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nReview Not Found!")
                        choice = input("Would you like to try again? Y/N: ")
                        if(choice == 'N'):
                            break
                        elif(choice == 'Y'):
                            None
                        else:
                            print("\nInvalid input! Try Again")
                except:
                    print("\nInvalid input! Try Again!")

            break
        elif(choice == "3"):
            while(True):
                try:
                    choice = input("\nEnter Rating to search for Review: ")
                    choice = int(choice)
                    review = Review.find_by_rating(choice)
                    if(review):
                        print("\nHere is the Review specified by a Rating: ")
                        print(Review.find_by_rating(choice))
                        choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nReview Not Found!")
                        choice = input("Would you like to try again? Y/N: ")
                        if(choice == 'N'):
                            break
                        elif(choice == 'Y'):
                            None
                        else:
                            print("\nInvalid input! Try Again")                  
                except Exception as e:
                    print("Invalid input! Try Again:", e)

            break
        elif(choice == "0"):
            review_menu()
            choice = input("Select an option from the menu: ")
            break
        else:
            print("\nInvalid option! Please select option from menu.")



def add_review():
    book_title = input("\nEnter a Title for the New Review: ")
    rating = input("Enter a Rating for the New Review: ")
    text = input("Enter a Text for the New Review: ")
    book_id = input("Enter a Book ID for the New Review: ")
    new_review = Review.create(book_title, rating, text, book_id)
    print("\nHere is the details for your new book: ")
    print(new_review)
    choice =  input("\nPress 'return' to continue...")


def update_review():
    while(True):
        try:
            choice = input("\nEnter ID to update the Review: ")
            choice = int(choice)
            review = Review.find_by_id(choice)
            if(review):
                new_book_title = input("\nEnter a Title for the Review: ")
                new_rating = input("Enter a Rating for the Review: ")
                new_rating = int(new_rating)
                new_text = input("Enter a Text for the Review: ")
                new_book_id = input("Enter a Book ID for the Review: ")
                new_book_id = int(new_book_id)
                review.book_title = new_book_title
                review.rating = new_rating
                review.text = new_text
                review.book_id = new_book_id
                review.update()
                print("\nHere is the updated Review: ")
                print(review)
                choice = input("\nPress 'return' to continue...")
                break
            else:
                print("\nReview Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except Exception as e:
            print("\nInvalid input! Try Again:", e)



def delete_review():
    while(True):
        try:
            choice = input("\nEnter an ID to Delete a Review: ")
            choice = int(choice)
            review = Review.find_by_id(choice)
            if(review):
                review.delete()
                print("\nReview has been deleted!")
                choice = input("\nPress 'return' to continue...")
                break
            else:
                print("\nReview Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except:
            print("\nInvalid input! Try Again!")


def reviews_book():
    while(True):
        try:
            choice = input("\nEnter an ID to get the Book of Review: ")
            choice = int(choice)
            review = Review.find_by_id(choice)
            if(review):
                print(f"\nHere is the Book referred to in Review #{review.id}:")
                print(review.book())
                choice = input("\n Press 'return' to continue...")
                break
            else:
                print("\nReview Not Found!")
                choice = input("Would you like to try again? Y/N: ")
                if(choice == 'N'):
                    break
                elif(choice == 'Y'):
                    None
                else:
                    print("\nInvalid input! Try Again")
        except:
            print("\nInvalid input! Try Again!")
            choice = input("\n Press 'return' to continue...")
            break