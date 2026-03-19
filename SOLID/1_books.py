class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} from {self.author}"


class Library:
    def __init__(self, *args):
        self.books = list(args)

    def find_book(self, title):
        try:
            return [el for el in self.books if el.title == title][0]
        except IndexError:
            return "Book not found"

b1 = Book("title", "author")
b2 = Book("title2", "author2")
b3 = Book("title3", "author3")

lib = Library(b1, b2)
print(lib.find_book("title2"))