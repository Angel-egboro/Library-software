import json

# Function to load library data from a file
def load_library():
    try:
        with open('library.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save library data to a file
def save_library(library_data):
    with open('library.json', 'w') as file:
        json.dump(library_data, file)

# Function to display the library menu
def display_menu(): 
    print("1. Add A Book")
    print("2. Display All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

# Function to add a book to the library
def add_book(library_data):
    book_title = input("Enter book title: ")
    author = input("Enter author's name: ")
    isbn = input("Enter ISBN: ")
    library_data[isbn] = {"title": book_title, "author": author, "available": True}
    print("The Book has been added successfully!")

# Function to display all books in the library
def display_all_books(library_data):
    for isbn, book in library_data.items():
        print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Available: {book['available']}")

# Function to borrow a book
def borrow_book(library_data):
    isbn = input("Enter ISBN of the book you want to borrow: ")
    if isbn in library_data:
        if library_data[isbn]["available"]:
            library_data[isbn]["available"] = False
            print("Book borrowed successfully!")
        else:
            print("Sorry, the book is already borrowed.")
    else:
        print("Book not found in the library.")

# Function to return a book
def return_book(library_data):
    isbn = input("Enter ISBN of the book you want to return: ")
    if isbn in library_data:
        if not library_data[isbn]["available"]:
            library_data[isbn]["available"] = True
            print("Book returned successfully!")
        else:
            print("The book is already in the library.")
    else:
        print("Book not found in the library.")

# Function to search for a book
def search_book(library_data):
    search_term = input("Enter book title, author, or ISBN to search: ")
    found_books = []
    for isbn, book in library_data.items():
        if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower() or search_term == isbn:
            found_books.append(book)
    if found_books:
        for book in found_books:
            print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Available: {book['available']}")
    else:
        print("No matching books found in the library.")

# Main function to manage the library
def main():
    library_data = load_library()

    while True:
        print("WELCOME USER!")
        display_menu()
        choice = input("please select an option from (1-6): ")

        if choice == "1":
            add_book(library_data)
        elif choice == "2":
            display_all_books(library_data)
        elif choice == "3":
            borrow_book(library_data)
        elif choice == "4":
            return_book(library_data)
        elif choice == "5":
            search_book(library_data)
        elif choice == "6":
            save_library(library_data)
            print("Library data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    print("Hello World")