from interfaces import Printable, Comparable


class Book(Printable, Comparable):
    def __init__(self, title, author, year, pages, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
        else:
            raise ValueError(f"Книга '{self.title}' уже выдана.")

    def return_book(self):
        self.available = True

    def to_string(self):
        status = "доступна" if self.available else "выдана"
        return (
            f"Книга: '{self.title}', автор: {self.author}, "
            f"год: {self.year}, страниц: {self.pages}, статус: {status}"
        )

    def compare_to(self, other):
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только книги.")
        if self.pages > other.pages:
            return 1
        elif self.pages < other.pages:
            return -1
        return 0


class EBook(Book):
    def __init__(self, title, author, year, pages, file_format, file_size_mb, available=True):
        super().__init__(title, author, year, pages, available)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def download(self):
        return f"Электронная книга '{self.title}' скачана."

    def to_string(self):
        status = "доступна" if self.available else "недоступна"
        return (
            f"Электронная книга: '{self.title}', автор: {self.author}, "
            f"год: {self.year}, страниц: {self.pages}, формат: {self.file_format}, "
            f"размер: {self.file_size_mb} MB, статус: {status}"
        )


class AudioBook(Book):
    def __init__(self, title, author, year, pages, duration_min, narrator, available=True):
        super().__init__(title, author, year, pages, available)
        self.duration_min = duration_min
        self.narrator = narrator

    def play_sample(self):
        return f"Проигрывается фрагмент аудиокниги '{self.title}'."

    def to_string(self):
        status = "доступна" if self.available else "выдана"
        return (
            f"Аудиокнига: '{self.title}', автор: {self.author}, "
            f"год: {self.year}, страниц: {self.pages}, длительность: {self.duration_min} мин, "
            f"диктор: {self.narrator}, статус: {status}"
        )


class Magazine(Printable):
    def __init__(self, title, issue_number, month):
        self.title = title
        self.issue_number = issue_number
        self.month = month

    def to_string(self):
        return f"Журнал: '{self.title}', номер: {self.issue_number}, месяц: {self.month}"


class LibraryCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all(self):
        return self.items

    def get_printable(self):
        return [item for item in self.items if isinstance(item, Printable)]

    def get_comparable(self):
        return [item for item in self.items if isinstance(item, Comparable)]

    def sort_comparable(self):
        items = self.get_comparable()
        result = items[:]

        for i in range(len(result)):
            for j in range(len(result) - 1 - i):
                if result[j].compare_to(result[j + 1]) == 1:
                    result[j], result[j + 1] = result[j + 1], result[j]

        return result