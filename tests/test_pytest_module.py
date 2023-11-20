import pytest

from src.pytest_module import *


@pytest.fixture
def coll():
    return [1, 2, 3, 4, 5]


def test_sum_divisible_by_3_or_5_common_input():
    assert sum_divisible_by_3_or_5([3, 15, 21, 5, 10]) == 54


# tests
def test_sum_divisible_by_3_or_5_empty_input():
    assert sum_divisible_by_3_or_5([]) == 0


# tests
def test_sum_divisible_by_3_or_5_without_correct_nums():
    assert sum_divisible_by_3_or_5([4, 16, 7, 11, 31]) == 0


# tests
def test_check_email_with_valid_email():
    assert check_email("smth@mail.ru") is True


# tests
@pytest.mark.parametrize(
    "email, expected_result",
    [("smth-mail.ru", False), ("smth@mail-ru", False), ("smthmailru", False)],
)
def test_check_email_with_invalid_email(email, expected_result):
    assert check_email(email) is expected_result


# tests
def test_check_email_with_empty_email():
    assert check_email("") is False


# tests
@pytest.mark.parametrize(
    "numbers, number, expected_result",
    [
        (
            [
                1,
                2,
                3,
                4,
                3,
                5,
            ],
            3,
            2,
        ),
        (
            [
                -1,
                -2,
                -3,
                2,
                -3,
                2,
            ],
            2,
            2,
        ),
        (
            [
                1.1,
                2.2,
                3.2,
                4,
                3.2,
                5,
            ],
            3,
            0,
        ),
        ([-1.2, 0, -3.4, 0, 3.5, 0, 0.9], 0, 3),
    ],
)
def test_count_number_in_list(numbers, number, expected_result):
    assert count_number_in_list(numbers, number) == expected_result


@pytest.mark.parametrize(
    "shape, sides, expected_result",
    [
        ("квадрат", 2, 4.00),
        ("квадрат", [2], 4.00),
        ("квадрат", [2, 2, 2, 2], 4.00),
        ("квадрат", [2, 3, 2, 2], None),
        ("квадрат", [2, 2, 2], None),
        ("прямоугольник", [2, 3], 6.00),
        (
            "прямоугольник",
            [
                2,
                2,
                3,
                3,
            ],
            6.00,
        ),
        ("прямоугольник", [2, 3, 2, 3], 6.00),
        ("прямоугольник", [2, 3, 4, 3], None),
        ("прямоугольник", [2, 3, 3], None),
        ("треугольник", [2, 3, 4], 2.90),
        ("треугольник", [2, 3, 5], None),
        ("треугольник", [2, 3], None),
        ("круг", 3, 28.27),
        ("круг", [3], 28.27),
        ("круг", [2, 3], None),
    ],
)
def test_calculate_area(shape, sides, expected_result):
    assert calculate_area(shape, sides) == expected_result


# tests
@pytest.mark.parametrize(
    "start, end, expected_result",
    [
        (1, None, [2, 3, 4, 5]),
        (1, 4, [2, 3, 4]),
        (1, 3, [2, 3]),
        (-4, 3, [2, 3]),
        (-7, 3, [1, 2, 3]),
        (1, -2, [2, 3]),
        (-4, -1, [2, 3, 4]),
    ],
)
def test_my_slice(coll, start, end, expected_result):
    assert my_slice(coll, start, end) == expected_result
