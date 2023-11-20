from typing import Optional


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
