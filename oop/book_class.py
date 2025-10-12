class Book:
    # Constructor: initializes the attributes
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor: prints a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation (user-friendly)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation (developer/debug-friendly)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"