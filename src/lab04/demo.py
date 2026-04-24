from interfaces import Printable, Comparable
from models import Book, EBook, AudioBook, Magazine, LibraryCollection


def print_all(items):
    print("=== Вывод объектов через интерфейс Printable ===")
    for item in items:
        print(item.to_string())
    print()


def check_interfaces(items):
    print("=== Проверка через isinstance ===")
    for item in items:
        print(item.__class__.__name__)
        print("Printable:", isinstance(item, Printable))
        print("Comparable:", isinstance(item, Comparable))
        print()
        

def show_sorted(items):
    print("=== Comparable-объекты ===")
    for item in items:
        print(item.to_string())
    print()


def main():
    book = Book("Война и мир", "Лев Толстой", 1869, 1225)
    ebook = EBook("Python для начинающих", "Иван Петров", 2023, 350, "PDF", 5.4)
    audiobook = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 720, "Алексей Иванов")
    magazine = Magazine("Наука и жизнь", 4, "Апрель")

    library = LibraryCollection()
    library.add_item(book)
    library.add_item(ebook)
    library.add_item(audiobook)
    library.add_item(magazine)

    # Сценарий 1
    print_all(library.get_printable())

    # Сценарий 2
    check_interfaces(library.get_all())

    # Сценарий 3
    show_sorted(library.get_comparable())

    print("=== Сортировка через интерфейс Comparable ===")
    for item in library.sort_comparable():
        print(item.to_string())
    print()

    print("=== Дополнительные методы ===")
    print(ebook.download())
    print(audiobook.play_sample())
    print()

    print("=== Изменение состояния книги ===")
    print(book.to_string())
    book.borrow()
    print(book.to_string())
    book.return_book()
    print(book.to_string())


if __name__ == "__main__":
    main()