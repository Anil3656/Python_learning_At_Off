from Book import Book
from Library_Member import LibraryMember

# Create books
book1 = Book("1984", "George Orwell", "Fiction")
book2 = Book("A Brief History of Time", "Stephen Hawking", "Science")
book3 = Book("Sapiens", "Yuval Noah Harari", "Non-Fiction")
book4 = Book("The Selfish Gene", "Richard Dawkins", "Science")
book5 = Book("World War1", "Rutherford", "History")
book6 = Book("Mahabharata", "Thikkana", "History")


# Scenario 1: Student Member Borrowing
student1 = LibraryMember("Karthik", 101, "Student")

print(student1.borrow_book(book1))  # OK
#print(student1.borrow_book(book2))  # OK
#print(student1.borrow_book(book3))  # OK
#print(student1.borrow_book(book4))  # Exceeds limit

#returning the Borrowed books
#print(student1.return_book(book1))
#print(student1.return_book(book4))

# Try borrowing already borrowed book
#print(student1.borrow_book(book1))  # Book is already borrowed by Karthik.
#(student1.borrow_book(book2))  # Book is already borrowed by Karthik.
#print(student1.borrow_book(book3))



student2 = LibraryMember("Ganesh", 102, 'Student')
#print(student2.borrow_book(book1))
#print(student2.return_book(book1))
#print(student2.member_type)
#print(student2.get_borrowed_books())
#print(student2.borrow_book(book5))
#print(student2.get_borrowed_books())


# Scenario 2: Faculty Member Borrowing and Returning

faculty1 = LibraryMember("Rahul", 401, "Faculty")
print(faculty1.borrow_book(book1))  # OK
#print(faculty1.return_book(book4))  # Returned
#print(faculty1.return_book(book3))  # Doesn't have it
#print(faculty1.borrow_book(book1))


faculty2 = LibraryMember("Ravi", 402, "Faculty")
print(faculty2.borrow_book(book2))  # OK
#print(faculty2.return_book(book4))  # Returned
#print(faculty2.return_book(book3))  # Doesn't have it
#print(faculty2.borrow_book(book1))

# Scenario 3: Invalid Book Category Checking
try:
    invalid_book = Book("Mystery of Time", "Unknown", "Mystery")  # Invalid category
except ValueError as e:
    print(f'\n{e}')


# Display statistics
print(f"\n{student1.name}'s borrowed books: {student1.get_borrowed_books()}")
print(f"\n {student2.name}'s borrowed books: {student2.get_borrowed_books()}")
print(f"\n{faculty1.name}'s borrowed books: {faculty1.get_borrowed_books()}")
print(f"\n{faculty2.name}'s borrowed books: {faculty2.get_borrowed_books()}")

print(f"\nTotal members registered In Library: {LibraryMember.get_total_members()}")  #Total member Registered
print(Book.number_of_books()) #It shows the number of books in Library
print(Book.total_books()) #It shows the title of all books in Library
print(LibraryMember.not_borrowed_number()) #Not borrowed books in Library
print((LibraryMember.not_borrowed_books()))  #It shows not borrowed book in Library

#(f"\nTotal books created: {Book.get_total_books()}")
