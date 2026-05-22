"""собственные исключения для предметной области библиотеки"""


class LibraryError(Exception):
    """базовое исключение приложения"""
    pass


class ItemNotFoundError(LibraryError):
    """книга не найдена в коллекции"""
    pass


class DuplicateItemError(LibraryError):
    """книга с такими данными уже существует"""
    pass