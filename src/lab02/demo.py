from .collection import Library
from .model import Book


def print_books(title, books):
    print(f"\n{title}")
    if not books:
        print("Нет книг")
        return

    for i, book in enumerate(books):
        print(f"{i}: {book}")


def main():
    book1 = Book("1984", "Джордж Оруэлл", 1949, 328, 500)
    book2 = Book("Война и мир", "Лев Толстой", 1869, 1225, 950)
    book3 = Book("Чистый код", "Роберт Мартин", 2008, 464, 1200)
    book4 = Book("Хоббит", "Д. Р. Р. Толкин", 1937, 310, 700)

    library = Library("Central Library")

    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(book4)

    print_books("После добавления книг:", library)

    print(f"\nКоличество книг: {len(library)}")

    print("\nПеребор через for:")
    for book in library:
        print(book)

    print_books("Поиск по автору 'Джордж Оруэлл':", library.find_by_author("Джордж Оруэлл"))
    print_books("Поиск по названию '1984':", library.find_by_title("1984"))
    print_books("Поиск по году 1937:", library.find_by_year(1937))

    print("\nПопытка добавить дубликат:")
    try:
        duplicate = Book("1984", "Джордж Оруэлл", 1949, 328, 500)
        library.add(duplicate)
    except ValueError as error:
        print("Ошибка:", error)

    print("\nПопытка добавить неправильный тип:")
    try:
        library.add("не книга")
    except TypeError as error:
        print("Ошибка:", error)

    print("\nКнига с индексом 1:")
    print(library[1])

    sorted_by_title = library.sort_by_title()
    print_books("Сортировка по названию:", sorted_by_title)

    sorted_by_price = library.sort_by_price()
    print_books("Сортировка по цене:", sorted_by_price)

    book3.take() 
    print_books("Только доступные книги:", library.get_available())
    print_books("Дорогие книги (цена > 800):", library.get_expensive(800))
    print_books("Большие книги:", library.get_big_books())

    library.remove(book4)
    print_books("После удаления Хоббит:", library)

    library.remove_at(0)
    print_books("После удаления элемента с индексом 0:", library)


if __name__ == "__main__":
    main()