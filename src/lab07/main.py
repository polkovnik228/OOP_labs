"""Точка входа в консольное приложение библиотеки."""

import os

from .app import LibraryApp
from .cli import run


def main() -> None:
    """Создать приложение и запустить CLI."""
    # путь к main.py → lab07/ → src/ → корень проекта
    lab07_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(lab07_dir)
    project_root = os.path.dirname(src_dir)

    data_path = os.path.join(project_root, "data", "library.json")
    app = LibraryApp(data_path)
    run(app)


if __name__ == "__main__":
    main()