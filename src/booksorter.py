class BookSorter:
    @staticmethod
    @DeprecationWarning
    def selection_sort(books, key):
        """
        Sort the list of books using the Selection Sort algorithm.

        Parameters:
        - books (list): List of Book objects to sort
        - key (str): Attribute name (e.g., 'title', 'author', 'year', 'genre') used for sorting

        Returns:
        - List of books sorted based on the specified key
        """
        n = len(books)
        for i in range(n):
            # Assume the current position has the minimum value
            min_idx = i
            for j in range(i + 1, n):
                # Update min_idx if a smaller element is found
                if getattr(books[j], key) < getattr(books[min_idx], key):
                    min_idx = j
            # Swap the found minimum with the current position
            books[i], books[min_idx] = books[min_idx], books[i]
        return books

    @staticmethod
    def sort_books(books, key):
        """
        Quicksort implementation for sorting through the books in
        a bookshelf.

        Parameters:
        - books (list): List of Book objects to sort
        - key (str): Attribute name (e.g., 'title', 'author', 'year', 'genre') to sort books by

        Returns:
        - list of books sorted based on the specified key
        """
        # print("LENGBOOK", len(books))
        if len(books) < 2:
            # print("Tamo aqui")
            return books
        else:
            pivot = books[0]
            pivot_val = getattr(pivot, key)
            less = [i for i in books[1:] if getattr(i, key) <= getattr(pivot, key)]
            greater = [i for i in books[1:] if getattr(i, key) > getattr(pivot, key)]
            return BookSorter.sort_books(less, key) + [pivot] + BookSorter.sort_books(greater, key)
            # less = [i for i in arr[1:] if i <= pivot]
            # greater = [i for i in arr[1:] if i > pivot]
            # return quicksort(less) + [pivot] + quicksort(greater)
