class Book:
    total_Books = 0
    total_books_list = []
    valid_categories = ["Fiction", "Non-Fiction", "Science",'History']

    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = False
        Book.total_books_list.append(self)
        #Book.total_books_list.append({'title' : self.title, 'author' : self.author, 'category' : self.category, 'borrowed' : self.is_borrowed})
        #print(type(Book.total_books))
        Book.total_Books += 1
        if not Book.is_valid_category(category):
            raise ValueError(f"Invalid category: {category}")

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
        return cls.total_Books

    @classmethod
    def total_books(cls):
        return f'List of Total Books: {[
            {
                "title": book.title,
                "author": book.author,
                "category": book.category,
                "is_borrowed": book.is_borrowed
            }
            for book in cls.total_books_list
        ]}'

    @classmethod
    def number_of_books(cls):
        return f'Number of Books Count: {len(cls.total_books_list)}'

    @staticmethod
    def is_valid_category(category):
        return category in Book.valid_categories