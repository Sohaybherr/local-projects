class book:
    def __init__(self,title,author,year,available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {'Available' if self.available else 'Not Available'}"
class library:
    def __init__(self): 
        self.books = [] 
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")
    def remove_book(self, book):
        self.books.remove(book)
        print(f"Removed book: {book.title}")
    def display_books(self):
        for book in self.books:
            print(book.__str__())   
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You have borrowed '{title}'")
                return
        print(f"Sorry, '{title}' is not available.")
    def return_book(self,title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You have returned '{title}'")
                return
        print(f"'{title}' was not borrowed from this library.")
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write("Books in Library:\n")
            for book in self.books:
                file.write(book.__str__() + "\n")  
        print("Library saved to file.")
    def load_from_file(self, filename):
        self.books = []
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                t=line.strip().split(" - ")
                v=t[0].split(" by ")
                if t[1]=="Available":
                    available=True
                else:
                    available=False
                title=v[0]
                w=v[1].split(" (")
                author=w[0]
                year=w[1].strip(")")

                Book = book(title, author, year, available)
                self.add_book(Book)
            
        print("Library loaded from file.")
# Example usage:
library_instance = library()
library_instance.load_from_file("exam.txt") 
print("#"*20)      
library_instance.display_books()
print("#"*20)
library_instance.borrow_book("1984") 
print("#"*20)
library_instance.save_to_file("exam.txt")
library_instance.load_from_file("exam.txt")
print("#"*20)
library_instance.display_books()