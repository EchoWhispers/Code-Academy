class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

     def get_author(self):
        return f"Author: {self.author}"

     def get_title(self):
        return f"Title: {self.title}"

     def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

book1 = Book("Pride and Prejudice", "Jane Austen (PP)")
book2 = Book("Hamlet", "William Shakespeare (H)")
book3 = Book("War and Peace", "Leo Tolstoy (WP)")


print(book1)
print(book2)
print(book3)