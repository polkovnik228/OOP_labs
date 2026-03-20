from validate import (
    validate_title,
    validate_author,
    validate_year,
    validate_pages,
    validate_price,
    validate_percent,
)


class Book:
    library_name = "Central Library"
    current_year = 2026

    def __init__(self, title, author, year, pages, price):
        validate_title(title)
        validate_author(author)
        validate_year(year, Book.current_year)
        validate_pages(pages)
        validate_price(price)

        self._title = title
        self._author = author
        self._year = year
        self._pages = pages
        self._price = float(price)

        self._is_available = True

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not self._is_available:
            raise Exception("Нельзя менять цену выданной книги")
        validate_price(value)
        self._price = float(value)

    @property
    def is_available(self):
        return self._is_available

    def take(self):
        if not self._is_available:
            raise Exception("Книга уже выдана")
        self._is_available = False

    def return_book(self):
        self._is_available = True

    def discount(self, percent):
        if not self._is_available:
            raise Exception("Нельзя делать скидку на выданную книгу")
        validate_percent(percent)
        self._price *= (1 - percent / 100)

    def is_big(self):
        return self._pages >= 500

    def __str__(self):
        status = "доступна" if self._is_available else "выдана"
        return f" '{self._title}' — {self._author}, {self._year}, {self._pages} стр., {self._price:.2f}₽ ({status})"

    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', {self._year}, {self._pages}, {self._price})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self._title == other._title
            and self._author == other._author
            and self._year == other._year
        )
    
 