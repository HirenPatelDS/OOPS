class Book:
    """
    A simple Book class to demonstrate the use of magic (dunder) methods.
    """

    def __init__(self, title, author, pages):
        """
        Constructor: Automatically called when you create a new Book object.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Called when you print the object. Returns a user-friendly string.
        """
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        """
        Called when you use len() on the object. Returns number of pages.
        """
        return self.pages

    def __add__(self, other):
        """
        Called when you use the + operator between two Book objects.
        Returns the total number of pages.
        """
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented


# Create two book objects
book1 = Book("Python Basics", "Hiren", 200)
book2 = Book("OOP in Python", "Khushbu", 150)

# Use __str__()
print(book1)  # Output: 'Python Basics' by Hiren

# Use __len__()
print(len(book1))  # Output: 200

# Use __add__()
total_pages = book1 + book2
print(f"Total pages: {total_pages}")  # Output: Total pages: 350
