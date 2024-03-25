# lib/helpers.py

from models.author import Author
from models.book import Book


def initalization():
    Author.create_table()
    Book.create_table()

    Author.get_all()
    Book.get_all()


def exit_program():
    print("Happy Reading! Goodbye!")
    exit()

def author_data():
    while(True):
        author_menu()
        choice = input("Select an option from the menu:")
        if(choice == "1"):
            create_author()
            break
        elif(choice == "2"):
            get_author()
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
        else:
            print("Invalid option! Please choose from menu.\n")




def author_menu():
    print("\nAuthor Menu:")
    print("1: Create New Author")
    print("2: Retrieve Author Data")
    print("3: Update an Author")
    print("4: Delete an Author")
    print("5: Retrieve an Author's books\n")

def create_author():
    first_name = input("Enter a first name for the new author: ")
    last_name = input("Enter a last name for the new author: ")
    new_author = Author.create(first_name, last_name)
    print("Here is the detail for your new author: ")
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
                    else:
                        print("\nAuthor Not Found!")
                    choice = input("\nPress 'return' to continue...")
                    break
                except:
                    print("Invalid input! Try Again!")

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
                    else:
                        print("\nAuthor Not Found!")
                    choice = input("\nPress 'return' to continue...")
                    break
                except:
                    print("Invalid input! Try Again!")

            break
        else:
            print("Invalid option! Please choose from menu.")



def get_author_menu():
    print("\nWould you like to get all authors or just one?")
    print("1: Get All Authors")
    print("2: Get One Author By ID")
    print("3: Get One Author By Last Name")

def update_author():
    while(True):
        try:
            choice = input("\nEnter ID to update the Author: ")
            choice = int(choice)
            author = Author.find_by_id(choice)
            if(author):
                new_first_name = input("Enter a new First Name for the Author: ")
                new_last_name = input("Enter a new Last Name for the Author: ")
                author.first_name = new_first_name
                author.last_name = new_last_name
                author.update()
                print("The Author has been updated: ")
                print(author)
                choice = input("\nPress 'return' to continue...")
            else:
                print("\nAuthor Not Found!")
            break
        except:
            print("Invalid input! Try Again!")


def delete_author():
    while(True):
        try:
            choice = input("\nEnter an ID to Delete the Author: ")
            choice = int(choice)
            author = Author.find_by_id(choice)
            if(author):
                author.delete()
                print("Author has been deleted!")
            else:
                print("\nAuthor Not Found!")
            break
        except:
            print("Invalid input! Try Again!")

def get_author_books():
    while(True):
        try:
            choice = input("\nEnter an ID to get the Books written by Author: ")
            choice = int(choice)
            author = Author.find_by_id(choice)
            if(author):
                print(f"\nHere are the books for Author #{author.id}:")
                print(author.books())
            else:
                print("\nAuthor Not Found!")
            choice = input("\n Press 'return' to continue...")
            break
        except:
            print("Invalid input! Try Again!")


def book_data():
    print("You have entered the book data")