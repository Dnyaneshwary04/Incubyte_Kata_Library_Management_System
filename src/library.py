class Book:
    def __init__(self,isbn,title,author,publicationYear) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
        self.available  = True

class Library:
    def __init__(self):
        self.books = []

    def addbook(self,book):
        self.books.append(book)
