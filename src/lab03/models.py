from .base import Book


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, price, cover_type, circulation):
        super().__init__(title, author, year, pages, price)

        if not isinstance(cover_type, str):
            raise TypeError("Тип обложки должен быть строкой")
        if not cover_type.strip():
            raise ValueError("Тип обложки не может быть пустым")

        if not isinstance(circulation, int):
            raise TypeError("Тираж должен быть целым числом")
        if circulation <= 0:
            raise ValueError("Тираж должен быть больше 0")

        self._cover_type = cover_type
        self._circulation = circulation

    @property
    def cover_type(self):
        return self._cover_type

    @property
    def circulation(self):
        return self._circulation

    def calculate_price(self):
        if self._circulation < 1000:
            return self.price * 1.15
        return self.price

    def is_rare(self):
        return self._circulation < 500

    def __str__(self):
        status = "доступна" if self.is_available else "выдана"
        return (
            f"Печатная книга: '{self.title}' — {self.author}, {self.year}, "
            f"{self.pages} стр., {self.price:.2f}₽, обложка: {self.cover_type}, "
            f"тираж: {self.circulation} ({status})"
        )


class EBook(Book):
    def __init__(self, title, author, year, pages, price, file_format, file_size):
        super().__init__(title, author, year, pages, price)

        if not isinstance(file_format, str):
            raise TypeError("Формат файла должен быть строкой")
        if not file_format.strip():
            raise ValueError("Формат файла не может быть пустым")

        if not isinstance(file_size, (int, float)):
            raise TypeError("Размер файла должен быть числом")
        if file_size <= 0:
            raise ValueError("Размер файла должен быть больше 0")

        self._file_format = file_format
        self._file_size = float(file_size)

    @property
    def file_format(self):
        return self._file_format

    @property
    def file_size(self):
        return self._file_size

    def calculate_price(self):
        return self.price * 0.85

    def can_store_on_device(self, free_space):
        if not isinstance(free_space, (int, float)):
            raise TypeError("Свободное место должно быть числом")
        if free_space < 0:
            raise ValueError("Свободное место не может быть отрицательным")
        return free_space >= self.file_size

    def __str__(self):
        status = "доступна" if self.is_available else "выдана"
        return (
            f"Электронная книга: '{self.title}' — {self.author}, {self.year}, "
            f"{self.pages} стр., {self.price:.2f}₽, формат: {self.file_format}, "
            f"размер: {self.file_size:.2f} МБ ({status})"
        )