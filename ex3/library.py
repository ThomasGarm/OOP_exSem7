


from book import *

from books_list import *

class Library():
    
    def __init__(self):
        self.books_list = []
        

    def add_book(self, book):
        self.books_list.append(book)

        

    def get_book(self, title):
        title = input("choose a book")
        for title in self.books_list :
            if title == Book.title :
                return book
        return None
