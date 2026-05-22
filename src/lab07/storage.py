"""сохранение и загрузка коллекции книг в JSON-файл"""

import json
import os
from typing import List

from lab01.model import Book
from lab03.models import PrintedBook, EBook


def book_to_dict(book: Book) -> dict:
    """преобразовать книгу в словарь для сохранения"""
    data = {
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "pages": book.pages,
        "price": book.price,
        "is_available": book.is_available,
    }

    if isinstance(book, PrintedBook):
        data["type"] = "printed"
        data["cover_type"] = book.cover_type
        data["circulation"] = book.circulation
    elif isinstance(book, EBook):
        data["type"] = "ebook"
        data["file_format"] = book.file_format
        data["file_size"] = book.file_size
    else:
        data["type"] = "book"

    return data


def dict_to_book(data: dict) -> Book:
    """восстановить книгу из словаря"""
    book_type = data.get("type", "book")

    if book_type == "printed":
        book = PrintedBook(
            data["title"], data["author"], data["year"],
            data["pages"], data["price"],
            data["cover_type"], data["circulation"],
        )
    elif book_type == "ebook":
        book = EBook(
            data["title"], data["author"], data["year"],
            data["pages"], data["price"],
            data["file_format"], data["file_size"],
        )
    else:
        book = Book(
            data["title"], data["author"], data["year"],
            data["pages"], data["price"],
        )

    if not data.get("is_available", True):
        book.take()

    return book


def save(books: List[Book], filepath: str) -> None:
    """сохранить список книг в JSON-файл"""
    data = [book_to_dict(book) for book in books]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(filepath: str) -> List[Book]:
    """загрузить список книг из JSON-файла, если файла нет - вернуть пустой список"""
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [dict_to_book(item) for item in data]