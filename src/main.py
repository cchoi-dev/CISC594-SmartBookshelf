from bookshelf import Book, Bookshelf
from booksorter import BookSorter


def demo():
    shelf = Bookshelf()
    book1 = Book("My Book", "Name Namenson", "Horror", "1984")
    book2 = Book("El Libro", "Nombre Nombrado", "Horror", "2020")
    book3 = Book("Chek", "Yirum Sungham", "History", "2025")

    shelf.add_book(book1)
    shelf.add_book(book2)
    shelf.add_book(book3)

    print("Printing the shelf before sorting")
    shelf.display_books()

    shelf.books = BookSorter.sort_books(shelf.books, 'title')
    print()
    print("Displaying the bookshelf after sorting by title")
    shelf.display_books()

    shelf.books = BookSorter.sort_books(shelf.books, 'author')
    print()
    print("Displaying the bookshelf after sorting by author")
    shelf.display_books()

    shelf.books = BookSorter.sort_books(shelf.books, 'genre')
    print()
    print("Displaying the bookshelf after sorting by genre")
    shelf.display_books()

    shelf.books = BookSorter.sort_books(shelf.books, 'year')
    print()
    print("Displaying the bookshelf after sorting by year")
    shelf.display_books()

def main():
    bookshelf = Bookshelf()

    while True:
        print("Smart Bookshelf Organizer")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Display Books")
        print("4. Sort Books")
        print("5. Demo Run")
        print("5. Exit")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                # Collect book details from user input
                title = input("Enter book title: ")
                author = input("Enter author: ")
                genre = input("Enter genre: ")
                year = input("Enter publication year: ")

                # Add the new book to the bookshelf
                bookshelf.add_book(Book(title, author, genre, year))
                print("Book added!")

            case "2":
                # Ask for the title of the book to remove
                title = input("Enter the title of the book to remove: ")

                # Remove the book by title
                bookshelf.remove_book(title)
                print("Book removed!")

            case "3":
                # Display all books currently on the shelf
                print("Your Bookshelf:")
                bookshelf.display_books()

            case "4":
                # Ask the user which attribute to sort the books by
                print("Sort by: (title/author/genre/year)")
                key = input("Enter sorting criteria: ")

                # Use bubble sort to sort books by the selected attribute
                # bookshelf.books = Sorting.bubble_sort(bookshelf.books, key) # TODO Uncomment when ready to implement
                print("Books sorted!")

            case "5":
                # Running demo run of project
                print("Running demo!")
                demo()

            case "6":
                print("Exiting Program...")
                break
            case _:
                print("Invalid option: ", choice)
                print("Valid inputs include: [1-5]")


if __name__ == '__main__':
    main()
    exit()
