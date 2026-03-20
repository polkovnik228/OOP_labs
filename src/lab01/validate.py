def validate_title(value):
    if not isinstance(value, str):
        raise TypeError("Название должно быть строкой")
    if not value.strip():
        raise ValueError("Название не может быть пустым")


def validate_author(value):
    if not isinstance(value, str):
        raise TypeError("Автор должен быть строкой")
    if not value.strip():
        raise ValueError("Автор не может быть пустым")


def validate_year(value, current_year):
    if not isinstance(value, int):
        raise TypeError("Год должен быть числом")
    if value < 0:
        raise ValueError("Год не может быть отрицательным")
    if value > current_year:
        raise ValueError("Год не может быть из будущего")


def validate_pages(value):
    if not isinstance(value, int):
        raise TypeError("Страницы должны быть числом")
    if value <= 0:
        raise ValueError("Количество страниц должно быть > 0")


def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")
    if value < 0:
        raise ValueError("Цена не может быть отрицательной")


def validate_percent(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Скидка должна быть числом")
    if value <= 0 or value > 100:
        raise ValueError("Скидка должна быть в диапазоне 0–100")