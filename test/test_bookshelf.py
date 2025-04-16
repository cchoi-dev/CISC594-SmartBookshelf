import sys
import os
from io import StringIO
from unittest.mock import patch

# Modifying PATH variable (only for duration of the script)
# to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from bookshelf import Book, Bookshelf

class TestBookshelf(unittest.TestCase):

    def test_add_book(self):
        shelf = Bookshelf()

        shelf.add_book(Book("Test", "Author", "Genre", 2023))
        shelf.add_book(Book("Harry Potter", "J.K", "Children", 1992))

        self.assertEqual(len(shelf.books), 2)
        self.assertEqual(shelf.books[0].title, "Test")
        self.assertEqual(shelf.books[0].author, "Author")
        self.assertEqual(shelf.books[0].genre, "Genre")
        self.assertEqual(shelf.books[0].year, 2023)
        self.assertEqual(shelf.books[1].title, "Harry Potter")
        self.assertEqual(shelf.books[1].author, "J.K")
        self.assertEqual(shelf.books[1].genre, "Children")
        self.assertEqual(shelf.books[1].year, 1992)

    def test_remove_book(self):
        shelf = Bookshelf()
        shelf.add_book(Book("Test", "Author", "Genre", 2023))
        shelf.add_book(Book("Harry Potter", "J.K", "Children", 1992))

        shelf.remove_book("Harry Potter")

        self.assertEqual(len(shelf.books), 1)
        self.assertEqual(shelf.books[0].title, "Test")
        self.assertEqual(shelf.books[0].author, "Author")
        self.assertEqual(shelf.books[0].genre, "Genre")
        self.assertEqual(shelf.books[0].year, 2023)

    def test_display_books(self):
        shelf = Bookshelf()
        shelf.books = [
            Book("Book A", "Author A", "Genre A", 2000),
            Book("Book B", "Author B", "Genre B", 2001)
        ]

        expected_output = (
            "Book A by Author A (Genre A, 2000)\n"
            "Book B by Author B (Genre B, 2001)\n"
        )

        with patch('sys.stdout', new=StringIO()) as fake_out:
            shelf.display_books()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()