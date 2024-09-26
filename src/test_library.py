import unittest
from library import Book,Library

class Library_Testing(unittest.TestCase):
    def setUp(self):
        self.Library = Library()

    def test_addbooks(self):
        book = Book(isbn="23-978-5163-389",title="Object Oriented Programing in Java",author="Rick Halterman",publicationYear=2013)
        self.Library.addbook(book)
        self.assertIn(book,self.Library.books)
        
    def test_borrowbook(self):
        book = Book(isbn="23-978-5163-389",title="Object Oriented Programing in Java",author="Rick Halterman",publicationYear=2013)
        self.Library.addbook(book)
        self.Library.borrowbook("23-978-5163-389")
        self.assertFalse(book.available)
        
    def test_borrow_unavailable_book(self):
        book = Book(isbn="23-978-5163-389",title="Object Oriented Programing in Java",author="Rick Halterman",publicationYear=2013)
        self.Library.addbook(book)
        self.Library.borrowbook("23-978-5163-389")
        with self.assertRaises(Exception) as message:
            self.Library.borrowbook("23-978-5163-389")
        self.assertTrue('Book Not Available' in str(message.exception))
        
    def test_returnbook(self):
        book = Book(isbn="23-978-5163-389",title="Object Oriented Programing in Java",author="Rick Halterman",publicationYear=2013)
        self.Library.addbook(book)
        self.Library.borrowbook("23-978-5163-389")
        self.Library.returnbook("23-978-5163-389")
        self.assertTrue(book.available)
        
    def test_view_available_books(self):
        book1 = Book(isbn="12-231-978-5163-389",title="Data Structure Using CPP",author="Amit Verma",publicationYear=2015)
        book2 = Book(isbn="23-978-5163-389", title="Object Oriented Programing in Java", author="Rick Halterman", publicationYear=2013)
        self.Library.addbook(book1)
        self.Library.addbook(book2)
        self.Library.borrowbook("23-978-5163-389")
        available_books = self.Library.view_availablebooks()
        self.assertIn(book1, available_books) 
        self.assertNotIn(book2, available_books) 



        
if __name__ == '__main__':
    unittest.main()