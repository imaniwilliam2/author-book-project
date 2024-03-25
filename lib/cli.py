# lib/cli.py

from helpers import (
    exit_program,
    author_data, 
    initalization,
    book_data
)


def main():
    initalization()

    while True:
        menu()
        choice = input("Select an option from the menu: ")
        if (choice == "1"):
            author_data()
        elif choice == "2":
            book_data()
        elif(choice == "0"):
            exit_program()
        else:
            print("Invalid option! Please choose from menu!\n")


def menu():
    print("\nWelcome to the Library Database!\n")
    print("Main Menu:")
    print("1: Access the Author data")
    print("2: Access the Book data")
    print("0: Exit the Library\n")


if __name__ == "__main__":
    main()
