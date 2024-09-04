# Write a function that takes a list of dictionaries representing books, each with keys for 'title' and 'author', and returns the list sorted by author's name.

# Enter number of books: 3
# Enter book title: To Kill a Mockingbird
# Enter author name: Harper Lee
# Enter book title: 1984
# Enter author name: George Orwell
# Enter book title: The Great Gatsby
# Enter author name: F. Scott Fitzgerald
def libary():

    books = []
    nr_books = int(input("Enter number of books you want to add: "))
    i = 0

    while i < nr_books:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        combined = title + ", " + "Author: " + author
        books.append(combined)
        i += 1
    return books

print(f" Sorted books:",libary())


