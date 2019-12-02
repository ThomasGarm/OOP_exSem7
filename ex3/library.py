


from book import *

from books_list import *

class Library():
    
    def __init__(self):
        self.books = []
        

    def add_book(self, book):
        self.books.append(book)

        

    def get_book(self, title):
        for book in self.books:
            if title == book.title :
               return book
        raise Exception("not here")
