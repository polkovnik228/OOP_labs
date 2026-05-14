from lab03.models import PrintedBook, EBook


def by_title(book):
    """сортировка по названию книги"""
    return book.title.lower()


def by_price(book):
    """сортировка по цене книги"""
    return book.price


def by_year_and_pages(book):
    """сортировка по году, затем по количеству страниц"""
    return (book.year, book.pages)


def is_available(book):
    """фильтр: книга доступна"""
    return book.is_available


def is_big(book):
    """фильтр: большая книга"""
    return book.is_big()


def is_printed(book):
    """фильтр: только печатные книги"""
    return isinstance(book, PrintedBook)


def is_ebook(book):
    """фильтр: только электронные книги"""
    return isinstance(book, EBook)


def to_title(book):
    """вернуть название книги"""
    return book.title


def to_dict(book):
    """преобразовать книгу в словарь"""
    return {
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "price": book.price,
    }


def make_price_filter(max_price):
    """создаёт фильтр по максимальной цене"""
    def filter_fn(book):
        return book.price <= max_price
    return filter_fn


def make_year_filter(min_year):
    """создаёт фильтр по минимальному году издания"""
    def filter_fn(book):
        return book.year >= min_year
    return filter_fn


def apply_discount(percent):
    """создаёт функцию, применяющую скидку к книге"""
    def transformer(book):
        if book.is_available:
            book.discount(percent)
        return book
    return transformer


class DiscountStrategy:
    """стратегия расчёта цены со скидкой"""

    def __init__(self, percent):
        self.percent = percent

    def __call__(self, book):
        return book.price * (1 - self.percent / 100)

    def __repr__(self):
        return f"DiscountStrategy(percent={self.percent})"


class PriceCalculatorStrategy:
    """стратегия расчёта цены через calculate_price() из ЛР-3"""

    def __call__(self, book):
        return book.calculate_price()

    def __repr__(self):
        return "PriceCalculatorStrategy()"