import pytest

from ..extra import *


@pytest.fixture
def products():
    return [
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 25, "category": "w", "quantity": 2},
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 55, "category": "e", "quantity": 4},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]


@pytest.fixture
def orders():
    return [
        {
            "id": "1",
            "date": "2019-04-03T18:35:29.512364",
            "items": [
                {"name": "", "price": 1, "quantity": 2},
                {"name": "", "price": 3, "quantity": 3},
                {"name": "", "price": 4, "quantity": 5},
            ],
        },
        {"id": "2", "date": "2019-05-03T18:35:29.512364", "items": [{"name": "", "price": 2, "quantity": 3}]},
        {"id": "3", "date": "2019-05-06T18:35:29.512364", "items": [{"name": "", "price": 3, "quantity": 3}]},
        {"id": "4", "date": "2019-07-10T18:35:29.512364", "items": [{"name": "", "price": 3, "quantity": 2}]},
        {"id": "5", "date": "2019-07-12T18:35:29.512364", "items": [{"name": "", "price": 10, "quantity": 1}]},
    ]


@pytest.fixture
def coll():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize(
    "words, result",
    [
        (["hello", "world", "apple", "pear", "banana", "pop"], ["pop"]),
        ([" ", "madam", "racecar", "noon", "level", " "], [" ", "madam", "racecar", "noon", "level", " "]),
        ([], []),
    ],
)
def test_get_similar(words, result):
    assert get_similar(words) == result


'''def test_get_dir_content():
    assert get_dir_content(".") == {"files": 5, "folders": 6}
    assert get_dir_content(".", count_all=True) == {"files": 816, "folders": 123}'''


@pytest.mark.parametrize("nums, result", [([2, 3, 5, 7, 11], 77),
                                          ([-5, -7, -9, -13], 117),
                                          ([1, 2], 2),
                                          ([4], 0)])
def test_get_max_multiply(nums, result):
    assert get_max_multiply(nums) == result


def test_sort_by_price(products):
    assert sort_by_price(products) == [
        {"name": "", "price": 55, "category": "e", "quantity": 4},
        {"name": "", "price": 25, "category": "w", "quantity": 2},
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]
    assert sort_by_price(products, category="q") == [
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]


def test_get_months_statistic(orders):
    assert get_months_statistic(orders) == {
        "2019.04": {"average_order_value": 20.0, "order_count": 1},
        "2019.05": {"average_order_value": 7.5, "order_count": 2},
        "2019.07": {"average_order_value": 8.0, "order_count": 2},
    }


def test_sum_divisible_by_3_or_5_common_input():
    assert sum_divisible_by_3_or_5([3, 15, 21, 5, 10]) == 54


def test_sum_divisible_by_3_or_5_empty_input():
    assert sum_divisible_by_3_or_5([]) == 0


def test_sum_divisible_by_3_or_5_without_correct_nums():
    assert sum_divisible_by_3_or_5([4, 16, 7, 11, 31]) == 0


def test_check_email_with_valid_email():
    assert check_email("smth@mail.ru") is True


@pytest.mark.parametrize("email, expected_result", [('smth-mail.ru', False),
                                                    ('smth@mail-ru', False),
                                                    ('smthmailru', False)])
def test_check_email_with_invalid_email(email, expected_result):
    assert check_email(email) is expected_result


def test_check_email_with_empty_email():
    assert check_email('') is False


@pytest.mark.parametrize("numbers, number, expected_result", [([1, 2, 3, 4, 3, 5, ], 3, 2),
                                                              ([-1, -2, -3, 2, -3, 2, ], 2, 2),
                                                              ([1.1, 2.2, 3.2, 4, 3.2, 5, ], 3, 0),
                                                              ([-1.2, 0, -3.4, 0, 3.5, 0, 0.9], 0, 3)])
def test_count_number_in_list(numbers, number, expected_result):
    assert count_number_in_list(numbers, number) == expected_result


@pytest.mark.parametrize("shape, sides, expected_result", [('квадрат', 2, 4.00),
                                                           ('квадрат', [2], 4.00),
                                                           ('квадрат', [2, 2, 2, 2], 4.00),
                                                           ('квадрат', [2, 3, 2, 2], None),
                                                           ('квадрат', [2, 2, 2], None),
                                                           ('прямоугольник', [2, 3], 6.00),
                                                           ('прямоугольник', [2, 2, 3, 3, ], 6.00),
                                                           ('прямоугольник', [2, 3, 2, 3], 6.00),
                                                           ('прямоугольник', [2, 3, 4, 3], None),
                                                           ('прямоугольник', [2, 3, 3], None),
                                                           ('треугольник', [2, 3, 4], 2.90),
                                                           ('треугольник', [2, 3, 5], None),
                                                           ('треугольник', [2, 3], None),
                                                           ('круг', 3, 28.27),
                                                           ('круг', [3], 28.27),
                                                           ('круг', [2, 3], None)])
def test_calculate_area(shape, sides, expected_result):
    assert calculate_area(shape, sides) == expected_result


@pytest.mark.parametrize("start, end, expected_result", [(1, None, [2, 3, 4, 5]),
                                                         (1, 4, [2, 3, 4]),
                                                         (1, 3, [2, 3]),
                                                         (-4, 3, [2, 3]),
                                                         (-7, 3, [1, 2, 3]),
                                                         (1, -2, [2, 3]),
                                                         (-4, -1, [2, 3, 4])])
def test_my_slice(coll, start, end, expected_result):
    assert my_slice(coll, start, end) == expected_result


@pytest.mark.parametrize("check_list, expected_result",
                         [([], []),
                          ([[], []], []),
                          ([[0]], []),
                          ([[0, ""], [False, None]], []),
                          ([[0, 1, 2], [], [], [False, True, 42]], [[1, 2], [True, 42]])]
                         )
def test_non_empty_truths(check_list, expected_result):
    assert non_empty_truths(check_list) == expected_result


@pytest.mark.parametrize("matrix, expected_result", [([[1, 2], [3, 4]], True),
                                                     ([[1, None], [3, 4]], False),
                                                     ([], True),])
def test_each2d(matrix, expected_result):
    def is_int(x):
        return isinstance(x, int)

    assert each2d(is_int, matrix) is expected_result


@pytest.mark.parametrize("matrix, expected_result", [([[None, "foo"], [(), {}]], False),
                                                     ([[None, "foo"], [0, {}]], True),
                                                     ([], False),])
def test_some2d(matrix, expected_result):
    def is_int(x):
        return isinstance(x, int)

    assert some2d(is_int, matrix) is expected_result


def test_sum2d():
    def is_int(x):
        return isinstance(x, int)

    assert sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]) == 111
