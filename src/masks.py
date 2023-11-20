import os

from data import PATH_DATA


def get_dir_content(path: str = ".", count_all: bool = False) -> dict:
    """
    Функция считает количество директорий и файлов.
    :param path: директория для подсчета
    :param count_all: флаг для подсчета в глубину
    :return: словарь с количеством директорий и файлов
    """
    content = {"files": 0, "folders": 0}

    for dir_path, dir_names, file_names in os.walk(path):
        # перебираем каталоги
        for dir_name in dir_names:
            content["folders"] += 1

        # перебираем файлы
        for file_name in file_names:
            content["files"] += 1

        if not count_all:
            break

    return content
