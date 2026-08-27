# Library Book Management System using OOP

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.category = self.assign_category()

    def assign_category(self):
        if self.price >= 500:
            return "Premium"
        else:
            return "Standard"

    def display(self):
        print("Book ID :", self.book_id)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)
        print("Category :", self.category)
        print("----------------------------")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nLibrary Book Records")
            print("==========================")
            for book in self.books:
                book.display()

# Main Program
library = Library()

n = int(input("Enter number of books: "))

for i in range(n):
    print(f"\nEnter details of Book {i + 1}")

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    price = float(input("Enter Price: "))

    b = Book(book_id, title, author, price)
    library.add_book(b)
library.display_books()