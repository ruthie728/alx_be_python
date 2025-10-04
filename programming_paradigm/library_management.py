class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    # ADD THIS METHOD:
    def is_available(self):
        """Public method to check availability without exposing private attribute"""
        return not self._is_checked_out

    # ADD THIS METHOD:
    def __str__(self):
        """String representation for consistent formatting"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"You have checked out '{title}'.")
                    return
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
       
        for book in self._books:
             if book.is_available():
                print(book)  