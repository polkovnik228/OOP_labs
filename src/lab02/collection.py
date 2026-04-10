from .model import Book

class Library:
    def __init__(self, name="Library"):
        self.name = name
        self._items = []

    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("Можно добавлять только объекты Book")

        if item in self._items:
            raise ValueError("Такая книга уже есть в библиотеке")

        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("Книга не найдена в библиотеке")

        self._items.remove(item)

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")

        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")

        del self._items[index]

    def get_all(self):
        return self._items.copy()

    def find_by_title(self, title):
        return [book for book in self._items if book.title.lower() == title.lower()]

    def find_by_author(self, author):
        return [book for book in self._items if book.author.lower() == author.lower()]

    def find_by_year(self, year):
        return [book for book in self._items if book.year == year]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self, key):
        new_library = Library(f"{self.name} (sorted)")
        new_library._items = sorted(self._items, key=key)
        return new_library

    def sort_by_title(self):
        return self.sort(lambda book: book.title.lower())

    def sort_by_price(self):
        return self.sort(lambda book: book.price)

    def sort_by_year(self):
        return self.sort(lambda book: book.year)

    def get_available(self):
        new_library = Library(f"{self.name} (available)")
        new_library._items = [book for book in self._items if book.is_available]
        return new_library

    def get_expensive(self, min_price):
        new_library = Library(f"{self.name} (expensive)")
        new_library._items = [book for book in self._items if book.price > min_price]
        return new_library

    def get_big_books(self):
        new_library = Library(f"{self.name} (big books)")
        new_library._items = [book for book in self._items if book.is_big()]
        return new_library

    def __str__(self):
        if not self._items:
            return f"{self.name}: пусто"
        return f"{self.name}:\n" + "\n".join(str(book) for book in self._items)

    def __repr__(self):
        return f"Library(name='{self.name}', items={self._items})"