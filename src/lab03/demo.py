from lab02.collection import Library
from .base import Book
from .models import PrintedBook, EBook


def print_books(title, books):
    print(f"\n{title}")
    books = list(books)

    if not books:
        print("Нет книг")
        return

    for i, book in enumerate(books, start=1):
        print(f"{i}. {book}")


def main():
    print("========== СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ ==========")

    book1 = PrintedBook("Война и мир", "Лев Толстой", 1869, 1225, 950, "твёрдая", 300)
    book2 = PrintedBook("Хоббит", "Д. Р. Р. Толкин", 1937, 310, 700, "мягкая", 5000)
    book3 = EBook("Чистый код", "Роберт Мартин", 2008, 464, 1200, "PDF", 12.5)
    book4 = EBook("1984", "Джордж Оруэлл", 1949, 328, 500, "EPUB", 3.2)

    print(book1)
    print(book2)
    print(book3)
    print(book4)

    print("\n========== СЦЕНАРИЙ 2: РАБОТА ЧЕРЕЗ ОДНУ КОЛЛЕКЦИЮ ==========")

    library = Library("Central Library")
    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(book4)

    print_books("Все книги в библиотеке:", library)
    print(f"\nКоличество книг: {len(library)}")

    print("\n========== СЦЕНАРИЙ 3: ПОЛИМОРФИЗМ ==========")
    print("Один и тот же метод calculate_price() работает по-разному:")

    for book in library:
        print(
            f"{book.title}: базовая цена = {book.price:.2f}₽, "
            f"итоговая цена = {book.calculate_price():.2f}₽"
        )

    print("\n========== СЦЕНАРИЙ 4: МЕТОДЫ БАЗОВОГО И ДОЧЕРНИХ КЛАССОВ ==========")

    print(f"'{book1.title}' большая книга: {'Да' if book1.is_big() else 'Нет'}")
    print(f"'{book1.title}' редкое издание: {'Да' if book1.is_rare() else 'Нет'}")

    print(
        f"'{book3.title}' поместится на устройство с 10 МБ: "
        f"{'Да' if book3.can_store_on_device(10) else 'Нет'}"
    )

    print(
        f"'{book3.title}' поместится на устройство с 20 МБ: "
        f"{'Да' if book3.can_store_on_device(20) else 'Нет'}"
    )

    print("\n========== СЦЕНАРИЙ 5: ПРОВЕРКА ТИПОВ ЧЕРЕЗ isinstance() ==========")

    for book in library:
        if isinstance(book, PrintedBook):
            print(f"'{book.title}' — это печатная книга")
        elif isinstance(book, EBook):
            print(f"'{book.title}' — это электронная книга")
        elif isinstance(book, Book):
            print(f"'{book.title}' — это обычная книга")

    print("\n========== СЦЕНАРИЙ 6: ФИЛЬТРАЦИЯ ПО ТИПУ ==========")

    printed_books = [book for book in library if isinstance(book, PrintedBook)]
    ebooks = [book for book in library if isinstance(book, EBook)]

    print_books("Только печатные книги:", printed_books)
    print_books("Только электронные книги:", ebooks)

    print("\n========== СЦЕНАРИЙ 7: ИНТЕГРАЦИЯ С КОЛЛЕКЦИЕЙ ИЗ ЛР-2 ==========")

    book3.take()

    print_books("Только доступные книги:", library.get_available())
    print_books("Большие книги:", library.get_big_books())
    print_books("Сортировка по названию:", library.sort_by_title())
    print_books("Сортировка по цене:", library.sort_by_price())


if __name__ == "__main__":
    main()