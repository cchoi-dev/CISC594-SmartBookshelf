import unittest
from bookshelf import Book, Bookshelf
from booksorter import BookSorter

if __name__ == '__main__':
    shelf = Bookshelf()
    book1 = Book("My Book", "Name Namenson", "Horror", "1984")
    book2 = Book("El Libro", "Nombre Nombrado", "Horror", "2020")
    book3 = Book("Chek", "Yirum Sungham", "History", "2025")

    shelf.add_book(book1)
    shelf.add_book(book2)
    shelf.add_book(book3)

    print("Printing the shelf before sorting")
    shelf.display_books()

    BookSorter.selection_sort(shelf.books, 'title')
    print()
    print("Displaying the bookshelf after sorting by title")
    shelf.display_books()

    BookSorter.selection_sort(shelf.books, 'author')
    print()
    print("Displaying the bookshelf after sorting by author")
    shelf.display_books()

    BookSorter.selection_sort(shelf.books, 'genre')
    print()
    print("Displaying the bookshelf after sorting by genre")
    shelf.display_books()

    BookSorter.selection_sort(shelf.books, 'year')
    print()
    print("Displaying the bookshelf after sorting by year")
    shelf.display_books()
    pass
