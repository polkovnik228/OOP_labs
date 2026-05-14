from typing import TypeVar, Generic, Callable, Optional, Protocol

from lab01.model import Book
from lab03.models import PrintedBook, EBook


T = TypeVar("T")
R = TypeVar("R")


class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]


class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


class BookView(Book):
    def display(self) -> str:
        return f"'{self.title}' — {self.author}, {self.year}"

    def score(self) -> float:
        return self.price


class PrintedBookView(PrintedBook):
    def display(self) -> str:
        return f"[печатная] '{self.title}' — {self.author}, тираж {self.circulation}"

    def score(self) -> float:
        return self.calculate_price()


class EBookView(EBook):
    def display(self) -> str:
        return f"[электронная] '{self.title}' — {self.author}, {self.file_format}"

    def score(self) -> float:
        return self.calculate_price()