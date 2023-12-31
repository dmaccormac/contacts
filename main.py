from book import *

# Examples

# view all contacts
book = Book()
print(book.view())

# add new contact
book.add("John", "Main Road 232", "(555) 1234", "john@example.com")
print(book.view())
