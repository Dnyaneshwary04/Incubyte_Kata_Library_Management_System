import unittest
from library import Book,Library

class Library_Testing(unittest.TestCase):
    def setUp(self):
        self.Library = Library()

    def test_addbooks(self):
        book = Book(isbn="23-978-5163-389",title="Object Oriented Programing in Java",author="Rick Halterman",publicationYear=2013)
        self.Library.addbook(book)
        self.assertIn(book,self.Library.books)
        
    def test_borrow_book(self):
        book = Book(isbn="23-978-5163-389",title="Object Oriented Programing in Java",author="Rick Halterman",publicationYear=2013)
        self.Library.addbook(book)
        self.Library.borrowbook("23-978-5163-389")
        self.assertFalse(book.available)
        
if __name__ == '__main__':
    unittest.main()