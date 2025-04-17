import sys
import os
from unittest.mock import patch
import unittest

# Modifying PATH variable (only for duration of the script)
# to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from bookshelf import Book, Bookshelf
from booksorter import BookSorter

class TestBooksorter(unittest.TestCase):

    def util_check_bookshelfs_equal(self, shelf1_books, shelf2_books):
        if len(shelf1_books) != len(shelf2_books):
            print("Error - shelf lenghts dont match")
            return False

        for index, value in enumerate(shelf1_books):
            if value != shelf2_books[index]:
                return False
        return True


    def test_sort_empty_shelf(self):
        shelf = Bookshelf()
        sorted_books = BookSorter.sort_books(shelf.books, 'title')
        self.assertEqual(len(shelf.books), 0)
        self.assertEqual(shelf.books, sorted_books)
        sorted_books = BookSorter.sort_books(shelf.books, 'author')
        self.assertEqual(len(shelf.books), 0)
        self.assertEqual(shelf.books, sorted_books)
        sorted_books = BookSorter.sort_books(shelf.books, 'genre')
        self.assertEqual(len(shelf.books), 0)
        self.assertEqual(shelf.books, sorted_books)
        sorted_books = BookSorter.sort_books(shelf.books, 'year')
        self.assertEqual(len(shelf.books), 0)
        self.assertEqual(shelf.books, sorted_books)


    def test_sort_single_book(self):
        shelf = Bookshelf()
        shelf.add_book(Book("TestTitle", "Test Author", "TestGenre", "2020"))
        sorted_books = BookSorter.sort_books(shelf.books, 'title')
        self.assertEqual(len(shelf.books), 1)
        self.assertEqual(shelf.books, sorted_books)
        sorted_books = BookSorter.sort_books(shelf.books, 'author')
        self.assertEqual(len(shelf.books), 1)
        self.assertEqual(shelf.books, sorted_books)
        sorted_books = BookSorter.sort_books(shelf.books, 'genre')
        self.assertEqual(len(shelf.books), 1)
        self.assertEqual(shelf.books, sorted_books)
        sorted_books = BookSorter.sort_books(shelf.books, 'year')
        self.assertEqual(len(shelf.books), 1)
        self.assertEqual(shelf.books, sorted_books)


    def test_sort_books_by_title(self):
        shelf = Bookshelf()
        book1 = Book("My Book", "Name Namenson", "Horror", "1984")
        book2 = Book("El Libro", "Nombre Nombrado", "Horror", "2020")
        book3 = Book("Chek", "Yirum Sungham", "History", "2025")
        shelf.add_book(book1)
        shelf.add_book(book2)
        shelf.add_book(book3)

        self.assertTrue(self.util_check_bookshelfs_equal([book1, book2, book3], shelf.books))
        books_original_order = shelf.books
        sorted_books = BookSorter.sort_books(shelf.books, "title")
        self.assertTrue(self.util_check_bookshelfs_equal([book3, book2, book1], sorted_books))
        self.assertFalse(self.util_check_bookshelfs_equal(books_original_order, sorted_books))


    def test_sort_books_by_author(self):
        shelf = Bookshelf()
        book1 = Book("El Libro", "Nombre Nombrado", "Horror", "2020")
        book2 = Book("My Book", "Name Namenson", "Horror", "1984")
        book3 = Book("Chek", "Yirum Sungham", "History", "2025")
        shelf.add_book(book1)
        shelf.add_book(book2)
        shelf.add_book(book3)

        self.assertTrue(self.util_check_bookshelfs_equal([book1, book2, book3], shelf.books))
        books_original_order = shelf.books
        sorted_books = BookSorter.sort_books(shelf.books, "author")
        self.assertTrue(self.util_check_bookshelfs_equal([book2, book1, book3], sorted_books))
        self.assertFalse(self.util_check_bookshelfs_equal(books_original_order, sorted_books))


    def test_sort_books_by_genre(self):
        shelf = Bookshelf()
        book1 = Book("My Book", "Name Namenson", "Science-Fiction", "1984")
        book2 = Book("El Libro", "Nombre Nombrado", "Horror", "2020")
        book3 = Book("Chek", "Yirum Sungham", "History", "2025")
        shelf.add_book(book1)
        shelf.add_book(book2)
        shelf.add_book(book3)

        self.assertTrue(self.util_check_bookshelfs_equal([book1, book2, book3], shelf.books))
        books_original_order = shelf.books
        sorted_books = BookSorter.sort_books(shelf.books, "genre")
        self.assertTrue(self.util_check_bookshelfs_equal([book3, book2, book1], sorted_books))
        self.assertFalse(self.util_check_bookshelfs_equal(books_original_order, sorted_books))


    def test_sort_books_by_year(self):
        shelf = Bookshelf()
        book1 = Book("My Book", "Name Namenson", "Horror", "1984")
        book2 = Book("Chek", "Yirum Sungham", "History", "2025")
        book3 = Book("El Libro", "Nombre Nombrado", "Horror", "2020")
        shelf.add_book(book1)
        shelf.add_book(book2)
        shelf.add_book(book3)

        self.assertTrue(self.util_check_bookshelfs_equal([book1, book2, book3], shelf.books))
        books_original_order = shelf.books
        sorted_books = BookSorter.sort_books(shelf.books, "year")
        self.assertTrue(self.util_check_bookshelfs_equal([book1, book3, book2], sorted_books))
        self.assertFalse(self.util_check_bookshelfs_equal(books_original_order, sorted_books))


if __name__=='__main__':
    unittest.main()
