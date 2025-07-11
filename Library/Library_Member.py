from Book import Book

class LibraryMember:
    total_members = 0
    total_members_list = []

    def __init__(self, name, member_id, member_type):
        self.name = name
        self.member_id = member_id
        self.member_type = member_type
        self.borrowed_books = []
        LibraryMember.total_members_list.append(self)
        LibraryMember.total_members += 1


    def borrow_book(self, book):
        if len(self.borrowed_books) >= LibraryMember.max_books_allowed(self.member_type):
            return f"{self.name} has reached the borrowing limit."
        if book.is_borrowed:
            for member in LibraryMember.total_members_list:
                if book in member.borrowed_books:
                    return f"{book.title} is already borrowed by {member.name}."
            return f"{book.title} is already borrowed."
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
        return f'{[book.title for book in self.borrowed_books]}'


    @staticmethod
    def not_borrowed_books():
        not_borrowed = [
            {
                "title": book.title,
                "author": book.author,
                "category": book.category,
                "is_borrowed": book.is_borrowed
            }
            for book in Book.total_books_list if not book.is_borrowed
        ]
        return f'List of Not Borrowed Books: {not_borrowed}'

    @classmethod
    def get_total_members(cls):
        return cls.total_members

    @staticmethod
    def max_books_allowed(member_type):
        limits = {"Student": 3, "Faculty": 5}
        return limits.get(member_type, 0)

    @classmethod
    def not_borrowed_number(cls):
        return f"Not Borrowed Books Count: {len(cls.total_members_list)}"