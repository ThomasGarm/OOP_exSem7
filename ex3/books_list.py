# coding: utf8

books_list = [
    ['Katinka', ['page1', 'page2', 'page3', 'page4', 'page5']],
    ['La légende de Gösta Berling', ['page1', 'page2', 'page3', 'page4', 'page5']],
    ['Le père Goriot', ['page1', 'page2', 'page3', 'page4', 'page5']],
    ['Harry Poter', ['page1', 'page2', 'page3', 'page4', 'page5']],
    ['La nuit des temps', ['page1', 'page2', 'page3', 'page4', 'page5']],
    ['Les pensées', ['page1', 'page2', 'page3', 'page4', 'page5']]
]


def add_book(book):
    book = books_list
    for i in book:
        title = i[0]
        for j in i:
            pages = j[0::]
    return title, pages
                


book = books_list
print(add_book(book))