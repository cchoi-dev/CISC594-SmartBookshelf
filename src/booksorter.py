class BookSorter:
    @staticmethod
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