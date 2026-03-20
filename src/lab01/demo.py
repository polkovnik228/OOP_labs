from model import Book

print("========== СЦЕНАРИЙ 1: СОЗДАНИЕ И ВЫВОД ==========")

book1 = Book("War and Peace", "Lev Tolstoy", 1869, 1200, 1000)
book2 = Book("Crime and Punishment", "Fedor Dostoevsky", 1866, 650, 900)

print(book1)
print(book2)

print("\n========== СЦЕНАРИЙ 2: СРАВНЕНИЕ ==========")
book3 = Book("War and Peace", "Lev Tolstoy", 1869, 1200, 500)
print("book1 == book2:", book1 == book2)
print("book1 == book3:", book1 == book3)

print("\n========== СЦЕНАРИЙ 3: SETTER ==========")
print("Старая цена:", book1.price)
book1.price = 800
print("Новая цена:", book1.price)

print("\n========== СЦЕНАРИЙ 4: БИЗНЕС-МЕТОДЫ ==========")
book1.discount(10)
print("Цена после скидки:", book1.price)
print("Большая ли книга:", book1.is_big())

print("\n========== СЦЕНАРИЙ 5: АТРИБУТ КЛАССА ==========")
print("Через класс:", Book.library_name)
print("Через объект:", book1.library_name)

print("\n========== СЦЕНАРИЙ 6: СОСТОЯНИЕ ==========")
print("До выдачи:", book1)
book1.take()
print("После выдачи:", book1)

print("\nПопытка взять книгу повторно:")
try:
    book1.take()
except Exception as e:
    print("Ошибка:", e)

print("\nПопытка изменить цену выданной книги:")
try:
    book1.price = 500
except Exception as e:
    print("Ошибка:", e)

print("\nПопытка применить скидку к выданной книге:")
try:
    book1.discount(5)
except Exception as e:
    print("Ошибка:", e)

print("\nВозврат книги:")
book1.return_book()
print(book1)

print("\n========== СЦЕНАРИЙ 7: ВАЛИДАЦИЯ ==========")

tests = [
    ("", "Author", 2000, 100, 100),
    ("Book", "", 2000, 100, 100),
    ("Book", "Author", 3000, 100, 100),
    ("Book", "Author", 2000, -10, 100),
    ("Book", "Author", 2000, 100, -50),
]

for t in tests:
    try:
        Book(*t)
    except Exception as e:
        print("Ошибка:", e)

print("\nПроверка некорректной скидки:")
try:
    book2.discount(150)
except Exception as e:
    print("Ошибка:", e)

print("\n========== СЦЕНАРИЙ 8: REPR ==========")
print(repr(book2))
