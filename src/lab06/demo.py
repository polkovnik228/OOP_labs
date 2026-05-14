from .container import (
    TypedCollection,
    BookView,
    PrintedBookView,
    EBookView,
)


def main():
    print("========== СЦЕНАРИЙ 1: СОЗДАНИЕ ТИПИЗИРОВАННОЙ КОЛЛЕКЦИИ ==========")

    books: TypedCollection[BookView] = TypedCollection()
    books.add(BookView("1984", "Джордж Оруэлл", 1949, 328, 500))
    books.add(BookView("Война и мир", "Лев Толстой", 1869, 1225, 950))
    books.add(BookView("Хоббит", "Д. Р. Р. Толкин", 1937, 310, 700))

    print("Все элементы коллекции:")
    for book in books.get_all():
        print(book)

    print(f"\nКоличество элементов: {len(books)}")
    print(f"Элемент с индексом 0: {books[0]}")

    print("\n========== СЦЕНАРИЙ 2: ВАЛИДАЦИЯ ТИПОВ ==========")

    print("Добавление объекта другого типа (строка вместо BookView):")
    try:
        books.add("не книга")
        print("Объект добавлен (без проверки в рантайме)")
    except Exception as e:
        print("Ошибка:", e)

    print("\nПри статической проверке типов (например, mypy)")
    print("такая строка будет помечена как ошибка — TypedCollection[BookView]")
    print("ожидает только объекты BookView.")

    books.remove("не книга")

    print("\n========== СЦЕНАРИЙ 3: МЕТОД find ==========")

    found = books.find(lambda b: b.year > 1900)
    print(f"Первая книга, изданная после 1900: {found}")

    not_found = books.find(lambda b: b.year > 3000)
    print(f"Поиск книги из будущего: {not_found}")

    print("\n========== СЦЕНАРИЙ 4: МЕТОД filter ==========")

    big_books = books.filter(lambda b: b.pages >= 500)
    print("Большие книги (>= 500 страниц):")
    for book in big_books:
        print(book)

    print("\n========== СЦЕНАРИЙ 5: МЕТОД map С РАЗНЫМИ ТИПАМИ РЕЗУЛЬТАТА ==========")

    titles: list[str] = books.map(lambda b: b.title)
    print("Список названий (list[str]):")
    print(titles)

    prices: list[float] = books.map(lambda b: b.price)
    print("\nСписок цен (list[float]):")
    print(prices)

    print("\n========== СЦЕНАРИЙ 6: TypedCollection[D] И ПРОТОКОЛ Displayable ==========")

    displayable: TypedCollection = TypedCollection()
    displayable.add(BookView("1984", "Джордж Оруэлл", 1949, 328, 500))
    displayable.add(PrintedBookView("Хоббит", "Д. Р. Р. Толкин", 1937, 310, 700, "мягкая", 5000))
    displayable.add(EBookView("Чистый код", "Роберт Мартин", 2008, 464, 1200, "PDF", 12.5))

    print("Объекты разных типов в одной коллекции (без наследования от Displayable):")
    for item in displayable:
        print(item.display())

    print("\n========== СЦЕНАРИЙ 7: TypedCollection[S] И ПРОТОКОЛ Scorable ==========")

    scorable: TypedCollection = TypedCollection()
    scorable.add(BookView("1984", "Джордж Оруэлл", 1949, 328, 500))
    scorable.add(PrintedBookView("Хоббит", "Д. Р. Р. Толкин", 1937, 310, 700, "мягкая", 5000))
    scorable.add(EBookView("Чистый код", "Роберт Мартин", 2008, 464, 1200, "PDF", 12.5))

    print("Метод score() работает для каждого типа по-своему:")
    for item in scorable:
        print(f"{item.title}: score = {item.score():.2f}")


if __name__ == "__main__":
    main()