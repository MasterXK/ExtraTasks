import os
from datetime import datetime
from typing import Optional, Callable
from functools import reduce


# masks
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


# widget
def get_similar(words: list[str]) -> list[str]:
    """
    Функция фильтрует список слов
    :param words: список слов
    :return: список слов с одиннаковой буквой в начале и конце
    """
    similar_start_end_words = []
    if words:

        for word in words:
            if word:

                if word[0] == word[-1]:

                    similar_start_end_words.append(word)

        return similar_start_end_words

    return []


# widget
def get_max_multiply(numbers: list[int]) -> int:
    """
    Функция ищет максимальное произведение двух чисел
    :param numbers: список чисел
    :return: масимальное произведение
    """
    nums = sorted(numbers)
    if len(nums) < 2:

        return 0

    if nums[-1] * nums[-2] > nums[0] * nums[1]:

        return nums[-1] * nums[-2]

    return nums[0] * nums[1]


# processing
def sort_by_price(products: list[dict], category: str = None) -> list[dict]:
    """
    Функция сортирует продукты по цене
    :param products: список продуктов
    :param category: категория продуктов для сортировки
    :return: отсортированный список продуктов выбранной категории
    """
    if category:

        products_to_sort = [
            product for product in products if product["category"] == category
        ]

        return sorted(products_to_sort, key=lambda x: x["price"], reverse=True)

    return sorted(products, key=lambda x: x["price"], reverse=True)


# processing
def get_months_statistic(orders: list[dict]) -> dict:
    """
    Функция получает статистику заказов по месяцам
    :param orders: список заказов
    :return:
    """
    months_statistic: dict[str, dict] = {}
    pattern_in = "%Y-%m-%dT%H:%M:%S.%f"
    pattern_out = "%Y.%m"

    for order in orders:

        date_in = datetime.strptime(order["date"], pattern_in)
        date = date_in.strftime(pattern_out)

        if date in months_statistic.keys():

            months_statistic[date]["order_count"] += 1

            for item in order["items"]:
                months_statistic[date]["average_order_value"] += (
                    item["price"] * item["quantity"]
                )
        else:

            for item in order["items"]:

                months_statistic[date] = {
                    "average_order_value": item["price"] * item["quantity"],
                    "order_count": 1,
                }

    for month in months_statistic.values():
        month["average_order_value"] /= month["order_count"]

    return months_statistic


# tests
def sum_divisible_by_3_or_5(lst: list[int]) -> int:
    """
    Функция возвращает сумму всех элементов списка, которые делятся на 3 или  5 без остатка.
    :param lst: Список чисел
    :return: сумма элементов списка, которые делятся на 3 или  5 без остатка
    """
    result = 0
    for num in lst:
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


# tests
def check_email(email: Optional[str]) -> bool:
    if email:

        if "@" in email:

            if "." in email[email.index("@") + 1 :]:

                return True

    return False


# tests
def count_number_in_list(numbers: list[int | float], number: int | float) -> int:
    counter = 0
    for num in numbers:

        if num == number:
            counter += 1

    return counter


# tests
def calculate_area(shape: str, sides: list[int | float] | int) -> float | None:
    if shape == "квадрат":

        if type(sides) is int:
            return round(sides**2, 2)

        if type(sides) is list:

            if all(x == sides[0] for x in sides[1:]) and len(sides) in [1, 4]:
                return round(sides[0] ** 2, 2)

        return None

    elif shape == "прямоугольник" and len(sides) in [2, 4]:
        if len(set(sides)) == 2:
            a = sides[0]
            for side in sides:
                if side != a:
                    return round(a * side, 2)

        return None

    elif shape == "треугольник" and len(sides) == 3:
        if (
            sides[0] + sides[1] > sides[2]
            and sides[1] + sides[2] > sides[0]
            and sides[0] + sides[2] > sides[1]
        ):
            p = sum(sides) / 2
            return round(
                (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5, 2
            )

        return None

    elif shape == "круг":
        if type(sides) is int:
            return round(3.1415 * sides**2, 2)

        if type(sides) is list:
            if len(sides) == 1:
                return round(3.1415 * sides[0] ** 2, 2)

        return None

    return None


# tests
def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:

        if normalized_start < -length:
            normalized_start = 0

        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]


# generators
def non_empty_truths(elements: list) -> list:
    clear_list = [
        elem
        for elem in [
            [arg for arg in element if bool(arg) is True] for element in elements
        ]
        if bool(elem) is True
    ]
    return clear_list


# generators
def each2d(test: Callable, matrix: list[list]):
    return all(False for element in matrix for arg in element if not test(arg))


# generators
def some2d(test: Callable, matrix: list[list]):
    return any(True for element in matrix for arg in element if test(arg))


# generators
def sum2d(test: Callable, matrix: list[list]):
    return sum(arg for element in matrix for arg in element if test(arg))


# generators
def my_map(f, xs):
    return reduce(lambda x, y: x + [f(y)], xs, [])


# generators
def my_filter(f, xs):
    return reduce(lambda x, y: x + [y] if f(y) else x, xs, [])


# generators
def replicate_each(n, xs):
    return reduce(lambda x, y: x + [y] * n, xs, [])
