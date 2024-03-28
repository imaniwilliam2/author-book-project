# lib/cli.py

from helpers import (
    exit_program,
    author_data, 
    initalization,
    book_data,
    review_data
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
        elif(choice == "3"):
            review_data()
        else:
            print("\nInvalid option! Please select from menu!")
            choice = input("\nPress 'return' to continue...")



def menu():
    print("\nWelcome to the Literary Locator Database!\n")
    print("Main Menu:")
    print("1: Access Author Data")
    print("2: Access Book Data")
    print("3: Access Review Data")
    print("0: Exit the Library\n")


if __name__ == "__main__":
    main()
