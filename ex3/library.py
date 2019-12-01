


from book import *

from books_list import *

class Library():
    
    def __init__(self, books_list):
        self.title = None
        self.pages = None
        for i in books_list:
            if hasattr(self, i):
                setattr(self, i)
        

        

    def add_book(self, book):
        book = books_list
        for i in book:
            title = i[0]
        for j in i:
            pages = j[0::]
        return title, pages

        

    def get_book(self, title):
        title = input("Choose your book")
        return title
