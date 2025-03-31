import sys
import os

# Modifying PATH variable (only for duration of the script)
# to include the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from bookshelf import Book, Bookshelf

class TestBookshelf(unittest.TestCase):
    def test_add_book(self):
        shelf = Bookshelf()
        shelf.add_book(Book("Test", "Author", "Genre", 2023))
        self.assertEqual(len(shelf.books), 1)

if __name__ == '__main__':
    unittest.main()