''' LIBARY MANAGEMENT SYSTEM'''

# Creating a book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"You borrowed '{self.title}'."
        else:
            return f"'{self.title}' is already borrowed."
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"You returned '{self.title}'"
        else:
            return f"'{self.title}' was not borrowed."
 
class Library:
    def __init__(self):
        self.books = [] # List to hold book objects

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        return f"Book '{title}' added to library."
    
    def view_books(self):
        if not self.books:
            return "No books in the library"
        
        result = []
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            result.append(f"{book.title} by {book.author} ({book.year}) - {status}")
        return result
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow()
        return f"Book '{title}' not found in the library."
    
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Book '{title}' not found in the library."

# ------------  DEMO -------------
if __name__ == "__main__":   
    library = Library()
    
    print("\n Welcome To Bookshelf. ")
    print(library.add_book("Harry Potter", "J.k. Rowling", 1997))
    print(library.add_book("The Hobbit", "J.R.R. Tolkien", 1937))
    print(library.add_book("Things Fall Apart", "Chinua Achebe", 1958))

# Libary collection
    print("\n Library Collection")
    for book in library.view_books():     
        print(book)

# Borrowing
    print("\n ---- Borrowing ---- ")
    print(library.borrow_book('Harry Potter'))
    print(library.borrow_book("Harry Potter"))

# Returning
    print("\n --- Returning ---")
    print(library.return_book("Harry Potter"))
    print(library.return_book("Harry Potter"))

# Borrow book that doesn't exist
    print("\n --- Invalid borrow --- ")
    print(library.borrow_book("Unknown Book"))

# View status after borrowing/returning
    print("\n Final library Collection: ")
    for book in library.view_books():
        print(book)
