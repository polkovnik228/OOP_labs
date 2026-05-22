"""слой бизнес-логики: управление коллекцией книг"""

from typing import List, Optional, Callable

from lab01.model import Book
from lab03.models import PrintedBook, EBook

from .exceptions import ItemNotFoundError, DuplicateItemError
from . import storage


class LibraryApp:
    """CLI обращается к данным только через этот класс"""

    def __init__(self, filepath: str = "library.json") -> None:
        """создать приложение с указанным файлом данных"""
        self._filepath: str = filepath
        self._books: List[Book] = []

    def load_data(self) -> int:
        """загрузить книги из файла, вернуть количество загруженных книг"""
        self._books = storage.load(self._filepath)
        return len(self._books)

    def save_data(self) -> None:
        """сохранить книги в файл"""
        storage.save(self._books, self._filepath)

    def get_all(self) -> List[Book]:
        """вернуть список всех книг"""
        return list(self._books)

    def count(self) -> int:
        """вернуть количество книг в коллекции"""
        return len(self._books)

    def add_book(self, book: Book) -> None:
        """добавить книгу, бросает DuplicateItemError, если такая уже есть"""
        for existing in self._books:
            if existing == book:
                raise DuplicateItemError(
                    f"Книга '{book.title}' ({book.year}) уже есть в библиотеке"
                )
        self._books.append(book)

    def remove_book(self, title: str) -> Book:
        """удалить книгу по названию, бросает ItemNotFoundError, если не найдена"""
        book = self.find_by_title(title)
        if book is None:
            raise ItemNotFoundError(f"Книга '{title}' не найдена")
        self._books.remove(book)
        return book

    def find_by_title(self, title: str) -> Optional[Book]:
        """найти первую книгу по названию (без учёта регистра)"""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_by_author(self, author: str) -> List[Book]:
        """найти все книги указанного автора"""
        return [b for b in self._books if b.author.lower() == author.lower()]

    def filter_by_price(self, max_price: float) -> List[Book]:
        """вернуть книги с ценой не выше указанной"""
        return [b for b in self._books if b.price <= max_price]

    def filter_available(self) -> List[Book]:
        """вернуть только доступные книги"""
        return [b for b in self._books if b.is_available]

    def sort_by(self, key_func: Callable[[Book], object]) -> List[Book]:
        """вернуть отсортированный список книг по переданной функции-стратегии"""
        return sorted(self._books, key=key_func)