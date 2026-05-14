from lab03.models import PrintedBook, EBook

from .collection import BookCollection
from .strategies import (
    by_title, by_price, by_year_and_pages,
    is_available, is_big, is_printed, is_ebook,
    to_title, to_dict,
    make_price_filter, make_year_filter, apply_discount,
    DiscountStrategy, PriceCalculatorStrategy,
)


def print_books(title, books):
    print(f"\n{title}")
    books = list(books)
    if not books:
        print("Нет книг")
        return
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book}")


def build_collection():
    collection = BookCollection()
    collection.add(PrintedBook("Война и мир", "Лев Толстой", 1869, 1225, 950, "твёрдая", 300))
    collection.add(PrintedBook("Хоббит", "Д. Р. Р. Толкин", 1937, 310, 700, "мягкая", 5000))
    collection.add(EBook("Чистый код", "Роберт Мартин", 2008, 464, 1200, "PDF", 12.5))
    collection.add(EBook("1984", "Джордж Оруэлл", 1949, 328, 500, "EPUB", 600))
    collection.add(PrintedBook("Преступление и наказание", "Ф. Достоевский", 1866, 671, 850, "твёрдая", 800))
    return collection


def main():
    collection = build_collection()

    print("========== СЦЕНАРИЙ 1: СОРТИРОВКА ТРЕМЯ СТРАТЕГИЯМИ ==========")

    print_books("Исходная коллекция:", collection.books)
    print_books("Сортировка по названию:", sorted(collection.books, key=by_title))
    print_books("Сортировка по цене:", sorted(collection.books, key=by_price))
    print_books("Сортировка по году и страницам:", sorted(collection.books, key=by_year_and_pages))

    print("\n========== СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ ==========")

    print_books("Только доступные книги:", filter(is_available, collection.books))
    print_books("Только электронные книги (isinstance):", filter(is_ebook, collection.books))

    print("\n========== СЦЕНАРИЙ 3: ИСПОЛЬЗОВАНИЕ MAP ==========")

    names = list(map(to_title, collection.books))
    print("Названия книг:", names)

    print("\nКниги в виде словарей:")
    for d in map(to_dict, collection.books):
        print(d)

    print("\nАвторы через lambda:")
    authors = list(map(lambda book: book.author, collection.books))
    print(authors)

    print("\n========== СЦЕНАРИЙ 4: ФАБРИКИ ФУНКЦИЙ ==========")

    cheap = make_price_filter(800)
    print_books("Книги дешевле 800₽:", filter(cheap, collection.books))

    modern = make_year_filter(1950)
    print_books("Книги с 1950 года:", filter(modern, collection.books))

    print("\n========== СЦЕНАРИЙ 5: МЕТОДЫ КОЛЛЕКЦИИ ==========")

    print_books("sort_by(by_price):", collection.sort_by(by_price).books)
    print_books("filter_by(is_big):", collection.filter_by(is_big).books)
    print_books("filter_by(is_printed):", collection.filter_by(is_printed).books)

    print("\n========== СЦЕНАРИЙ 6: LAMBDA И ИМЕНОВАННАЯ ФУНКЦИЯ ==========")

    by_named = collection.sort_by(by_title)
    by_lambda = collection.sort_by(lambda book: book.title.lower())

    print("Через именованную функцию by_title:")
    for book in by_named.books:
        print(book.title)

    print("\nЧерез lambda:")
    for book in by_lambda.books:
        print(book.title)

    print("\n========== СЦЕНАРИЙ 7: ЦЕПОЧКА FILTER -> SORT -> APPLY ==========")

    fresh = build_collection()

    step1 = fresh.filter_by(is_available)
    print_books("Шаг 1. После filter_by(is_available):", step1.books)

    step2 = step1.sort_by(by_price)
    print_books("Шаг 2. После sort_by(by_price):", step2.books)

    step3 = step2.apply(apply_discount(10))
    print_books("Шаг 3. После apply(apply_discount(10)):", step3.books)

    print("\nТо же одной строкой:")
    fresh2 = build_collection()
    result = fresh2.filter_by(is_available).sort_by(by_price).apply(apply_discount(10))
    print_books("Результат цепочки:", result.books)

    print("\n========== СЦЕНАРИЙ 8: ЗАМЕНА СТРАТЕГИИ ==========")

    fresh = build_collection()
    print("Коллекция одна и та же, меняем только функцию-стратегию:")
    print_books("sort_by(by_title):", fresh.sort_by(by_title).books)
    print_books("sort_by(by_price):", fresh.sort_by(by_price).books)
    print_books("sort_by(by_year_and_pages):", fresh.sort_by(by_year_and_pages).books)

    print("\n========== СЦЕНАРИЙ 9: CALLABLE-ОБЪЕКТ КАК СТРАТЕГИЯ ==========")

    fresh = build_collection()

    discount_20 = DiscountStrategy(20)
    discount_50 = DiscountStrategy(50)
    poly_price = PriceCalculatorStrategy()

    print("Созданные стратегии:")
    print(discount_20)
    print(discount_50)
    print(poly_price)

    print("\nПрименение разных стратегий к одной коллекции:")
    for book in fresh.books:
        print(f"{book.title}:")
        print(f"  базовая цена: {book.price:.2f}")
        print(f"  скидка 20%: {discount_20(book):.2f}")
        print(f"  скидка 50%: {discount_50(book):.2f}")
        print(f"  через calculate_price: {poly_price(book):.2f}")


if __name__ == "__main__":
    main()