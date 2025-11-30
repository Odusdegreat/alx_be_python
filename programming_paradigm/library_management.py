class Book:
    """Represents a book in the library with title, author, and availability status."""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """
        Check if the book is available.
        
        Returns:
            bool: True if available, False if checked out
        """
        return not self._is_checked_out


class Library:
    """Manages a collection of books in the library."""
    
    def __init__(self):
        """Initialize the Library with an empty collection of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): An instance of the Book class
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book from the library by title.
        
        Args:
            title (str): The title of the book to check out
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available or does not exist.")
    
    def return_book(self, title):
        """
        Return a book to the library by title.
        
        Args:
            title (str): The title of the book to return
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out or does not exist.")
    
    def list_available_books(self):
        """Display all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")