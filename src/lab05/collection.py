class BookCollection:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def show(self):
        for book in self.books:
            print(book)

    def sort_by(self, key_func):
        sorted_books = sorted(self.books, key=key_func)
        new_collection = BookCollection()
        for book in sorted_books:
            new_collection.add(book)
        return new_collection

    def filter_by(self, predicate):
        filtered_books = filter(predicate, self.books)
        new_collection = BookCollection()
        for book in filtered_books:
            new_collection.add(book)
        return new_collection

    def apply(self, func):
        result = list(map(func, self.books))
        new_collection = BookCollection()
        for item in result:
            new_collection.add(item)
        return new_collection