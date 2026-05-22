"""слой интерфейса: меню, ввод и вывод"""

from typing import List

from lab01.model import Book
from lab03.models import PrintedBook, EBook

from .app import LibraryApp
from .exceptions import LibraryError


def print_menu() -> None:
    """главное меню"""
    print("\n" + "=" * 40)
    print("        БИБЛИОТЕКА - ГЛАВНОЕ МЕНЮ")
    print("=" * 40)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу")
    print("4. Фильтрация книг")
    print("5. Сортировка книг")
    print("6. Удалить книгу")
    print("0. Выход")
    print("=" * 40)


def print_books(books: List[Book]) -> None:
    """вывести список книг в виде таблицы"""
    if not books:
        print("\nКниг нет.")
        return

    print(f"\n{'№':<3} {'Название':<28} {'Автор':<22} {'Год':<6} {'Цена':<10} {'Статус':<10}")
    print("-" * 82)
    for i, book in enumerate(books, start=1):
        status = "доступна" if book.is_available else "выдана"
        print(
            f"{i:<3} {book.title[:27]:<28} {book.author[:21]:<22} "
            f"{book.year:<6} {book.price:<10.2f} {status:<10}"
        )


def input_int(prompt: str) -> int:
    """запросить целое число, ValueError при некорректном вводе"""
    return int(input(prompt))


def input_float(prompt: str) -> float:
    """запросить число с плавающей точкой"""
    return float(input(prompt))


def confirm(prompt: str) -> bool:
    """запросить подтверждение y/n."""
    answer = input(f"{prompt} (y/n): ").strip().lower()
    return answer == "y"


def action_add(app: LibraryApp) -> None:
    """добавить книгу: запросить данные и передать в app"""
    print("\n--- Добавление книги ---")
    print("Тип книги: 1 - обычная, 2 - печатная, 3 - электронная")

    try:
        book_type = input_int("Выберите тип: ")
        title = input("Название: ").strip()
        author = input("Автор: ").strip()
        year = input_int("Год издания: ")
        pages = input_int("Количество страниц: ")
        price = input_float("Цена: ")

        if book_type == 2:
            cover = input("Тип обложки: ").strip()
            circulation = input_int("Тираж: ")
            book: Book = PrintedBook(title, author, year, pages, price, cover, circulation)
        elif book_type == 3:
            fmt = input("Формат файла: ").strip()
            size = input_float("Размер файла (МБ): ")
            book = EBook(title, author, year, pages, price, fmt, size)
        else:
            book = Book(title, author, year, pages, price)

        app.add_book(book)
        print(f"\nКнига '{title}' добавлена.")

    except ValueError as e:
        print(f"\nОшибка ввода: {e}")
    except LibraryError as e:
        print(f"\nОшибка: {e}")


def action_show(app: LibraryApp) -> None:
    """показать все книги"""
    print("\n--- Все книги ---")
    print_books(app.get_all())
    print(f"\nВсего книг: {app.count()}")


def action_find(app: LibraryApp) -> None:
    """найти книгу по названию"""
    print("\n--- Поиск книги ---")
    title = input("Введите название: ").strip()
    book = app.find_by_title(title)
    if book is None:
        print(f"\nКнига '{title}' не найдена.")
    else:
        print_books([book])


def action_filter(app: LibraryApp) -> None:
    """отфильтровать книги по выбранному условию"""
    print("\n--- Фильтрация ---")
    print("1. По максимальной цене")
    print("2. Только доступные")

    try:
        choice = input_int("Выберите фильтр: ")
        if choice == 1:
            max_price = input_float("Максимальная цена: ")
            print_books(app.filter_by_price(max_price))
        elif choice == 2:
            print_books(app.filter_available())
        else:
            print("Неверный пункт.")
    except ValueError as e:
        print(f"\nОшибка ввода: {e}")


def action_sort(app: LibraryApp) -> None:
    """отсортировать книги по выбранной стратегии"""
    print("\n--- Сортировка ---")
    print("1. По названию")
    print("2. По цене")
    print("3. По году")

    try:
        choice = input_int("Сортировать по: ")
        if choice == 1:
            print_books(app.sort_by(lambda b: b.title.lower()))
        elif choice == 2:
            print_books(app.sort_by(lambda b: b.price))
        elif choice == 3:
            print_books(app.sort_by(lambda b: b.year))
        else:
            print("Неверный пункт.")
    except ValueError as e:
        print(f"\nОшибка ввода: {e}")


def action_remove(app: LibraryApp) -> None:
    """удалить книгу с подтверждением"""
    print("\n--- Удаление книги ---")
    title = input("Введите название книги для удаления: ").strip()

    book = app.find_by_title(title)
    if book is None:
        print(f"\nКнига '{title}' не найдена.")
        return

    if confirm(f"Удалить '{book.title}'?"):
        try:
            app.remove_book(title)
            print(f"\nКнига '{title}' удалена.")
        except LibraryError as e:
            print(f"\nОшибка: {e}")
    else:
        print("\nУдаление отменено.")


def run(app: LibraryApp) -> None:
    """главный цикл приложения"""
    count = app.load_data()
    print(f"Загружено книг из файла: {count}")

    while True:
        print_menu()

        try:
            choice = input_int("Выберите пункт: ")
        except ValueError:
            print("\nОшибка: введите число.")
            continue

        if choice == 1:
            action_add(app)
        elif choice == 2:
            action_show(app)
        elif choice == 3:
            action_find(app)
        elif choice == 4:
            action_filter(app)
        elif choice == 5:
            action_sort(app)
        elif choice == 6:
            action_remove(app)
        elif choice == 0:
            app.save_data()
            print("\nДанные сохранены. До свидания!")
            break
        else:
            print("\nНеверный пункт меню.")