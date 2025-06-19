'''from oops import Employee

class Anil(Employee):
    def __init__(self, name, Id, salary):
        super().__init__(name, Id, salary)
    def task(Anil):
        print('Task is Given!')

anil = Anil("Aneel",401,5000)
anil.task()'''

class Book:
    total_books = 0
    valid_categories = ["Fiction", "Non-Fiction", "Science"]

    def __init__(self, title, author, category):
        if not Book.is_valid_category(category):
            raise ValueError(f"Invalid category: {category}")
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = False
        Book.total_books += 1

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.title}' has been borrowed."
        return f"'{self.title}' is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.title}' has been returned."
        return f"'{self.title}' was not borrowed."

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_category(category):
        return category in Book.valid_categories


class LibraryMember:
    total_members = 0

    def __init__(self, name, member_id, member_type):
        self.name = name
        self.member_id = member_id
        self.member_type = member_type
        self.borrowed_books = []
        LibraryMember.total_members += 1

    def borrow_book(self, book):
        if len(self.borrowed_books) >= LibraryMember.max_books_allowed(self.member_type):
            return f"{self.name} has reached the borrowing limit."
        if book.is_borrowed:
            return f"{book.title} is already borrowed by someone else."
        book.borrow_book()
        self.borrowed_books.append(book)
        return f"{self.name} borrowed '{book.title}'."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}'."
        return f"{self.name} does not have '{book.title}'."

    def get_borrowed_books(self):
        return [book.title for book in self.borrowed_books]

    @classmethod
    def get_total_members(cls):
        return cls.total_members

    @staticmethod
    def max_books_allowed(member_type):
        limits = {"Student": 3, "Faculty": 5}
        return limits.get(member_type, 0)

# Create books
book1 = Book("1984", "George Orwell", "Fiction")
book2 = Book("A Brief History of Time", "Stephen Hawking", "Science")
book3 = Book("Sapiens", "Yuval Noah Harari", "Non-Fiction")
book4 = Book("The Selfish Gene", "Richard Dawkins", "Science")

# Scenario 1: Student Member Borrowing
student = LibraryMember("Alice", 101, "Student")
print(student.borrow_book(book1))  # OK
print(student.borrow_book(book2))  # OK
print(student.borrow_book(book3))  # OK
print(student.borrow_book(book4))  # Exceeds limit

# Try borrowing already borrowed book
print(student.borrow_book(book1))  # Already borrowed

# Scenario 2: Faculty Member Borrowing and Returning
faculty = LibraryMember("Dr. Bob", 202, "Faculty")
print(faculty.borrow_book(book4))  # OK
print(faculty.return_book(book4))  # Returned
print(faculty.return_book(book3))  # Doesn't have it

# Scenario 3: Invalid Book Category
try:
    invalid_book = Book("Mystery of Time", "Unknown", "Mystery")  # Invalid category
except ValueError as e:
    print(e)

# Display statistics
print(f"Total books created: {Book.get_total_books()}")
print(f"Total members registered: {LibraryMember.get_total_members()}")

print(f"{student.name}'s borrowed books: {student.get_borrowed_books()}")
print(f"{faculty.name}'s borrowed books: {faculty.get_borrowed_books()}")
