
class Book:
    """Book class that stores basic information about a book."""

    def __init__(self, title, author, genre, year):
        # Initialize a Book object with title, author, genre, and publication year
        self.title = title      # Title of the book
        self.author = author    # Author of the book
        self.genre = genre      # Genre of the book (e.g., Fiction, Non-Fiction)
        self.year = year        # Year the book was published

    def __str__(self):
        # Return a formatted string representation of the book
        return f"{self.title} by {self.author} ({self.genre}, {self.year})"


class Bookshelf:
    """Bookshelf class that represents a collection of books."""

    def __init__(self):
        # Initialize an empty list to store Book objects
        self.books = []

    def add_book(self, book):
        """
        Add a book to the bookshelf.

        Parameters:
        - book (Book): A Book object to be added to the shelf
        """
        self.books.append(book)

    def remove_book(self, title):
        """
        Remove a book from the bookshelf by its title.

        Parameters:
        - title (str): The title of the book to remove

        Note: If multiple books have the same title, all will be removed.
        """
        self.books = [book for book in self.books if book.title != title]

    def display_books(self):
        """
        Print all books currently stored on the bookshelf.

        Each book is displayed using its string representation.
        """
        for book in self.books:
            print(book)
