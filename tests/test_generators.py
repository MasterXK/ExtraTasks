import pytest

from src.generators import *


@pytest.mark.parametrize(
    "check_list, expected_result",
    [
        ([], []),
        ([[], []], []),
        ([[0]], []),
        ([[0, ""], [False, None]], []),
        ([[0, 1, 2], [], [], [False, True, 42]], [[1, 2], [True, 42]]),
    ],
)
def test_non_empty_truths(check_list, expected_result):
    assert non_empty_truths(check_list) == expected_result


@pytest.mark.parametrize(
    "matrix, expected_result",
    [
        ([[1, 2], [3, 4]], True),
        ([[1, None], [3, 4]], False),
        ([], True),
    ],
)
def test_each2d(matrix, expected_result):
    def is_int(x):
        return isinstance(x, int)

    assert each2d(is_int, matrix) is expected_result


@pytest.mark.parametrize(
    "matrix, expected_result",
    [
        ([[None, "foo"], [(), {}]], False),
        ([[None, "foo"], [0, {}]], True),
        ([], False),
    ],
)
def test_some2d(matrix, expected_result):
    def is_int(x):
        return isinstance(x, int)

    assert some2d(is_int, matrix) is expected_result


def test_sum2d():
    def is_int(x):
        return isinstance(x, int)

    assert sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]) == 111
